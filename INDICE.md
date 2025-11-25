# 📑 ÍNDICE COMPLETO DEL PROYECTO

## Guía Rápida de Navegación

---

## 📚 DOCUMENTACIÓN PRINCIPAL

### 1️⃣ [README.md](README.md)
**¿Cuándo leer?** PRIMERO - Visión general del proyecto

**Contenido:**
- Descripción del sistema
- Características principales
- Arquitectura
- Instalación rápida
- Uso básico
- Solución de problemas

**Tiempo de lectura:** 5-10 minutos

---

### 2️⃣ [GUIA_EJECUCION.md](GUIA_EJECUCION.md)
**¿Cuándo leer?** SEGUNDO - Paso a paso práctico

**Contenido:**
- Estructura del proyecto
- Instalación detallada paso a paso
- Comandos exactos para Windows 11
- Cómo ejecutar cada módulo
- Ejemplo de flujo completo
- Preparación de enlaces públicos
- Checklist de verificación

**Tiempo de lectura:** 15-20 minutos

**🎯 USA ESTO PARA:** Seguir instrucciones paso a paso

---

### 3️⃣ [MARCO_TEORICO.md](MARCO_TEORICO.md)
**¿Cuándo leer?** Para entender la teoría detrás del código

**Contenido:**
- Fundamentos de Web Scraping
- Procesamiento de Lenguaje Natural (NLP)
- Machine Learning para texto
- Algoritmos utilizados
- Métricas de evaluación
- Arquitectura del sistema
- Aplicaciones prácticas
- Glosario de términos

**Tiempo de lectura:** 30-40 minutos

**🎯 USA ESTO PARA:** Entender los conceptos y explicarlos en el video

---

### 4️⃣ [GUION_VIDEO.md](GUION_VIDEO.md)
**¿Cuándo leer?** ANTES de grabar tu video

**Contenido:**
- Estructura del video (minuto a minuto)
- Qué decir en cada sección
- Qué mostrar en pantalla
- Checklist de preparación
- Consejos de presentación
- Software de grabación recomendado
- Proceso de subida

**Tiempo de lectura:** 20-25 minutos

**🎯 USA ESTO PARA:** Planificar y grabar tu video de 15 minutos

---

### 5️⃣ [CONSEJOS_PRACTICOS.md](CONSEJOS_PRACTICOS.md)
**¿Cuándo leer?** Antes de la presentación final

**Contenido:**
- Estrategia para maximizar tu calificación
- Frases que demuestran conocimiento
- Manejo de errores en vivo
- Optimización del video
- Respuestas a preguntas comunes
- Checklist final antes de enviar

**Tiempo de lectura:** 15-20 minutos

**🎯 USA ESTO PARA:** Pulir tu presentación y evitar errores comunes

---

## 💻 CÓDIGO FUENTE

### 📂 src/

#### 6️⃣ [src/scraping.py](src/scraping.py)
**Función:** Módulo de Web Scraping

**Clases:**
- `WebScraper`: Extrae contenido de URLs

**Funciones principales:**
- `extraer_texto_url()`: Extrae texto de una URL
- `extraer_multiples_urls()`: Procesa múltiples URLs
- `limpiar_texto()`: Limpia el HTML

**Ejemplo de uso:**
```python
scraper = WebScraper()
df = scraper.extraer_multiples_urls(['url1', 'url2'])
```

**Líneas de código:** ~150

---

#### 7️⃣ [src/preprocessing.py](src/preprocessing.py)
**Función:** Preprocesamiento y NLP

**Clases:**
- `PreprocesadorTexto`: Procesa y vectoriza texto

**Funciones principales:**
- `limpiar_texto()`: Normalización básica
- `tokenizar()`: Divide en palabras
- `eliminar_stopwords()`: Filtra palabras comunes
- `aplicar_stemming()`: Reduce a raíces
- `procesar_texto()`: Pipeline completo
- `vectorizar_textos()`: Convierte a TF-IDF

**Ejemplo de uso:**
```python
prep = PreprocesadorTexto()
texto_procesado = prep.procesar_texto(texto)
vectores = prep.vectorizar_textos(textos_lista)
```

**Líneas de código:** ~180

---

#### 8️⃣ [src/model.py](src/model.py)
**Función:** Modelos de Machine Learning

**Clases:**
- `ModeloAprendizajeWeb`: Clasificación y clustering

**Funciones principales:**
- `entrenar_clasificador()`: Entrena Naive Bayes
- `predecir()`: Hace predicciones
- `predecir_con_probabilidad()`: Predicciones + confianza
- `entrenar_clustering()`: K-Means
- `visualizar_matriz_confusion()`: Gráficos
- `guardar_modelo()` / `cargar_modelo()`: Persistencia

**Ejemplo de uso:**
```python
modelo = ModeloAprendizajeWeb()
metricas = modelo.entrenar_clasificador(X, y)
prediccion = modelo.predecir(X_nuevo)
```

