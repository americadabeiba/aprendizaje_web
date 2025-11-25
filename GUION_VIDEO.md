# 🎥 GUIÓN PARA VIDEO - APRENDIZAJE EN LA WEB

## DURACIÓN TOTAL: 15 MINUTOS MAX

---

## 📌 ESTRUCTURA DEL VIDEO

```
┌──────────────────────────────────────────────────────┐
│ INTRO (2 min) → TEORÍA (3 min) → DEMO (9 min) → CIERRE (1 min) │
└──────────────────────────────────────────────────────┘
```

---

## 🎬 MINUTO 0-2: INTRODUCCIÓN

### PANTALLA: Título del proyecto

**DECIR:**
> "Hola, bienvenidos. En este video voy a presentar mi proyecto sobre **Aprendizaje en la Web**, 
> que combina técnicas de web scraping, procesamiento de lenguaje natural y machine learning 
> para extraer y aprender automáticamente de contenido web."

### PANTALLA: Diagrama de flujo simple

**DECIR:**
> "El sistema funciona en 4 etapas principales:
> 1. Extracción de contenido web mediante web scraping
> 2. Preprocesamiento del texto usando NLP
> 3. Entrenamiento de modelos de machine learning
> 4. Predicción y análisis de nuevos textos"

### PANTALLA: Aplicaciones prácticas

**DECIR:**
> "Este tipo de sistemas tiene aplicaciones muy útiles como: clasificación automática de noticias, 
> análisis de opiniones en redes sociales, detección de spam, y sistemas de recomendación de contenido."

---

## 📚 MINUTO 2-5: EXPLICACIÓN TEÓRICA

### PANTALLA: Código de scraping.py

**DECIR:**
> "Comencemos con el **web scraping**. Este módulo utiliza la biblioteca BeautifulSoup para 
> extraer contenido de páginas web. La función `extraer_texto_url` recibe una URL, 
> descarga el HTML, extrae el texto de los párrafos, y lo limpia eliminando caracteres extraños."

**MOSTRAR:**
- Resaltar la función `extraer_texto_url`
- Mostrar el método `limpiar_texto`

### PANTALLA: Código de preprocessing.py

**DECIR:**
> "El segundo paso es el **preprocesamiento**. Aquí aplicamos varias técnicas de NLP:
> - Tokenización: dividimos el texto en palabras
> - Eliminamos stopwords: palabras comunes sin valor semántico como 'el', 'la', 'de'
> - Aplicamos stemming: reducimos las palabras a su raíz
> - Vectorizamos: convertimos el texto en números usando TF-IDF"

**MOSTRAR:**
- La clase `PreprocesadorTexto`
- El método `procesar_texto` paso a paso
- Ejemplo de texto antes y después

### PANTALLA: Código de model.py

**DECIR:**
> "El tercer componente es el **modelo de machine learning**. Utilizamos Naive Bayes para 
> clasificación supervisada, que es rápido y funciona bien con texto. El modelo aprende 
> de documentos etiquetados y luego puede predecir la categoría de textos nuevos."

**MOSTRAR:**
- La función `entrenar_clasificador`
- Las métricas de evaluación (accuracy, precision, recall)

---

## 💻 MINUTO 5-14: DEMOSTRACIÓN PRÁCTICA

### PREPARACIÓN (HACER ANTES DE GRABAR):
```powershell
# Tener todo listo:
1. Entorno virtual activado
2. Terminal abierta en la carpeta del proyecto
3. Navegador listo para localhost:8501
4. Textos de ejemplo preparados para copiar/pegar
```

### PANTALLA: Terminal

**DECIR:**
> "Ahora voy a demostrar el sistema en funcionamiento. Primero, voy a ejecutar 
> un script de demostración completo que muestra todo el pipeline."

**EJECUTAR:**
```powershell
python demo_completa.py
```

**MIENTRAS SE EJECUTA, COMENTAR:**
> "Como pueden ver, el script está:
> - Cargando un dataset de ejemplo con 15 documentos de 3 categorías
> - Procesando los textos mediante tokenización y limpieza
> - Vectorizando usando TF-IDF
> - Entrenando el clasificador
> - Y haciendo predicciones en textos nuevos"

**RESALTAR:**
- La precisión del modelo (accuracy)
- Las predicciones correctas
- Las métricas por categoría

### PANTALLA: Terminal + Navegador

