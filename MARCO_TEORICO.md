# 📚 MARCO TEÓRICO - APRENDIZAJE EN LA WEB

## 1. INTRODUCCIÓN

### ¿Qué es el Aprendizaje en la Web?

El **Aprendizaje en la Web** (Web Learning) es una rama del Machine Learning que se enfoca en extraer, procesar y aprender de datos disponibles en internet. Combina técnicas de:

- **Web Scraping**: Extracción automatizada de contenido web
- **Procesamiento de Lenguaje Natural (NLP)**: Análisis y comprensión de texto
- **Machine Learning**: Aprendizaje de patrones y predicción
- **Minería de Datos**: Descubrimiento de conocimiento en grandes volúmenes de información

---

## 2. COMPONENTES FUNDAMENTALES

### 2.1 Web Scraping

**Definición**: Proceso automatizado de extracción de información de sitios web.

**Técnicas principales:**
- **Parsing HTML**: Análisis de estructura DOM (Document Object Model)
- **Selectores CSS**: Identificación de elementos específicos
- **XPath**: Navegación en documentos XML/HTML
- **APIs Web**: Acceso estructurado a datos

**Herramientas en Python:**
```
• BeautifulSoup: Parsing HTML/XML
• Scrapy: Framework completo de scraping
• Selenium: Scraping de páginas dinámicas (JavaScript)
• Requests: Peticiones HTTP
```

**Consideraciones éticas:**
- Respetar el archivo `robots.txt`
- No sobrecargar servidores (rate limiting)
- Cumplir con términos de servicio
- Respetar derechos de autor

---

### 2.2 Procesamiento de Lenguaje Natural (NLP)

**Definición**: Campo de la IA que permite a las computadoras entender, interpretar y generar lenguaje humano.

#### Pipeline típico de NLP:

**1. Tokenización**
```
Texto: "Python es genial"
Tokens: ["Python", "es", "genial"]
```

**2. Normalización**
- Convertir a minúsculas
- Eliminar puntuación
- Eliminar caracteres especiales

**3. Stopwords Removal**
```
Texto: ["el", "python", "es", "un", "lenguaje"]
Filtrado: ["python", "lenguaje"]
```
*Elimina palabras comunes sin valor semántico*

**4. Stemming / Lemmatization**
```
Stemming: "corriendo" → "corr"
Lemmatization: "corriendo" → "correr"
```

**5. Vectorización**
Convertir texto en números que las máquinas pueden procesar.

**Técnicas de vectorización:**

a) **Bag of Words (BoW)**
```
Documento 1: "me gusta python"
Documento 2: "python es genial"

Vocabulario: [me, gusta, python, es, genial]

Vector 1: [1, 1, 1, 0, 0]
Vector 2: [0, 0, 1, 1, 1]
```

b) **TF-IDF (Term Frequency - Inverse Document Frequency)**
```
TF-IDF = TF × IDF

TF (Term Frequency): 
   Frecuencia de término en el documento

IDF (Inverse Document Frequency): 
   log(Total documentos / Documentos con el término)

Ventaja: Palabras comunes tienen menor peso
```

c) **Word Embeddings**
- Word2Vec
- GloVe
- FastText
- Transformers (BERT, GPT)

---

### 2.3 Machine Learning para Texto

#### Clasificación de Texto

**Definición**: Asignar categorías predefinidas a documentos.

**Algoritmos comunes:**

1. **Naive Bayes**
   - Basado en probabilidad bayesiana
   - Rápido y eficiente
   - Funciona bien con datasets pequeños
   - Asume independencia entre características

   ```
   P(Categoría|Texto) = P(Texto|Categoría) × P(Categoría) / P(Texto)
   ```

2. **Support Vector Machines (SVM)**
   - Encuentra el hiperplano que mejor separa las clases
   - Efectivo en espacios de alta dimensión
   - Robusto contra overfitting

3. **Random Forest**
   - Conjunto de árboles de decisión
   - Reduce overfitting
   - Maneja características no lineales

4. **Redes Neuronales**
   - Deep Learning para texto
   - LSTM, GRU para secuencias
   - Transformers para tareas complejas

**Métricas de evaluación:**

