# 🎓 GUÍA COMPLETA DE EJECUCIÓN DEL PROYECTO

## Aprendizaje en la Web - Proyecto Práctico

---

## 📁 ESTRUCTURA DEL PROYECTO

```
proyecto_aprendizaje_web/
│
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación
│
├── data/                     # Datos
│   ├── raw/                  # Datos crudos extraídos
│   └── processed/            # Datos procesados
│
├── models/                   # Modelos entrenados (se genera automáticamente)
│
├── src/                      # Código fuente
│   ├── scraping.py          # Módulo de extracción web
│   ├── preprocessing.py     # Módulo de preprocesamiento
│   ├── model.py             # Módulo de machine learning
│   └── app.py               # Aplicación Streamlit
│
└── results/                  # Resultados y visualizaciones (se genera automáticamente)
```

---

## 🚀 PASOS PARA EJECUTAR EL PROYECTO

### PASO 1: Preparar el Entorno

```powershell
# 1. Crear las carpetas necesarias
mkdir data\raw
mkdir data\processed
mkdir models
mkdir results

# 2. Activar el entorno virtual (si lo creaste)
venv_aprendizaje_web\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Descargar recursos de NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

---

### PASO 2: Probar Módulos Individuales

#### A) Probar el Scraper

```powershell
cd src
python scraping.py
```

**Qué hace:**
- Extrae contenido de 3 URLs de ejemplo (Wikipedia)
- Muestra el texto extraído
- Guarda los resultados en `data/raw/contenido_extraido.csv`

**Salida esperada:**
```
📥 Extrayendo contenido de: https://...
✅ Se extrajeron 3 documentos exitosamente
💾 Datos guardados en: data/raw/contenido_extraido.csv
```

---

#### B) Probar el Preprocesador

```powershell
python preprocessing.py
```

**Qué hace:**
- Toma textos de ejemplo
- Aplica tokenización, limpieza, stemming
- Vectoriza usando TF-IDF
- Muestra las palabras más importantes

**Salida esperada:**
```
📝 Texto original: La inteligencia artificial...
🔧 Texto procesado: inteligenc artifici revolucion...
🔢 Vectorizando 4 documentos...
✅ Vectorización completa: 4 documentos x 50 características
```

---

#### C) Probar el Modelo

```powershell
python model.py
```

**Qué hace:**
- Crea un dataset sintético de ejemplo
- Entrena un clasificador
- Hace predicciones
- Entrena un modelo de clustering

**Salida esperada:**
```
🤖 Entrenando clasificador...
✅ Entrenamiento completo - Precisión: 100.00%
🔮 Predicción para texto nuevo: 'algoritmo python...'
   Categoría predicha: Tecnología
```

---

### PASO 3: Ejecutar la Aplicación Web

```powershell
# Desde la raíz del proyecto:
streamlit run src/app.py
```

**Qué sucede:**
- Se abre automáticamente tu navegador
- Verás la interfaz web en `http://localhost:8501`
- Puedes interactuar con todas las funcionalidades

---

## 🎯 USO DE LA APLICACIÓN WEB

### 1. Página de Inicio
- Información general del sistema
- Explicación del flujo de trabajo

### 2. Extracción de Datos
**Opción A: URLs Individuales**
```
1. Ingresa URLs (una por línea)
2. Click en "Extraer Contenido"
3. Espera a que se procesen
4. Revisa los datos extraídos
```

**Opción B: Texto Directo**
```
1. Ingresa título y categoría
2. Escribe o pega el texto
3. Click en "Agregar Documento"
4. Repite para agregar más documentos
```

**Opción C: Dataset de Ejemplo** (RECOMENDADO PARA EMPEZAR)
```
1. Click en "Cargar Dataset de Ejemplo"
2. Se cargan 9 documentos pre-clasificados
3. Listo para entrenar el modelo
```

### 3. Entrenamiento
```
1. Click en "Procesar Textos"
   → Limpia y vectoriza los textos
   
2. Ajusta el slider de "datos para prueba" (recomendado: 20%)

3. Click en "Entrenar Modelo"
   → Entrena el clasificador
   → Muestra métricas de precisión
```

### 4. Predicción
```
1. Escribe un texto nuevo en el área de texto
2. Click en "Predecir Categoría"
3. Ve la categoría predicha y las probabilidades
```

**Ejemplo de texto para probar:**
```
Los algoritmos de machine learning están revolucionando 
la forma en que procesamos datos en Python.
```

### 5. Análisis
- Visualiza estadísticas de tus datos
- Gráficos de distribución
- Métricas del modelo entrenado

---

## 📊 EJEMPLO DE FLUJO COMPLETO