**DECIR:**
> "Ahora voy a mostrar la aplicación web interactiva que desarrollé con Streamlit."

**EJECUTAR:**
```powershell
streamlit run src/app.py
```

**ESPERAR A QUE SE ABRA EL NAVEGADOR**

### PANTALLA: Navegador - Página Inicio

**DECIR:**
> "Esta es la interfaz de usuario. Como pueden ver, tenemos un menú lateral para navegar 
> entre las diferentes secciones del sistema. La página de inicio explica el funcionamiento 
> general y el flujo de datos."

**NAVEGAR:** Por cada sección brevemente

### PANTALLA: Navegador - Extracción de Datos

**DECIR:**
> "En la sección de extracción de datos, voy a cargar el dataset de ejemplo 
> que viene preconfigurado con artículos de Tecnología, Deportes y Ciencia."

**HACER:**
1. Click en "Dataset de ejemplo"
2. Click en "Cargar Dataset de Ejemplo"
3. Mostrar la tabla de datos
4. Mostrar las métricas (documentos, palabras, etc.)
5. Mostrar el gráfico de distribución

**DECIR:**
> "Perfecto, aquí vemos 9 documentos cargados, 3 de cada categoría. 
> El gráfico muestra que están balanceados, lo cual es ideal para el entrenamiento."

### PANTALLA: Navegador - Entrenamiento

**DECIR:**
> "Ahora vamos a entrenar el modelo con estos datos."

**HACER:**
1. Click en "Procesar Textos"
2. Esperar a que termine
3. Mostrar ejemplo de texto procesado
4. Click en "Entrenar Modelo"
5. Esperar a que termine

**DECIR:**
> "El preprocesamiento ha convertido el texto a su forma normalizada, 
> eliminando stopwords y aplicando stemming. Ahora voy a entrenar el modelo...
> Excelente, hemos obtenido una precisión del [X]%. Las métricas por categoría 
> muestran que el modelo está aprendiendo bien cada clase."

**RESALTAR:**
- La precisión general
- El F1-Score
- El reporte detallado por categoría

### PANTALLA: Navegador - Predicción

**DECIR:**
> "Ahora lo más interesante: vamos a probar el modelo con textos completamente nuevos."

**TEXTO 1 (TECNOLOGÍA):**
```
Los algoritmos de deep learning están revolucionando el procesamiento 
de imágenes médicas mediante redes neuronales convolucionales avanzadas
```

**HACER:**
1. Pegar el texto
2. Click en "Predecir Categoría"
3. Mostrar resultado y probabilidades

**DECIR:**
> "Como pueden ver, el modelo ha clasificado correctamente este texto como Tecnología 
> con una probabilidad muy alta. El gráfico muestra la distribución de probabilidades 
> para cada categoría."

**TEXTO 2 (DEPORTES):**
```
El equipo de basketball ganó el campeonato después de un partido emocionante 
con canastas espectaculares en el último minuto
```

**HACER:**
1. Pegar el texto
2. Click en "Predecir Categoría"
3. Mostrar resultado

**DECIR:**
> "Perfecto, otra predicción correcta. El modelo identifica claramente 
> el contenido deportivo."

**TEXTO 3 (CIENCIA):**
```
Los científicos han descubierto un nuevo exoplaneta en la zona habitable 
de su estrella utilizando telescopios espaciales de última generación
```

**HACER:**
1. Pegar el texto
2. Click en "Predecir Categoría"
3. Mostrar resultado

**DECIR:**
> "Excelente, tres de tres predicciones correctas. El modelo está funcionando 
> muy bien para clasificar contenido nuevo."

### PANTALLA: Navegador - Análisis

**DECIR:**
> "Por último, la sección de análisis nos muestra estadísticas y visualizaciones 
> de nuestros datos y del rendimiento del modelo."

**MOSTRAR:**
1. Métricas generales
2. Gráfico de distribución de longitudes
3. Gráfico de distribución por categoría
4. Métricas del modelo por categoría

**DECIR:**
> "Aquí podemos ver todas las métricas importantes: distribución de documentos, 
> longitud promedio de textos, y el rendimiento del modelo para cada categoría."

---

## 🎯 MINUTO 14-15: CONCLUSIÓN Y CIERRE

### PANTALLA: Resumen visual o volver a inicio

