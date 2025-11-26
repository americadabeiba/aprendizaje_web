# 🌐 Sistema de Aprendizaje en la Web

## Proyecto Académico - Machine Learning + NLP + Web Scraping

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)

---

## 📋 Descripción

Sistema completo que combina **Web Scraping**, **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning** para extraer, procesar y aprender automáticamente de contenido web.

### Características principales:

✅ **Extracción web automatizada** - Web scraping de múltiples URLs  
✅ **Procesamiento NLP avanzado** - Tokenización, limpieza, vectorización  
✅ **Clasificación supervisada** - Categorización automática de textos  
✅ **Clustering no supervisado** - Agrupamiento de documentos similares  
✅ **Aplicación web interactiva** - Interfaz Streamlit fácil de usar  
✅ **Visualizaciones dinámicas** - Gráficos y métricas en tiempo real  

---

## 🎯 Aplicaciones Prácticas

- 📰 Clasificación automática de noticias
- 💬 Análisis de sentimientos en redes sociales
- 🚫 Detección de spam en correos electrónicos
- 🔍 Sistemas de recomendación de contenido
- 📊 Análisis de tendencias web
- 🏷️ Etiquetado automático de documentos

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────┐
│ Web Scraping│ --> │Preprocesamiento│ --> │Vectorización│ --> │Modelo ML │
│(BeautifulSoup)│     │    (NLP)     │     │   (TF-IDF)  │     │(Naive Bayes)│
└─────────────┘     └──────────────┘     └─────────────┘     └──────────┘
                                                                      │
                                                                      ▼
                                                              ┌───────────────┐
                                                              │  Predicción   │
                                                              │& Visualización│
                                                              │  (Streamlit)  │
                                                              └───────────────┘
```

---

## 📁 Estructura del Proyecto

```
proyecto_aprendizaje_web/
│
├── 📄 requirements.txt           # Dependencias del proyecto
├── 📄 README.md                  # Este archivo
├── 📄 GUIA_EJECUCION.md         # Guía detallada paso a paso
├── 📄 MARCO_TEORICO.md          # Fundamentos teóricos
├── 📄 GUION_VIDEO.md            # Guión para video de presentación
│
├── 📂 data/                      # Datos del proyecto
│   ├── 📂 raw/                   # Datos crudos extraídos
│   └── 📂 processed/             # Datos procesados
│
├── 📂 models/                    # Modelos entrenados guardados
│
├── 📂 src/                       # Código fuente
│   ├── 🐍 scraping.py           # Módulo de web scraping
│   ├── 🐍 preprocessing.py      # Módulo de preprocesamiento NLP
│   ├── 🐍 model.py              # Módulo de machine learning
│   └── 🐍 app.py                # Aplicación web Streamlit
│
├── 📂 results/                   # Resultados y visualizaciones
│
└── 🐍 demo_completa.py          # Script de demostración end-to-end
```

---

## 🚀 Instalación Rápida

### 1. Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Windows 11 / macOS / Linux

### 2. Clonar o Descargar el Proyecto
```bash
# Si usas Git:
git clone [URL_DEL_REPOSITORIO]
cd proyecto_aprendizaje_web

# Si descargaste un ZIP:
# Descomprime y navega a la carpeta
```

### 3. Crear Entorno Virtual (Recomendado)
```powershell
# Windows
python -m venv venv_aprendizaje_web
venv_aprendizaje_web\Scripts\activate

# macOS/Linux
python3 -m venv venv_aprendizaje_web
source venv_aprendizaje_web/bin/activate
```

### 4. Instalar Dependencias
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Descargar Recursos de NLTK
```powershell
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### 6. Crear Carpetas Necesarias
```powershell
mkdir data\raw
mkdir data\processed
mkdir models
mkdir results
```

---

## 💻 Uso del Sistema

### Opción 1: Demostración Completa (Recomendado para empezar)

```powershell
python demo_completa.py
```

Este script ejecuta automáticamente:
- ✅ Carga de datos de ejemplo
- ✅ Preprocesamiento completo
- ✅ Entrenamiento del modelo
- ✅ Predicciones de prueba
- ✅ Métricas y resultados

**Duración:** ~30 segundos

---

### Opción 2: Aplicación Web Interactiva

```powershell
streamlit run src/app.py
```

Se abrirá automáticamente en tu navegador: `http://localhost:8501`

#### Funcionalidades de la App:

**1. 🏠 Inicio**
- Información del sistema
- Explicación del flujo

**2. 📥 Extracción de Datos**
- Extraer contenido de URLs
- Ingresar texto manualmente
- Cargar dataset de ejemplo

**3. 🤖 Entrenamiento**
- Preprocesar textos
- Entrenar modelo de clasificación
- Ver métricas de rendimiento

**4. 🔮 Predicción**
- Clasificar nuevos textos
- Ver probabilidades por categoría
- Análisis de confianza

**5. 📊 Análisis**
- Estadísticas generales
- Visualizaciones interactivas
- Métricas del modelo

---

### Opción 3: Usar Módulos Individuales

```python
# Ejemplo: Clasificar un texto

from src.preprocessing import PreprocesadorTexto
from src.model import ModeloAprendizajeWeb
import joblib

# Cargar modelo entrenado
modelo = ModeloAprendizajeWeb()
modelo.cargar_modelo('models/clasificador_final.pkl')

# Preprocesar texto nuevo
prep = PreprocesadorTexto()
texto = "Los algoritmos de machine learning están revolucionando la tecnología"
texto_procesado = prep.procesar_texto(texto)

# Vectorizar
vector = prep.vectorizer.transform([texto_procesado])

# Predecir
prediccion = modelo.predecir(vector)
print(f"Categoría: {prediccion[0]}")
```

