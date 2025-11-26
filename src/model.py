"""
=======================================================
MÓDULO 3: MODELO DE APRENDIZAJE - Clasificación y Clustering
=======================================================
Este módulo entrena modelos para clasificar y agrupar textos
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, silhouette_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple


class ModeloAprendizajeWeb:
    """Clase para entrenar modelos de clasificación y clustering"""
    
    def __init__(self):
        self.modelo_clasificacion = None
        self.modelo_clustering = None
        self.categorias = None
    
    def entrenar_clasificador(self, X, y, test_size=0.2):
        """
        Entrena un clasificador de texto
        
        Args:
            X: Matriz de características (vectores TF-IDF)
            y: Etiquetas de categorías
            test_size: Proporción de datos para prueba
            
        Returns:
            Métricas de evaluación
        """
        print("🤖 Entrenando clasificador...")
        
        # Calcular el tamaño mínimo necesario por clase
        n_samples = X.shape[0]
        n_classes = len(np.unique(y))
        min_samples_per_class = np.min(np.unique(y, return_counts=True)[1])
        
        # Ajustar test_size si es necesario para datasets pequeños
        # Necesitamos al menos 1 muestra por clase en test
        min_test_samples = n_classes
        adjusted_test_size = max(min_test_samples / n_samples, test_size)
        
        # Si el dataset es muy pequeño, usar stratify=None
        # Stratify requiere al menos 2 muestras por clase
        use_stratify = min_samples_per_class >= 2 and n_samples >= n_classes * 4
        
        if not use_stratify:
            print(f"⚠️ Dataset pequeño detectado ({n_samples} muestras, {n_classes} clases)")
            print(f"   Entrenando sin estratificación para evitar errores")
        
        # Dividir datos
        if use_stratify:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42, stratify=y
            )
        else:
            # Para datasets muy pequeños, usar split simple
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=adjusted_test_size, random_state=42
            )
        
        # Entrenar modelo (Naive Bayes Multinomial)
        self.modelo_clasificacion = MultinomialNB()
        self.modelo_clasificacion.fit(X_train, y_train)
        
        # Evaluar
        y_pred = self.modelo_clasificacion.predict(X_test)
        accuracy = self.modelo_clasificacion.score(X_test, y_test)
        
        print(f"✅ Entrenamiento completo - Precisión: {accuracy:.2%}")
        
        # Guardar categorías únicas
        self.categorias = np.unique(y)
        
        # Generar reporte
        reporte = classification_report(
            y_test, y_pred, 
            target_names=self.categorias,
            output_dict=True
        )
        
        # Matriz de confusión
        matriz_confusion = confusion_matrix(y_test, y_pred)
        
        return {
            'accuracy': accuracy,
            'reporte': reporte,
            'matriz_confusion': matriz_confusion,
            'categorias': self.categorias
        }
    
    def predecir(self, X) -> np.ndarray:
        """
        Realiza predicciones con el modelo entrenado
        
        Args:
            X: Matriz de características
            
        Returns:
            Array de predicciones
        """
        if self.modelo_clasificacion is None:
            raise ValueError("El modelo no ha sido entrenado")
        
        return self.modelo_clasificacion.predict(X)
    
    def predecir_con_probabilidad(self, X) -> Tuple[np.ndarray, np.ndarray]:
        """
        Realiza predicciones con probabilidades
        
        Args:
            X: Matriz de características
            
        Returns:
            Tupla (predicciones, probabilidades)
        """
        if self.modelo_clasificacion is None:
            raise ValueError("El modelo no ha sido entrenado")
        
        predicciones = self.modelo_clasificacion.predict(X)
        probabilidades = self.modelo_clasificacion.predict_proba(X)
        
        return predicciones, probabilidades
    
    def entrenar_clustering(self, X, n_clusters: int = 3):
        """
        Entrena un modelo de clustering (agrupamiento)
        
        Args:
            X: Matriz de características
            n_clusters: Número de grupos
            
        Returns:
            Métricas de clustering
        """
        print(f"🎯 Entrenando clustering con {n_clusters} grupos...")
        
        # Entrenar K-Means
        self.modelo_clustering = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )
        
        clusters = self.modelo_clustering.fit_predict(X)
        
        # Calcular calidad del clustering
        silhouette = silhouette_score(X, clusters)
        
        print(f"✅ Clustering completo - Coeficiente Silhouette: {silhouette:.3f}")
        
        return {
            'clusters': clusters,
            'silhouette_score': silhouette,
            'n_clusters': n_clusters,
            'centros': self.modelo_clustering.cluster_centers_
        }
    
    def visualizar_matriz_confusion(self, matriz, categorias, guardar_path=None):
        """
        Visualiza la matriz de confusión
        
        Args:
            matriz: Matriz de confusión
            categorias: Lista de nombres de categorías
            guardar_path: Ruta para guardar la imagen
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            matriz, 
            annot=True, 
            fmt='d', 
            cmap='Blues',
            xticklabels=categorias,
            yticklabels=categorias
        )
        plt.title('Matriz de Confusión', fontsize=16, pad=20)
        plt.ylabel('Categoría Real', fontsize=12)
        plt.xlabel('Categoría Predicha', fontsize=12)
        plt.tight_layout()
        
        if guardar_path:
            plt.savefig(guardar_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {guardar_path}")
        
        plt.show()
    
    def visualizar_distribucion_clusters(self, clusters, guardar_path=None):
        """
        Visualiza la distribución de documentos por cluster
        
        Args:
            clusters: Array de asignaciones de cluster
            guardar_path: Ruta para guardar la imagen
        """
        plt.figure(figsize=(10, 6))
        
        unique, counts = np.unique(clusters, return_counts=True)
        plt.bar(unique, counts, color='skyblue', edgecolor='navy')
        plt.xlabel('Cluster', fontsize=12)
        plt.ylabel('Número de Documentos', fontsize=12)
        plt.title('Distribución de Documentos por Cluster', fontsize=16, pad=20)
        plt.xticks(unique)
        
        for i, count in enumerate(counts):
            plt.text(i, count + 0.5, str(count), ha='center', va='bottom')
        
        plt.tight_layout()
        
        if guardar_path:
            plt.savefig(guardar_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {guardar_path}")
        
        plt.show()
    
    def guardar_modelo(self, ruta: str):
        """Guarda el modelo entrenado"""
        if self.modelo_clasificacion:
            joblib.dump(self.modelo_clasificacion, ruta)
            print(f"💾 Modelo guardado en: {ruta}")
    
    def cargar_modelo(self, ruta: str):
        """Carga un modelo previamente guardado"""
        self.modelo_clasificacion = joblib.load(ruta)
        print(f"📂 Modelo cargado desde: {ruta}")


# ========================================
# EJEMPLO DE USO CON DATOS SINTÉTICOS
# ========================================
if __name__ == "__main__":
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    print("="*60)
    print("EJEMPLO DE ENTRENAMIENTO DE MODELO")
    print("="*60)
    
    # Datos de ejemplo: artículos por categoría
    textos_tecnologia = [
        "inteligencia artificial machine learning algoritmos datos",
        "programacion python desarrollo software codigo",
        "redes neuronales deep learning tensorflow"
    ]
    
    textos_deportes = [
        "futbol balon gol jugadores partido",
        "basketball canasta equipo entrenamiento",
        "tenis raqueta partido campeonato"
    ]
    
    textos_ciencia = [
        "biologia celula organismo investigacion",
        "fisica particulas experimento laboratorio",
        "quimica moleculas reaccion elemento"
    ]
    
    # Combinar datos
    textos = textos_tecnologia + textos_deportes + textos_ciencia
    categorias = ['Tecnología']*3 + ['Deportes']*3 + ['Ciencia']*3
    
    # Vectorizar
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    
    # Crear y entrenar modelo
    modelo = ModeloAprendizajeWeb()
    
    print("\n📊 CLASIFICACIÓN SUPERVISADA")
    print("-" * 60)
    metricas = modelo.entrenar_clasificador(X, categorias, test_size=0.3)
    
    print(f"\n🎯 Precisión del modelo: {metricas['accuracy']:.2%}")
    print(f"📋 Categorías detectadas: {', '.join(metricas['categorias'])}")
    
    # Probar predicción
    texto_nuevo = ["algoritmo python aprendizaje datos"]
    X_nuevo = vectorizer.transform(texto_nuevo)
    prediccion = modelo.predecir(X_nuevo)
    print(f"\n🔮 Predicción para texto nuevo: '{texto_nuevo[0]}'")
    print(f"   Categoría predicha: {prediccion[0]}")
    
    # Clustering
    print("\n\n🎯 CLUSTERING NO SUPERVISADO")
    print("-" * 60)
    metricas_cluster = modelo.entrenar_clustering(X, n_clusters=3)
    print(f"📊 Documentos agrupados en {metricas_cluster['n_clusters']} clusters")
    print(f"   Asignaciones: {metricas_cluster['clusters']}")
    
    # Guardar modelo
    modelo.guardar_modelo('models/clasificador_ejemplo.pkl')