**Líneas de código:** ~280

---

#### 9️⃣ [src/app.py](src/app.py)
**Función:** Aplicación Web Interactiva

**Páginas:**
- Inicio: Información general
- Extracción: Cargar/extraer datos
- Entrenamiento: Entrenar modelos
- Predicción: Clasificar nuevos textos
- Análisis: Visualizaciones

**Cómo ejecutar:**
```powershell
streamlit run src/app.py
```

**Líneas de código:** ~600+

---

### 🔟 [demo_completa.py](demo_completa.py)
**Función:** Script de demostración end-to-end

**Qué hace:**
1. Carga dataset de ejemplo (15 documentos)
2. Preprocesa los textos
3. Entrena el modelo
4. Hace predicciones de prueba
5. Realiza clustering
6. Guarda resultados

**Cómo ejecutar:**
```powershell
python demo_completa.py
```

**Duración:** ~30 segundos

**Líneas de código:** ~380

---

## 📦 ARCHIVOS DE CONFIGURACIÓN

### 1️⃣1️⃣ [requirements.txt](requirements.txt)
**Función:** Lista de dependencias del proyecto

**Contenido:**
- Bibliotecas de web scraping (requests, beautifulsoup4)
- Bibliotecas de NLP (nltk, spacy)
- Bibliotecas de ML (scikit-learn, pandas)
- Bibliotecas de visualización (matplotlib, plotly)
- Framework web (streamlit)

**Uso:**
```powershell
pip install -r requirements.txt
```

---

## 📁 ESTRUCTURA DE CARPETAS

```
proyecto_aprendizaje_web/
│
├── 📄 README.md                    [Visión general]
├── 📄 GUIA_EJECUCION.md           [Paso a paso]
├── 📄 MARCO_TEORICO.md            [Teoría]
├── 📄 GUION_VIDEO.md              [Script video]
├── 📄 CONSEJOS_PRACTICOS.md       [Tips finales]
├── 📄 INDICE.md                   [Este archivo]
├── 📄 requirements.txt            [Dependencias]
│
├── 📂 data/
│   ├── 📂 raw/                     [Datos extraídos]
│   └── 📂 processed/               [Datos procesados]
│
├── 📂 models/                      [Modelos entrenados]
│
├── 📂 src/
│   ├── 🐍 scraping.py             [Web scraping]
│   ├── 🐍 preprocessing.py        [NLP]
│   ├── 🐍 model.py                [Machine Learning]
│   └── 🐍 app.py                  [Aplicación web]
│
├── 📂 results/                     [Visualizaciones]
│
└── 🐍 demo_completa.py            [Demo end-to-end]
```

---

## 🎯 FLUJO DE TRABAJO RECOMENDADO

### Para Instalación:
```
1. README.md (visión general)
   ↓
2. GUIA_EJECUCION.md → Sección "Instalación"
   ↓
3. Ejecutar comandos paso a paso
   ↓
4. Probar demo_completa.py
```

### Para Entender el Código:
```
1. MARCO_TEORICO.md (conceptos)
   ↓
2. scraping.py (extracción)
   ↓
3. preprocessing.py (procesamiento)
   ↓
4. model.py (aprendizaje)
   ↓
5. app.py (integración)
```

### Para Preparar el Video:
```
1. GUION_VIDEO.md (estructura)
   ↓
2. CONSEJOS_PRACTICOS.md (optimización)
   ↓
3. Practicar con demo_completa.py
   ↓
4. Practicar con app.py
   ↓
5. Grabar siguiendo el guión
```

### Para Resolver Problemas:
```
1. README.md → Sección "Solución de Problemas"
   ↓
2. GUIA_EJECUCION.md → Sección "Troubleshooting"
   ↓
3. Si persiste: buscar error específico en Google
```

---

## ⏱️ TIEMPOS ESTIMADOS

| Actividad | Tiempo |
|-----------|--------|
| Leer documentación completa | 1.5-2 horas |
| Instalar y configurar | 30-45 min |
| Entender el código | 1-1.5 horas |
| Practicar demos | 30 min |
| Preparar video | 1 hora |
| Grabar video | 30-60 min |
| Editar y subir | 30 min |
| **TOTAL** | **5-7 horas** |

---

## 📊 ESTADÍSTICAS DEL PROYECTO

```
📝 Total de archivos: 12
📄 Archivos de documentación: 6
🐍 Archivos de código Python: 5
📦 Archivos de configuración: 1

📚 Total de líneas de documentación: ~3,500
💻 Total de líneas de código: ~1,590

⏱️ Tiempo de ejecución demo: ~30 seg
🎥 Duración recomendada video: 12-15 min
```

---

## 🗺️ MAPA MENTAL

```
                    PROYECTO
                       |
        +--------------+--------------+
        |              |              |
   DOCUMENTACIÓN    CÓDIGO       EJECUCIÓN
        |              |              |
   +----+----+    +----+----+    +----+----+
   |    |    |    |    |    |    |    |    |
 README GUIA MARCO SCRP PREP MOD DEMO APP TEST
         |              |
    GUION VIDEO    CONSEJOS
```