---

## 📊 Dataset de Ejemplo

El proyecto incluye un dataset sintético con:
- **15 documentos** de texto
- **3 categorías**: Tecnología, Deportes, Ciencia
- **5 documentos por categoría** (balanceado)

Ideal para:
- Aprender el funcionamiento del sistema
- Probar rápidamente
- Entender el flujo de trabajo

---

## 🎓 Fundamentos Teóricos

### Tecnologías Utilizadas:

#### 1. Web Scraping
- **BeautifulSoup**: Parsing de HTML
- **Requests**: Peticiones HTTP
- **lxml**: Parser rápido

#### 2. Procesamiento NLP
- **NLTK**: Tokenización, stopwords, stemming
- **TF-IDF**: Vectorización de texto
- **Regex**: Limpieza de texto

#### 3. Machine Learning
- **Naive Bayes**: Clasificación probabilística
- **K-Means**: Clustering no supervisado
- **scikit-learn**: Framework de ML

#### 4. Visualización y UI
- **Streamlit**: Aplicación web
- **Plotly**: Gráficos interactivos
- **Pandas**: Manipulación de datos

---

## 📈 Métricas de Rendimiento

El sistema evalúa el modelo usando:

- **Accuracy (Precisión)**: % de predicciones correctas
- **Precision**: Precisión por categoría
- **Recall**: Cobertura por categoría
- **F1-Score**: Media armónica de precision y recall
- **Matriz de Confusión**: Visualización de errores

### Resultados Típicos (Dataset de ejemplo):
```
✅ Accuracy:  85-100%
✅ F1-Score:  0.85-1.00
✅ Tiempo de entrenamiento: <5 segundos
✅ Tiempo de predicción: <1 segundo
```

---

## 🔧 Personalización

### Agregar Nuevas Categorías:

1. Recolecta documentos de la nueva categoría
2. Etiquétalos correctamente
3. Agrégalos al dataset
4. Reentrena el modelo

### Usar tus Propias URLs:

```python
from src.scraping import WebScraper

scraper = WebScraper()
urls = [
    "https://tu-sitio-1.com",
    "https://tu-sitio-2.com"
]
df = scraper.extraer_multiples_urls(urls)
```

### Ajustar Hiperparámetros:

En `preprocessing.py`:
```python
vectorizer = TfidfVectorizer(
    max_features=1000,  # Cambiar número de características
    ngram_range=(1, 2),  # Usar unigramas y bigramas
    min_df=2             # Frecuencia mínima
)
```

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```powershell
pip install nombre_del_modulo
```

### Error: "NLTK data not found"
```python
import nltk
nltk.download('all')
```

### La aplicación Streamlit no se abre
```powershell
# Verifica la instalación
pip show streamlit

# Ejecuta con python -m
python -m streamlit run src/app.py
```

### Problemas con codificación de caracteres
```python
# En Python, usa siempre:
open('archivo.txt', 'r', encoding='utf-8')
```

---

## 📚 Documentación Adicional

- 📖 [GUIA_EJECUCION.md](GUIA_EJECUCION.md) - Instrucciones detalladas paso a paso
- 📖 [MARCO_TEORICO.md](MARCO_TEORICO.md) - Fundamentos teóricos completos
- 📖 [GUION_VIDEO.md](GUION_VIDEO.md) - Guía para grabar video de presentación

---

## 🎥 Video de Demostración

[Enlace al video aquí]

---

## 👨‍💻 Autor

[Tu Nombre]  
[Tu Email]  
[LinkedIn/GitHub] (opcional)

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.

---

## 🙏 Agradecimientos

- Comunidad de Python y bibliotecas open source
- Documentación de scikit-learn, NLTK, Streamlit
- Recursos educativos de Machine Learning y NLP

---

## 🔮 Mejoras Futuras

Posibles extensiones del proyecto:

- [ ] Soporte para múltiples idiomas
- [ ] Integración con APIs de noticias (NewsAPI)
- [ ] Análisis de sentimientos
- [ ] Exportación a PDF/Excel
- [ ] Dashboard con métricas en tiempo real
- [ ] Modelo de deep learning (LSTM, BERT)
- [ ] Despliegue en la nube (Heroku, AWS)
- [ ] Base de datos para almacenar histórico
- [ ] Sistema de alertas automáticas
- [ ] API REST para integración

---

## 📞 Contacto y Soporte

Si tienes preguntas o sugerencias:
- Abre un issue en GitHub
- Envía un email a [tu-email]
- Conecta en [LinkedIn/otra red]

---

## ⭐ Si te gustó este proyecto

- Dale una estrella ⭐ en GitHub
- Compártelo con tus compañeros
- Contribuye con mejoras
- Úsalo como base para tus propios proyectos

---

**Desarrollado con ❤️ y ☕ para el aprendizaje automático**

---

## 📊 Estadísticas del Proyecto

```
📝 Líneas de código: ~1500
🐍 Módulos Python: 4
📦 Dependencias: 15+
⏱️ Tiempo de desarrollo: [X días/semanas]
🧪 Tests realizados: Múltiples
```

---

## 🎯 Objetivos Cumplidos

- [x] ✅ Implementar web scraping funcional
- [x] ✅ Aplicar técnicas de NLP
- [x] ✅ Entrenar modelo de ML con buena precisión
- [x] ✅ Crear aplicación web interactiva
- [x] ✅ Documentación completa
- [x] ✅ Scripts de demostración
- [x] ✅ Visualizaciones de resultados

---

**¡Gracias por usar este proyecto! 🚀**

_Última actualización: Noviembre 2024_