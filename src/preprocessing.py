"""
=======================================================
MÓDULO 2: PREPROCESAMIENTO - Limpieza y Transformación
=======================================================
Este módulo prepara el texto para el modelo de ML
"""

import re
import pandas as pd
import numpy as np
from typing import List
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings('ignore')


class PreprocesadorTexto:
    """Clase para preprocesar y vectorizar texto"""
    
    def __init__(self, idioma='spanish'):
        self.idioma = idioma
        self.stemmer = SnowballStemmer(idioma)
        
        # Descargar recursos de NLTK si no están disponibles
        try:
            self.stop_words = set(stopwords.words(idioma))
        except:
            nltk.download('stopwords', quiet=True)
            nltk.download('punkt', quiet=True)
            self.stop_words = set(stopwords.words(idioma))
        
        self.vectorizer = None
    
    def limpiar_texto(self, texto: str) -> str:
        """
        Limpia el texto eliminando elementos no deseados
        
        Args:
            texto: Texto a limpiar
            
        Returns:
            Texto limpio
        """
        # Convertir a minúsculas
        texto = texto.lower()
        
        # Eliminar URLs
        texto = re.sub(r'http\S+|www\S+', '', texto)
        
        # Eliminar números
        texto = re.sub(r'\d+', '', texto)
        
        # Eliminar puntuación y caracteres especiales
        texto = re.sub(r'[^\w\s]', ' ', texto)
        
        # Eliminar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto).strip()
        
        return texto
    
    def tokenizar(self, texto: str) -> List[str]:
        """
        Divide el texto en palabras (tokens)
        
        Args:
            texto: Texto a tokenizar
            
        Returns:
            Lista de tokens
        """
        return word_tokenize(texto, language=self.idioma)
    
    def eliminar_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Elimina palabras comunes sin significado relevante
        
        Args:
            tokens: Lista de tokens
            
        Returns:
            Tokens filtrados
        """
        return [token for token in tokens if token not in self.stop_words and len(token) > 2]
    
    def aplicar_stemming(self, tokens: List[str]) -> List[str]:
        """
        Reduce las palabras a su raíz
        Ejemplo: "corriendo" -> "corr"
        
        Args:
            tokens: Lista de tokens
            
        Returns:
            Tokens con stemming aplicado
        """
        return [self.stemmer.stem(token) for token in tokens]
    
    def procesar_texto(self, texto: str) -> str:
        """
        Pipeline completo de preprocesamiento
        
        Args:
            texto: Texto original
            
        Returns:
            Texto procesado
        """
        # 1. Limpiar
        texto = self.limpiar_texto(texto)
        
        # 2. Tokenizar
        tokens = self.tokenizar(texto)
        
        # 3. Eliminar stopwords
        tokens = self.eliminar_stopwords(tokens)
        
        # 4. Aplicar stemming
        tokens = self.aplicar_stemming(tokens)
        
        # Unir tokens de nuevo
        return ' '.join(tokens)
    
    def vectorizar_textos(self, textos: List[str], max_features: int = 1000):
        """
        Convierte textos en vectores numéricos usando TF-IDF
        
        Args:
            textos: Lista de textos
            max_features: Número máximo de características
            
        Returns:
            Matriz de vectores TF-IDF
        """
        print(f"🔢 Vectorizando {len(textos)} documentos...")
        
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 2),  # Usar unigramas y bigramas
            min_df=2,  # Ignorar términos que aparecen en menos de 2 documentos
            max_df=0.8  # Ignorar términos que aparecen en más del 80% de documentos
        )
        
        vectores = self.vectorizer.fit_transform(textos)
        
        print(f"✅ Vectorización completa: {vectores.shape[0]} documentos x {vectores.shape[1]} características")
        return vectores
    
    def obtener_palabras_importantes(self, n: int = 20) -> List[str]:
        """
        Obtiene las palabras más importantes del vocabulario
        
        Args:
            n: Número de palabras a retornar
            
        Returns:
            Lista de palabras importantes
        """
        if self.vectorizer is None:
            return []
        
        feature_names = self.vectorizer.get_feature_names_out()
        return list(feature_names[:n])


# ========================================
# EJEMPLO DE USO
# ========================================
if __name__ == "__main__":
    # Textos de ejemplo
    textos_ejemplo = [
        "La inteligencia artificial está revolucionando la tecnología moderna",
        "El aprendizaje automático permite que las máquinas aprendan de datos",
        "Python es el lenguaje de programación más popular para ciencia de datos",
        "Las redes neuronales son fundamentales en el deep learning actual"
    ]
    
    # Crear preprocesador
    prep = PreprocesadorTexto()
    
    print("="*60)
    print("EJEMPLO DE PREPROCESAMIENTO")
    print("="*60)
    
    # Procesar cada texto
    textos_procesados = []
    for i, texto in enumerate(textos_ejemplo, 1):
        print(f"\n📝 Texto {i} original:")
        print(f"   {texto}")
        
        texto_procesado = prep.procesar_texto(texto)
        textos_procesados.append(texto_procesado)
        
        print(f"🔧 Texto {i} procesado:")
        print(f"   {texto_procesado}")
    
    # Vectorizar textos
    print("\n" + "="*60)
    vectores = prep.vectorizar_textos(textos_procesados, max_features=50)
    
    # Mostrar palabras importantes
    palabras = prep.obtener_palabras_importantes(n=10)
    print(f"\n🎯 Top 10 palabras importantes:")
    for palabra in palabras:
        print(f"   • {palabra}")
    
    # Guardar resultados
    df_procesado = pd.DataFrame({
        'texto_original': textos_ejemplo,
        'texto_procesado': textos_procesados
    })
    df_procesado.to_csv('data/processed/textos_procesados.csv', index=False, encoding='utf-8')
    print("\n💾 Datos guardados en: data/processed/textos_procesados.csv")