---

## ✅ CHECKLIST DE NAVEGACIÓN

Marca lo que ya revisaste:

### Documentación:
- [ ] README.md
- [ ] GUIA_EJECUCION.md
- [ ] MARCO_TEORICO.md
- [ ] GUION_VIDEO.md
- [ ] CONSEJOS_PRACTICOS.md

### Código:
- [ ] scraping.py
- [ ] preprocessing.py
- [ ] model.py
- [ ] app.py
- [ ] demo_completa.py

### Ejecución:
- [ ] Instalación completada
- [ ] demo_completa.py ejecutado exitosamente
- [ ] app.py funciona correctamente
- [ ] Video grabado
- [ ] Enlaces preparados

---

## 🚀 INICIO RÁPIDO (5 MINUTOS)

Si tienes prisa, sigue este orden:

1. **README.md** (3 min) - Entender qué hace el proyecto
2. **demo_completa.py** (1 min) - Ver funcionando
3. **app.py** (1 min) - Ejecutar interfaz web

Luego, cuando tengas más tiempo, profundiza en el resto.

---

## 🆘 AYUDA RÁPIDA

### ¿No sé por dónde empezar?
→ **README.md**

### ¿Cómo instalo todo?
→ **GUIA_EJECUCION.md**

### ¿Qué es TF-IDF / Naive Bayes / etc?
→ **MARCO_TEORICO.md**

### ¿Cómo grabo el video?
→ **GUION_VIDEO.md**

### ¿Cómo mejoro mi presentación?
→ **CONSEJOS_PRACTICOS.md**

### ¿Algo no funciona?
→ **README.md** (Solución de problemas)

### ¿Cómo uso X módulo?
→ Lee los comentarios en el archivo .py correspondiente

---

## 📞 BÚSQUEDA RÁPIDA

### Quiero buscar información sobre:

**Web Scraping:**
- Documentación: MARCO_TEORICO.md → Sección 2.1
- Código: src/scraping.py
- Ejemplo: demo_completa.py (líneas 1-50)

**Procesamiento NLP:**
- Documentación: MARCO_TEORICO.md → Sección 2.2
- Código: src/preprocessing.py
- Ejemplo: demo_completa.py (líneas 51-100)

**Machine Learning:**
- Documentación: MARCO_TEORICO.md → Sección 2.3
- Código: src/model.py
- Ejemplo: demo_completa.py (líneas 101-200)

**Aplicación Web:**
- Documentación: GUIA_EJECUCION.md → Sección "Uso"
- Código: src/app.py
- Ejecutar: `streamlit run src/app.py`

**Instalación:**
- GUIA_EJECUCION.md → Pasos 1-6
- README.md → "Instalación Rápida"

**Video:**
- GUION_VIDEO.md (estructura completa)
- CONSEJOS_PRACTICOS.md (optimización)

---

## 🎓 PARA ESTUDIAR

Si necesitas explicar conceptos específicos:

**Tokenización:**
→ MARCO_TEORICO.md → NLP → Pipeline

**TF-IDF:**
→ MARCO_TEORICO.md → Vectorización

**Naive Bayes:**
→ MARCO_TEORICO.md → Clasificación de Texto

**Métricas (Accuracy, F1, etc):**
→ MARCO_TEORICO.md → Métricas de evaluación

**Clustering:**
→ MARCO_TEORICO.md → Clustering

---

## 💡 TIPS DE NAVEGACIÓN

1. **Usa Ctrl+F** para buscar palabras clave en cada documento
2. **Lee los comentarios** en el código Python
3. **Ejecuta ejemplos** mientras lees la teoría
4. **Toma notas** de lo que no entiendes para investigar después
5. **Practica** ejecutando el código antes del video

---

## 🎯 OBJETIVOS POR ARCHIVO

| Archivo | Objetivo |
|---------|----------|
| README.md | Entender el proyecto globalmente |
| GUIA_EJECUCION.md | Poder instalar y ejecutar |
| MARCO_TEORICO.md | Comprender la teoría |
| GUION_VIDEO.md | Saber qué decir en el video |
| CONSEJOS_PRACTICOS.md | Maximizar tu calificación |
| scraping.py | Saber extraer datos web |
| preprocessing.py | Entender procesamiento NLP |
| model.py | Comprender machine learning |
| app.py | Usar la interfaz web |
| demo_completa.py | Ver ejemplo completo |

---

## 🏁 CONCLUSIÓN

Este índice es tu **mapa de navegación**. Úsalo para:
- ✅ Orientarte en el proyecto
- ✅ Encontrar información rápidamente
- ✅ Seguir un orden lógico de aprendizaje
- ✅ No perderte entre archivos

**Empieza por README.md y sigue el flujo que mejor se adapte a tu objetivo.**

---

**¡Éxito en tu proyecto! 🚀**
