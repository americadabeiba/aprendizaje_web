"""
=======================================================
MÓDULO: CATEGORIZACIÓN AUTOMÁTICA
=======================================================
Este módulo identifica categorías automáticamente usando:
1. Clustering (K-Means) - Agrupa documentos similares
2. Análisis de Keywords - Identifica temas principales
3. Asignación de etiquetas - Nombra los grupos automáticamente
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import re


class CategorizadorAutomatico:
    """Clase para identificar categorías automáticamente"""
    
    def __init__(self):
        self.clusters = None
        self.keywords_por_cluster = {}
        self.etiquetas_sugeridas = {}
        
        # Diccionario de palabras clave por dominio
        self.dominios = {
            'Música': ['música', 'canción', 'cantante', 'álbum', 'banda', 'artista', 
                       'concierto', 'disco', 'vocal', 'instrumento', 'melodía', 'compositor',
                       'hip', 'hop', 'rock', 'pop', 'jazz', 'folk', 'electrónic', 'rap'],
            
            'Deportes': ['deporte', 'jugador', 'equipo', 'partido', 'campeonato', 'fútbol',
                        'basketball', 'tenis', 'olimp', 'medalla', 'entrenamiento', 'atleta',
                        'gol', 'canasta', 'victoria', 'competencia', 'campeón'],
            
            'Tecnología': ['tecnología', 'software', 'programa', 'computadora', 'internet',
                          'algoritmo', 'dato', 'inteligencia', 'artificial', 'machine', 'learning',
                          'python', 'código', 'desarrollo', 'aplicación', 'digital', 'red',
                          'neuronal', 'modelo', 'sistema'],
            
            'Ciencia': ['científico', 'investigación', 'estudio', 'experimento', 'teoría',
                       'física', 'química', 'biología', 'átomo', 'molécula', 'célula',
                       'universo', 'planeta', 'espacio', 'laboratorio', 'análisis'],
            
            'Política': ['político', 'gobierno', 'presidente', 'parlamento', 'ley',
                        'elección', 'partido', 'votación', 'democracia', 'estado'],
            
            'Economía': ['económico', 'mercado', 'empresa', 'negocio', 'dinero',
                        'banco', 'inversión', 'finanza', 'comercio', 'producto'],
            
            'Arte': ['arte', 'pintura', 'artista', 'obra', 'museo', 'exposición',
                    'escultura', 'creativo', 'estético', 'cultura'],
            
            'Literatura': ['libro', 'autor', 'novela', 'escritor', 'poesía', 'texto',
                          'literario', 'narrativa', 'cuento', 'página'],
            
            'Cine': ['película', 'cine', 'director', 'actor', 'film', 'escena',
                    'producción', 'estreno', 'pantalla', 'audiovisual'],
            
            'Historia': ['histórico', 'siglo', 'guerra', 'antiguo', 'época',
                        'civilización', 'imperio', 'revolución', 'pasado']
        }
    
    def detectar_categoria_por_keywords(self, texto_procesado, top_n=10):
        """
        Detecta la categoría basándose en palabras clave
        
        Args:
            texto_procesado: Texto ya preprocesado
            top_n: Número de palabras a considerar
            
        Returns:
            Tupla (categoria, confianza)
        """
        # Obtener palabras del texto
        palabras = texto_procesado.lower().split()
        
        # Contar coincidencias con cada dominio
        scores = {}
        for dominio, keywords in self.dominios.items():
            score = 0
            for palabra in palabras:
                for keyword in keywords:
                    # Coincidencia parcial (por ejemplo: "música" coincide con "musical")
                    if keyword in palabra or palabra in keyword:
                        score += 1
            scores[dominio] = score
        
        # Encontrar la mejor categoría
        if max(scores.values()) == 0:
            return ("Sin Clasificar", 0.0)
        
        mejor_categoria = max(scores, key=scores.get)
        total_matches = sum(scores.values())
        confianza = scores[mejor_categoria] / total_matches if total_matches > 0 else 0
        
        return (mejor_categoria, confianza)
    
    def categorizar_documentos(self, textos_procesados, umbral_confianza=0.3):
        """
        Categoriza múltiples documentos automáticamente
        
        Args:
            textos_procesados: Lista de textos preprocesados
            umbral_confianza: Confianza mínima para asignar categoría (0-1)
            
        Returns:
            DataFrame con categorías y confianzas
        """
        resultados = []
        
        for i, texto in enumerate(textos_procesados):
            categoria, confianza = self.detectar_categoria_por_keywords(texto)
            
            # Si la confianza es baja, marcar como "Incierto"
            if confianza < umbral_confianza:
                categoria = "Incierto"
            
            resultados.append({
                'indice': i,
                'categoria': categoria,
                'confianza': confianza
            })
        
        return pd.DataFrame(resultados)
    
    def clustering_con_etiquetas(self, X, n_clusters='auto', textos_procesados=None):
        """
        Realiza clustering y sugiere etiquetas para cada grupo
        
        Args:
            X: Matriz de características (TF-IDF)
            n_clusters: Número de clusters o 'auto' para detección automática
            textos_procesados: Textos procesados para análisis de keywords
            
        Returns:
            Dict con clusters, etiquetas sugeridas y keywords
        """
        # Determinar número óptimo de clusters si es 'auto'
        if n_clusters == 'auto':
            n_docs = X.shape[0]
            if n_docs < 6:
                n_clusters = 2
            elif n_docs < 15:
                n_clusters = 3
            else:
                n_clusters = min(5, n_docs // 5)
            
            print(f"📊 Clusters detectados automáticamente: {n_clusters}")
        
        # Realizar clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X)
        
        self.clusters = clusters
        
        # Si no hay textos procesados, solo devolver clusters
        if textos_procesados is None:
            return {
                'clusters': clusters,
                'n_clusters': n_clusters,
                'etiquetas': [f"Grupo {i+1}" for i in range(n_clusters)]
            }
        
        # Analizar keywords por cluster
        etiquetas_sugeridas = []
        keywords_por_cluster = {}
        
        for cluster_id in range(n_clusters):
            # Obtener textos de este cluster
            indices = np.where(clusters == cluster_id)[0]
            textos_cluster = [textos_procesados[i] for i in indices]
            
            # Unir todos los textos del cluster
            texto_completo = ' '.join(textos_cluster)
            
            # Obtener palabras más frecuentes
            palabras = texto_completo.split()
            palabra_counts = Counter(palabras)
            top_keywords = [palabra for palabra, _ in palabra_counts.most_common(5)]
            keywords_por_cluster[cluster_id] = top_keywords
            
            # Intentar identificar la categoría del cluster
            categoria, confianza = self.detectar_categoria_por_keywords(texto_completo)
            
            if confianza > 0.2:
                etiqueta = f"{categoria}"
            else:
                # Usar la palabra más común como etiqueta
                etiqueta = f"Tema: {top_keywords[0].title()}" if top_keywords else f"Grupo {cluster_id+1}"
            
            etiquetas_sugeridas.append(etiqueta)
        
        self.keywords_por_cluster = keywords_por_cluster
        self.etiquetas_sugeridas = etiquetas_sugeridas
        
        return {
            'clusters': clusters,
            'n_clusters': n_clusters,
            'etiquetas': etiquetas_sugeridas,
            'keywords': keywords_por_cluster
        }
    
    def analizar_y_categorizar(self, df, columna_texto='texto_procesado'):
        """
        Pipeline completo: analiza el dataframe y asigna categorías automáticamente
        
        Args:
            df: DataFrame con los documentos
            columna_texto: Nombre de la columna con texto procesado
            
        Returns:
            DataFrame con columna 'categoria_auto' añadida
        """
        textos = df[columna_texto].tolist()
        
        # Método 1: Por keywords
        print("🔍 Analizando por palabras clave...")
        df_categorias = self.categorizar_documentos(textos)
        
        # Añadir al dataframe original
        df['categoria_auto'] = df_categorias['categoria'].values
        df['confianza_categoria'] = df_categorias['confianza'].values
        
        # Estadísticas
        print(f"\n✅ Categorización completada:")
        print(f"   • Total documentos: {len(df)}")
        print(f"   • Categorías encontradas: {df['categoria_auto'].nunique()}")
        print(f"\n📊 Distribución:")
        for cat, count in df['categoria_auto'].value_counts().items():
            avg_conf = df[df['categoria_auto']==cat]['confianza_categoria'].mean()
            print(f"   • {cat}: {count} docs (confianza promedio: {avg_conf:.2f})")
        
        return df
    
    def agregar_keywords_personalizadas(self, dominio, keywords):
        """
        Permite agregar keywords personalizadas para un dominio
        
        Args:
            dominio: Nombre del dominio (ej: 'Música Rock', 'Videojuegos')
            keywords: Lista de palabras clave
        """
        self.dominios[dominio] = keywords
        print(f"✅ Dominio '{dominio}' agregado con {len(keywords)} keywords")


# ========================================
# EJEMPLO DE USO
# ========================================
if __name__ == "__main__":
    from preprocessing import PreprocesadorTexto
    
    print("="*70)
    print("EJEMPLO DE CATEGORIZACIÓN AUTOMÁTICA")
    print("="*70)
    
    # Textos de ejemplo SIN categorías predefinidas
    textos_ejemplo = [
        # Música
        "FKA Twigs es una cantante británica conocida por su música experimental y videos artísticos innovadores",
        "Ichiko Aoba es una compositora y cantante japonesa de música folk con influencias de jazz",
        "Death Grips es un grupo experimental de hip hop conocido por su sonido agresivo",
        
        # Tecnología
        "Python es un lenguaje de programación muy usado en ciencia de datos y machine learning",
        "Los algoritmos de deep learning están revolucionando la inteligencia artificial",
        "El desarrollo de software requiere conocimientos de programación y arquitectura de sistemas",
        
        # Deportes
        "El campeonato mundial de fútbol reúne a los mejores equipos del planeta",
        "Los jugadores de basketball entrenan diariamente para mejorar su técnica",
        "Las olimpiadas son el evento deportivo más importante del mundo"
    ]
    
    titulos = [
        "FKA Twigs", "Ichiko Aoba", "Death Grips",
        "Python", "Deep Learning", "Desarrollo Software",
        "Mundial Fútbol", "Basketball", "Olimpiadas"
    ]
    
    # Preprocesar
    print("\n🔧 Preprocesando textos...")
    prep = PreprocesadorTexto()
    textos_procesados = [prep.procesar_texto(t) for t in textos_ejemplo]
    
    # Crear DataFrame
    df = pd.DataFrame({
        'titulo': titulos,
        'texto': textos_ejemplo,
        'texto_procesado': textos_procesados
    })
    
    # Categorizar automáticamente
    print("\n" + "="*70)
    categorizador = CategorizadorAutomatico()
    df = categorizador.analizar_y_categorizar(df)
    
    # Mostrar resultados
    print("\n📋 RESULTADOS:")
    print(df[['titulo', 'categoria_auto', 'confianza_categoria']].to_string(index=False))
    
    # Ejemplo con clustering
    print("\n" + "="*70)
    print("CLUSTERING AUTOMÁTICO")
    print("="*70)
    
    # Vectorizar
    vectores = prep.vectorizar_textos(textos_procesados)
    
    # Clustering con etiquetas automáticas
    resultado = categorizador.clustering_con_etiquetas(
        vectores, 
        n_clusters=3,
        textos_procesados=textos_procesados
    )
    
    print(f"\n📊 Se identificaron {resultado['n_clusters']} grupos:")
    for i, etiqueta in enumerate(resultado['etiquetas']):
        keywords = resultado['keywords'][i]
        docs_en_cluster = np.sum(resultado['clusters'] == i)
        print(f"\n   Grupo {i+1}: {etiqueta}")
        print(f"   • Documentos: {docs_en_cluster}")
        print(f"   • Keywords: {', '.join(keywords[:3])}")
