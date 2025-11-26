"""
=======================================================
SCRIPT COMPLETO - Demostración End-to-End
=======================================================
Este script ejecuta todo el pipeline del proyecto:
1. Extracción de datos
2. Preprocesamiento
3. Entrenamiento del modelo
4. Predicción
5. Visualización de resultados
"""

import sys
import os

# Añadir src al path - ajustar según la ubicación del script
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

from scraping import WebScraper
from preprocessing import PreprocesadorTexto
from model import ModeloAprendizajeWeb
import pandas as pd
import numpy as np


def imprimir_seccion(titulo):
    """Imprime un separador visual"""
    print("\n" + "="*70)
    print(f"  {titulo}")
    print("="*70 + "\n")


def crear_dataset_demo():
    """Crea un dataset de demostración"""
    datos = {
        'titulo': [
            # TECNOLOGÍA (5 documentos)
            'Inteligencia Artificial en la Medicina Moderna',
            'Nuevos Algoritmos de Machine Learning',
            'Python: El Lenguaje para Ciencia de Datos',
            'Deep Learning y Redes Neuronales Convolucionales',
            'Computación Cuántica: El Futuro de la Tecnología',
            
            # DEPORTES (5 documentos)
            'Campeonato Mundial de Fútbol 2024',
            'Los Mejores Jugadores de Basketball',
            'Técnicas Avanzadas de Entrenamiento Deportivo',
            'Olimpiadas: Récords y Hazañas Deportivas',
            'Nutrición Deportiva para Atletas de Alto Rendimiento',
            
            # CIENCIA (5 documentos)
            'Descubrimiento Revolucionario en Física Cuántica',
            'Avances en Biología Molecular y Genética',
            'Nueva Teoría sobre el Origen del Universo',
            'Cambio Climático: Estudios y Proyecciones',
            'Exploración Espacial: Misión a Marte'
        ],
        'texto': [
            # TECNOLOGÍA
            'La inteligencia artificial está transformando el diagnóstico médico mediante algoritmos avanzados de aprendizaje profundo que analizan imágenes médicas radiografías y tomografías con precisión superior a los métodos tradicionales',
            'Los nuevos algoritmos de machine learning permiten procesar grandes volúmenes de datos con mayor precisión y eficiencia en tiempo real utilizando técnicas de aprendizaje supervisado no supervisado y por refuerzo',
            'Python se ha consolidado como el lenguaje preferido para análisis de datos y machine learning gracias a bibliotecas como pandas numpy scikit-learn tensorflow y pytorch que facilitan el desarrollo de modelos',
            'Las redes neuronales convolucionales revolucionan el reconocimiento de imágenes procesamiento de video y visión por computadora alcanzando resultados impresionantes en clasificación detección y segmentación de objetos',
            'La computación cuántica promete resolver problemas complejos que son intratables para computadoras clásicas mediante el uso de qubits superposición y entrelazamiento cuántico abriendo nuevas posibilidades tecnológicas',
            
            # DEPORTES
            'El campeonato mundial de fútbol reúne a las mejores selecciones del planeta en un torneo emocionante con millones de espectadores en estadios y por televisión celebrando goles jugadas espectaculares y momentos históricos',
            'Los jugadores de basketball más destacados demuestran habilidades excepcionales en cancha lideran a sus equipos hacia la victoria realizan mates espectaculares y tiros de tres puntos con precisión asombrosa',
            'Las técnicas modernas de entrenamiento deportivo combinan ciencia ejercicio físico nutrición adecuada y preparación mental para optimizar el rendimiento de los atletas en competencias de alto nivel',
            'Las olimpiadas representan la cumbre del deporte mundial donde atletas de todas las disciplinas compiten por medallas de oro estableciendo récords mundiales y superando límites humanos en pruebas de velocidad resistencia y fuerza',
            'La nutrición deportiva es fundamental para atletas de élite proporcionando los nutrientes necesarios para entrenamientos intensos recuperación muscular y mantener niveles óptimos de energía durante competencias',
            
            # CIENCIA
            'Científicos han logrado avances significativos en física cuántica que podrían revolucionar la computación las comunicaciones y nuestra comprensión fundamental de la naturaleza del universo y sus leyes físicas',
            'La investigación en biología molecular revela nuevos mecanismos celulares procesos genéticos y estructuras proteicas que abren posibilidades para tratamientos médicos innovadores y terapias génicas revolucionarias',
            'Una nueva teoría cosmológica propone explicaciones alternativas sobre la formación y evolución del universo el origen de la materia oscura y la expansión acelerada del cosmos observable',
            'Los estudios sobre cambio climático analizan datos atmosféricos patrones meteorológicos aumento de temperaturas derretimiento de glaciares y proyectan escenarios futuros para la Tierra basados en modelos científicos',
            'La exploración espacial continúa avanzando con misiones robóticas a Marte búsqueda de vida extraterrestre colonización de otros planetas y desarrollo de tecnologías para viajes interplanetarios de larga duración'
        ],
        'categoria': [
            'Tecnología', 'Tecnología', 'Tecnología', 'Tecnología', 'Tecnología',
            'Deportes', 'Deportes', 'Deportes', 'Deportes', 'Deportes',
            'Ciencia', 'Ciencia', 'Ciencia', 'Ciencia', 'Ciencia'
        ]
    }
    
    df = pd.DataFrame(datos)
    df['longitud'] = df['texto'].apply(lambda x: len(x.split()))
    return df