**DECIR:**
> "Para concluir, he desarrollado un sistema completo de aprendizaje en la web que:
> 
> 1. ✅ Extrae contenido de internet usando web scraping
> 2. ✅ Procesa el texto con técnicas de NLP
> 3. ✅ Entrena modelos de machine learning para clasificación
> 4. ✅ Predice categorías de nuevos textos con alta precisión
> 5. ✅ Presenta todo en una aplicación web interactiva
>
> El sistema es escalable y puede aplicarse a múltiples dominios como:
> clasificación de noticias, análisis de sentimientos, detección de spam, 
> o sistemas de recomendación."

### PANTALLA: Código abierto / GitHub

**DECIR:**
> "Todo el código está disponible en el enlace que he compartido, 
> incluyendo la documentación completa, los scripts de ejemplo, 
> y las instrucciones de instalación."

### PANTALLA: Tu nombre/contacto

**DECIR:**
> "Muchas gracias por ver este video. Si tienen alguna pregunta o 
> sugerencia, pueden contactarme. ¡Hasta pronto!"

---

## ✅ CHECKLIST ANTES DE GRABAR

### Preparación del entorno:
- [ ] Cerrar todas las aplicaciones innecesarias
- [ ] Limpiar el escritorio (sin archivos personales visibles)
- [ ] Cerrar notificaciones del sistema
- [ ] Poner el teléfono en silencio
- [ ] Probar el micrófono
- [ ] Buena iluminación
- [ ] Cámara estable (si vas a aparecer)

### Preparación técnica:
- [ ] Entorno virtual activado
- [ ] Todas las dependencias instaladas
- [ ] Terminal en la carpeta correcta
- [ ] Scripts de ejemplo probados
- [ ] Aplicación Streamlit funciona correctamente
- [ ] Textos de ejemplo listos para copiar/pegar
- [ ] Navegador limpio (cerrar tabs innecesarias)

### Durante la grabación:
- [ ] Hablar claro y a un ritmo moderado
- [ ] Hacer pausas entre secciones
- [ ] Explicar QUÉ haces y POR QUÉ lo haces
- [ ] Si cometes un error, no te detengas, sigue grabando
- [ ] Sonríe (se nota en la voz)
- [ ] Mantén energía y entusiasmo

---

## 🎤 CONSEJOS DE PRESENTACIÓN

### Tono de voz:
- Habla con entusiasmo pero natural
- Varía el tono para evitar monotonía
- Haz pausas estratégicas
- Enfatiza los puntos importantes

### Ritmo:
- No hables demasiado rápido
- Da tiempo para que el espectador procese
- Espera a que terminen las animaciones/carga de la app

### Contenido:
- Sé conciso pero completo
- Explica el "porqué", no solo el "cómo"
- Usa ejemplos concretos
- Evita jerga excesiva (o explícala)

---

## 🎬 SOFTWARE DE GRABACIÓN RECOMENDADO

### Windows 11:
- **OBS Studio** (Gratis, profesional)
- **Xbox Game Bar** (Win+G, integrado en Windows)
- **ShareX** (Gratis, simple)
- **Camtasia** (Pago, muy completo)

### Configuración recomendada:
- Resolución: 1920x1080 (Full HD)
- FPS: 30
- Audio: 48kHz, estéreo
- Bitrate: 5000-8000 kbps

---

## 📤 DESPUÉS DE GRABAR

### Edición (opcional):
- Cortar silencios largos
- Añadir intro/outro (5-10 seg)
- Ajustar volumen de audio
- Añadir texto en pantalla en puntos clave

### Subida:
1. **YouTube:**
   - Título: "Sistema de Aprendizaje en la Web - Machine Learning + NLP"
   - Descripción: Incluir enlace al código
   - Tags: machine learning, python, nlp, web scraping, streamlit
   - Visibilidad: Público o "No listado"

2. **Google Drive:**
   - Subir video
   - Cambiar permisos: "Cualquiera con el enlace puede ver"
   - Copiar enlace

### Compartir:
- [ ] Copiar enlace del video
- [ ] Copiar enlace del código (GitHub/Drive)
- [ ] Verificar que ambos enlaces sean públicos
- [ ] Enviar enlaces según instrucciones del profesor

---

## 💪 ¡ÁNIMO!

Recuerda: No tiene que ser perfecto. Lo importante es que demuestres:
1. Entiendes el tema
2. Implementaste el proyecto
3. Puedes explicarlo claramente
4. El sistema funciona

**¡Tú puedes! 🚀**