### DEMOSTRACIÓN PASO A PASO:

```
PASO 1: Extracción de Datos
└─> Ir a "Extracción de Datos"
└─> Seleccionar "Dataset de ejemplo"
└─> Click en "Cargar Dataset de Ejemplo"
└─> Resultado: 9 documentos cargados (3 de cada categoría)

PASO 2: Entrenamiento
└─> Ir a "Entrenamiento"
└─> Click en "Procesar Textos"
    └─> Esperar procesamiento (~10 segundos)
└─> Click en "Entrenar Modelo"
    └─> Esperar entrenamiento (~5 segundos)
└─> Resultado: Modelo entrenado con ~67-100% de precisión

PASO 3: Predicción
└─> Ir a "Predicción"
└─> Ingresar texto de prueba:
    "El nuevo algoritmo de deep learning mejora 
     el reconocimiento de imágenes"
└─> Click en "Predecir Categoría"
└─> Resultado: Categoría = "Tecnología" (alta probabilidad)

PASO 4: Análisis
└─> Ir a "Análisis"
└─> Ver gráficos de:
    • Distribución de documentos
    • Longitud de textos
    • Métricas del modelo
```

---

## 🎥 PREPARACIÓN PARA EL VIDEO

### Contenido Sugerido para tu Video (15 min max):

**Minuto 0-2: Introducción**
- ¿Qué es el aprendizaje en la web?
- Objetivo del proyecto

**Minuto 2-4: Explicación del Flujo**
- Mostrar el diagrama del flujo
- Explicar cada etapa brevemente

**Minuto 4-7: Demostración de Código**
- Mostrar `scraping.py` (1 min)
- Mostrar `preprocessing.py` (1 min)
- Mostrar `model.py` (1 min)

**Minuto 7-13: Demostración de la App Web**
- Ejecutar `streamlit run src/app.py`
- Mostrar el flujo completo:
  * Cargar datos
  * Entrenar modelo
  * Hacer predicción
  * Ver análisis

**Minuto 13-15: Conclusiones**
- Resultados obtenidos
- Aplicaciones prácticas
- Posibles mejoras

---

## 🔧 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "ModuleNotFoundError: No module named 'xxx'"
```powershell
pip install xxx
```

### Error: "NLTK data not found"
```python
python -c "import nltk; nltk.download('all')"
```

### Error: "Cannot connect to URL"
```
- Verifica tu conexión a internet
- Algunas URLs pueden bloquear scrapers
- Usa el dataset de ejemplo como alternativa
```

### La app Streamlit no se abre
```powershell
# Verifica que Streamlit esté instalado
pip show streamlit

# Si no está instalado:
pip install streamlit

# Ejecuta con el path completo:
python -m streamlit run src/app.py
```

---

## 📝 CHECKLIST ANTES DE PRESENTAR

- [ ] Todas las dependencias instaladas
- [ ] Módulos individuales funcionan correctamente
- [ ] La aplicación Streamlit se ejecuta sin errores
- [ ] Puedes cargar el dataset de ejemplo
- [ ] Puedes entrenar el modelo
- [ ] Puedes hacer predicciones
- [ ] Los gráficos se visualizan correctamente
- [ ] Video grabado (máx 15 minutos)
- [ ] Enlaces públicos preparados

---

## 🌐 PREPARAR ENLACES PÚBLICOS

### Para el Código (GitHub):
1. Crear repositorio en GitHub
2. Subir todos los archivos del proyecto
3. Asegurarte de que sea público
4. Copiar el enlace

### Para el Video:
1. Subir a YouTube (sin listar o público)
2. O subir a Google Drive (permisos: cualquiera con el enlace)
3. Copiar el enlace

---

## 💡 CONSEJOS PARA LA PRESENTACIÓN

1. **Practica el flujo completo** antes de grabar
2. **Prepara ejemplos de texto** interesantes para clasificar
3. **Explica el "porqué"** de cada paso, no solo el "cómo"
4. **Usa terminología técnica** correctamente
5. **Muestra resultados reales** de tu modelo
6. **Menciona posibles mejoras** o extensiones

---

## 🎯 APLICACIONES PRÁCTICAS A MENCIONAR

- Clasificación automática de noticias
- Análisis de sentimientos en redes sociales
- Detección de spam en correos
- Agrupamiento de documentos similares
- Recomendación de contenido
- Monitoreo de menciones de marca

---

## 📚 RECURSOS ADICIONALES

- Documentación NLTK: https://www.nltk.org/
- Scikit-learn: https://scikit-learn.org/
- Streamlit: https://docs.streamlit.io/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/

---

**¡Buena suerte con tu presentación! 🚀**