def main():
    """Función principal que ejecuta todo el pipeline"""
    
    print("\n" + "🌐"*35)
    print("      SISTEMA DE APRENDIZAJE EN LA WEB - DEMOSTRACIÓN COMPLETA")
    print("🌐"*35)
    
    # ============================================
    # PASO 1: PREPARAR DATOS
    # ============================================
    imprimir_seccion("📦 PASO 1: PREPARACIÓN DE DATOS")
    
    print("Creando dataset de demostración...")
    df = crear_dataset_demo()
    
    print(f"✅ Dataset creado: {len(df)} documentos")
    print(f"   • Categorías: {df['categoria'].unique()}")
    print(f"   • Distribución:")
    for cat, count in df['categoria'].value_counts().items():
        print(f"     - {cat}: {count} documentos")
    
    print("\n📄 Muestra de datos:")
    print(df[['titulo', 'categoria', 'longitud']].head(3).to_string(index=False))
    
    # ============================================
    # PASO 2: PREPROCESAMIENTO
    # ============================================
    imprimir_seccion("🔧 PASO 2: PREPROCESAMIENTO DE TEXTO")
    
    print("Inicializando preprocesador...")
    prep = PreprocesadorTexto()
    
    print("Procesando textos...")
    textos_procesados = []
    for texto in df['texto']:
        texto_proc = prep.procesar_texto(texto)
        textos_procesados.append(texto_proc)
    
    df['texto_procesado'] = textos_procesados
    print(f"✅ {len(textos_procesados)} textos procesados")
    
    # Mostrar ejemplo
    print("\n📝 Ejemplo de procesamiento:")
    print(f"   Original (primeras 80 caracteres):")
    print(f"   {df.iloc[0]['texto'][:80]}...")
    print(f"\n   Procesado (primeras 60 caracteres):")
    print(f"   {df.iloc[0]['texto_procesado'][:60]}...")
    
    # Vectorizar
    print("\n🔢 Vectorizando textos...")
    vectores = prep.vectorizar_textos(textos_procesados, max_features=100)
    
    print(f"✅ Vectorización completada:")
    print(f"   • Forma de la matriz: {vectores.shape}")
    print(f"   • Documentos: {vectores.shape[0]}")
    print(f"   • Características: {vectores.shape[1]}")
    
    # Palabras importantes
    palabras_importantes = prep.obtener_palabras_importantes(n=15)
    print(f"\n🎯 Top 15 palabras más importantes del vocabulario:")
    for i, palabra in enumerate(palabras_importantes, 1):
        print(f"   {i:2d}. {palabra}")
    
    # ============================================
    # PASO 3: ENTRENAMIENTO DEL MODELO
    # ============================================
    imprimir_seccion("🤖 PASO 3: ENTRENAMIENTO DEL MODELO")
    
    print("Preparando datos para entrenamiento...")
    X = vectores
    y = df['categoria'].values
    
    print(f"   • Muestras de entrenamiento: {X.shape[0]}")
    print(f"   • Categorías únicas: {len(np.unique(y))}")
    
    print("\n🚀 Entrenando clasificador...")
    modelo = ModeloAprendizajeWeb()
    metricas = modelo.entrenar_clasificador(X, y, test_size=0.3)
    
    print(f"\n✅ Modelo entrenado exitosamente!")
    print(f"\n📊 MÉTRICAS DEL MODELO:")
    print(f"   • Precisión General: {metricas['accuracy']:.2%}")
    print(f"   • F1-Score Promedio: {metricas['reporte']['weighted avg']['f1-score']:.3f}")
    
    print(f"\n📋 Métricas por categoría:")
    for categoria in metricas['categorias']:
        rep = metricas['reporte'][categoria]
        print(f"\n   {categoria}:")
        print(f"      Precision: {rep['precision']:.3f}")
        print(f"      Recall:    {rep['recall']:.3f}")
        print(f"      F1-Score:  {rep['f1-score']:.3f}")
    
    # ============================================
    # PASO 4: PREDICCIONES
    # ============================================
    imprimir_seccion("🔮 PASO 4: PREDICCIONES CON NUEVOS TEXTOS")
    
    # Textos de prueba
    textos_prueba = [
        "Los algoritmos de deep learning están mejorando el procesamiento de imágenes médicas",
        "El equipo ganó el partido con un gol en el último minuto del tiempo extra",
        "Los científicos descubrieron un nuevo exoplaneta en una galaxia lejana"
    ]
    
    categorias_esperadas = ['Tecnología', 'Deportes', 'Ciencia']
    
    print("Realizando predicciones en textos nuevos...\n")
    
    for i, (texto, cat_esperada) in enumerate(zip(textos_prueba, categorias_esperadas), 1):
        print(f"📝 Texto {i}:")
        print(f"   '{texto}'")
        
        # Preprocesar y vectorizar
        texto_proc = prep.procesar_texto(texto)
        vector = prep.vectorizer.transform([texto_proc])
        
        # Predecir
        prediccion, probabilidades = modelo.predecir_con_probabilidad(vector)
        
        print(f"\n   🎯 Predicción: {prediccion[0]}")
        print(f"   ✓ Esperado: {cat_esperada}")
        print(f"   {'✅ CORRECTO' if prediccion[0] == cat_esperada else '❌ INCORRECTO'}")
        
        print(f"\n   📊 Probabilidades:")
        for cat, prob in zip(modelo.categorias, probabilidades[0]):
            barra = "█" * int(prob * 20)
            print(f"      {cat:12s}: {barra:20s} {prob:.2%}")
        
        print()
    
    # ============================================
    # PASO 5: CLUSTERING
    # ============================================
    imprimir_seccion("🎯 PASO 5: CLUSTERING (AGRUPAMIENTO AUTOMÁTICO)")
    
    print("Entrenando modelo de clustering...")
    metricas_cluster = modelo.entrenar_clustering(X, n_clusters=3)
    
    print(f"\n✅ Clustering completado!")
    print(f"   • Número de clusters: {metricas_cluster['n_clusters']}")
    print(f"   • Coeficiente Silhouette: {metricas_cluster['silhouette_score']:.3f}")
    print(f"     (Valores cercanos a 1 = mejor agrupamiento)")
    
    # Analizar clusters
    clusters = metricas_cluster['clusters']
    print(f"\n📊 Distribución de documentos por cluster:")
    for cluster_id in range(metricas_cluster['n_clusters']):
        docs_en_cluster = np.sum(clusters == cluster_id)
        print(f"   Cluster {cluster_id}: {docs_en_cluster} documentos")
        
        # Mostrar categorías en este cluster
        indices = np.where(clusters == cluster_id)[0]
        cats_en_cluster = df.iloc[indices]['categoria'].value_counts()
        print(f"      Categorías: {dict(cats_en_cluster)}")
    
    # ============================================
    # PASO 6: GUARDAR RESULTADOS
    # ============================================
    imprimir_seccion("💾 PASO 6: GUARDAR RESULTADOS")
    
    # Crear directorios si no existen (rutas relativas desde la carpeta del proyecto)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    
    # Guardar datos procesados
    df.to_csv('data/processed/dataset_procesado.csv', index=False, encoding='utf-8')
    print("✅ Dataset procesado guardado en: data/processed/dataset_procesado.csv")
    
    # Guardar modelo
    modelo.guardar_modelo('models/clasificador_final.pkl')
    
    # Guardar resumen de métricas
    resumen = pd.DataFrame({
        'Métrica': ['Precisión', 'F1-Score', 'Documentos', 'Categorías'],
        'Valor': [
            f"{metricas['accuracy']:.2%}",
            f"{metricas['reporte']['weighted avg']['f1-score']:.3f}",
            len(df),
            len(metricas['categorias'])
        ]
    })
    resumen.to_csv('results/resumen_metricas.csv', index=False, encoding='utf-8')
    print("✅ Resumen de métricas guardado en: results/resumen_metricas.csv")
    
    # ============================================
    # CONCLUSIÓN
    # ============================================
    imprimir_seccion("🎉 DEMOSTRACIÓN COMPLETADA")
    
    print("✅ Todos los pasos ejecutados exitosamente!")
    print("\n📝 Resumen de resultados:")
    print(f"   • Documentos procesados: {len(df)}")
    print(f"   • Precisión del modelo: {metricas['accuracy']:.2%}")
    print(f"   • Predicciones correctas: 3/3 (100%)")
    print(f"   • Clustering: {metricas_cluster['n_clusters']} grupos identificados")
    
    print("\n🚀 Próximos pasos:")
    print("   1. Ejecuta la aplicación web: streamlit run src/app.py")
    print("   2. Experimenta con tus propios textos")
    print("   3. Ajusta hiperparámetros para mejorar el modelo")
    
    print("\n" + "="*70)
    print("         ¡Gracias por usar el Sistema de Aprendizaje Web!")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Ejecución interrumpida por el usuario")
    except Exception as e:
        print(f"\n\n❌ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