- **Accuracy (Precisión)**: 
  ```
  (Predicciones correctas) / (Total predicciones)
  ```

- **Precision**: 
  ```
  Verdaderos positivos / (Verdaderos positivos + Falsos positivos)
  ```

- **Recall (Sensibilidad)**: 
  ```
  Verdaderos positivos / (Verdaderos positivos + Falsos negativos)
  ```

- **F1-Score**: 
  ```
  2 × (Precision × Recall) / (Precision + Recall)
  ```

#### Clustering (Agrupamiento)

**Definición**: Agrupar documentos similares sin etiquetas previas (aprendizaje no supervisado).

**Algoritmos:**

1. **K-Means**
   - Define K clusters
   - Asigna documentos al centroide más cercano
   - Itera hasta convergencia

2. **DBSCAN**
   - Agrupa por densidad
   - Detecta outliers automáticamente

3. **Clustering Jerárquico**
   - Crea dendrogramas
   - Agrupa progresivamente

**Métricas de clustering:**

- **Silhouette Score**: 
  - Rango: [-1, 1]
  - Valores cercanos a 1 = buen agrupamiento
  - Valores negativos = mala asignación

---

## 3. ARQUITECTURA DEL SISTEMA

```
┌─────────────────────────────────────────────────────────┐
│                    ENTRADA DE DATOS                      │
│  • URLs de sitios web                                    │
│  • Texto directo                                         │
│  • Archivos (CSV, TXT, JSON)                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              1. WEB SCRAPING / RECOLECCIÓN              │
│  • Requests HTTP                                         │
│  • Parsing HTML (BeautifulSoup)                         │
│  • Extracción de texto relevante                        │
│  • Limpieza básica                                      │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              2. PREPROCESAMIENTO (NLP)                   │
│  • Tokenización                                          │
│  • Normalización (lowercase, sin puntuación)            │
│  • Eliminación de stopwords                             │
│  • Stemming / Lemmatization                             │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              3. VECTORIZACIÓN                            │
│  • TF-IDF Vectorizer                                     │
│  • Bag of Words                                          │
│  • Word Embeddings (opcional)                           │
│  Salida: Matriz de características numéricas            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              4. ENTRENAMIENTO DEL MODELO                 │
│                                                          │
│  OPCIÓN A: Clasificación Supervisada                    │
│  • Naive Bayes / SVM / Random Forest                    │
│  • Train/Test Split                                      │
│  • Evaluación con métricas                              │
│                                                          │
│  OPCIÓN B: Clustering No Supervisado                    │
│  • K-Means / DBSCAN                                      │
│  • Agrupamiento automático                              │
│  • Análisis de clusters                                 │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              5. PREDICCIÓN / INFERENCIA                  │
│  • Texto nuevo → Preprocesar                            │
│  • Vectorizar                                            │
│  • Aplicar modelo entrenado                             │
│  • Obtener categoría/cluster                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              6. VISUALIZACIÓN Y ANÁLISIS                 │
│  • Métricas de rendimiento                              │
│  • Gráficos de distribución                             │
│  • Matriz de confusión                                  │
│  • Palabras más relevantes                              │
└─────────────────────────────────────────────────────────┘
```

---

## 4. APLICACIONES PRÁCTICAS

### 4.1 Clasificación Automática de Contenido
- Categorización de noticias por tema
- Filtrado de spam en correos
- Clasificación de tickets de soporte

### 4.2 Análisis de Sentimientos
- Opiniones en redes sociales
- Reviews de productos
- Monitoreo de marca

### 4.3 Recomendación de Contenido
- Sugerencias de artículos similares
- Sistemas de recomendación
- Búsqueda semántica

### 4.4 Detección de Temas
- Identificar tendencias en redes
- Análisis de tópicos (Topic Modeling)
- Vigilancia de información

### 4.5 Extracción de Información
- Obtener datos estructurados de texto
- Named Entity Recognition (NER)
- Resumen automático de documentos

---

## 5. DESAFÍOS Y CONSIDERACIONES

### 5.1 Desafíos Técnicos
- **Escalabilidad**: Procesar grandes volúmenes de datos
- **Ruido en datos web**: HTML mal formado, publicidad
- **Ambigüedad del lenguaje**: Sarcasmo, ironía, contexto
- **Multilingüismo**: Soporte para múltiples idiomas
- **Datos desbalanceados**: Categorías con pocos ejemplos

### 5.2 Desafíos Éticos
- Privacidad de datos
- Sesgos en modelos de ML
- Derechos de autor del contenido
- Uso responsable de información

### 5.3 Mejores Prácticas
- Validación cruzada (k-fold cross-validation)
- Regularización para evitar overfitting
- Monitoreo continuo del modelo
- Reentrenamiento periódico
- Documentación exhaustiva

---

## 6. TENDENCIAS ACTUALES

### 6.1 Transfer Learning
- Usar modelos preentrenados (BERT, GPT)
- Fine-tuning para tareas específicas
- Menor necesidad de datos

### 6.2 Few-Shot Learning
- Aprender con pocos ejemplos
- Meta-learning
- Prompt engineering

### 6.3 Multimodalidad
- Combinar texto, imágenes, audio
- Modelos como CLIP, DALL-E
- Comprensión holística del contenido

### 6.4 Explicabilidad (XAI)
- Entender decisiones del modelo
- LIME, SHAP para interpretabilidad
- Confianza en predicciones

---

## 7. HERRAMIENTAS Y FRAMEWORKS

### Python Libraries:
- **Web Scraping**: BeautifulSoup, Scrapy, Selenium
- **NLP**: NLTK, spaCy, TextBlob
- **Machine Learning**: scikit-learn, XGBoost
- **Deep Learning**: TensorFlow, PyTorch, Keras
- **Visualización**: Matplotlib, Seaborn, Plotly
- **Web Apps**: Streamlit, Flask, FastAPI

### Cloud Services:
- **AWS**: SageMaker, Comprehend
- **Google Cloud**: Natural Language API, AutoML
- **Azure**: Cognitive Services

---

## 8. MÉTRICAS DE ÉXITO

Para evaluar un sistema de aprendizaje web:

1. **Precisión del modelo** (>85% es bueno)
2. **Velocidad de procesamiento** (documentos/segundo)
3. **Escalabilidad** (capacidad de crecer)
4. **Facilidad de uso** (interfaz intuitiva)
5. **Interpretabilidad** (entender predicciones)
6. **Robustez** (manejar datos ruidosos)

---

## 9. CONCLUSIÓN

El aprendizaje en la web es un campo interdisciplinario que combina:
- Ingeniería de software
- Ciencia de datos
- Lingüística computacional
- Estadística y matemáticas

**Ventajas:**
- Acceso a grandes volúmenes de datos
- Automatización de tareas repetitivas
- Descubrimiento de patrones ocultos
- Escalabilidad

**Limitaciones:**
- Dependencia de la calidad de datos
- Necesidad de etiquetado (aprendizaje supervisado)
- Mantenimiento continuo
- Consideraciones éticas

---

## 10. REFERENCIAS Y RECURSOS

### Libros:
- "Speech and Language Processing" - Jurafsky & Martin
- "Introduction to Information Retrieval" - Manning et al.
- "Python Machine Learning" - Sebastian Raschka

### Cursos Online:
- Coursera: Natural Language Processing Specialization
- Fast.ai: Practical Deep Learning
- DataCamp: NLP in Python

### Papers Importantes:
- "Attention Is All You Need" (Transformers)
- "BERT: Pre-training of Deep Bidirectional Transformers"
- "Efficient Estimation of Word Representations" (Word2Vec)

---

**Última actualización:** Noviembre 2024

---

## GLOSARIO DE TÉRMINOS

- **Corpus**: Colección de documentos de texto
- **Token**: Unidad mínima de texto (palabra, carácter)
- **Feature**: Característica extraída del texto
- **Label**: Etiqueta o categoría de clasificación
- **Training Set**: Conjunto de datos para entrenar
- **Test Set**: Conjunto de datos para evaluar
- **Overfitting**: Modelo aprende ruido del training
- **Underfitting**: Modelo demasiado simple
- **Hyperparameter**: Parámetro que se ajusta antes del entrenamiento
- **Pipeline**: Secuencia de pasos de procesamiento
