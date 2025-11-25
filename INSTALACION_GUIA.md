# 🚀 GUÍA DE INSTALACIÓN - WINDOWS 11
## Sistema de Aprendizaje en la Web

### PASO 1: VERIFICAR PYTHON
```powershell
# Abrir PowerShell o CMD y verificar versión de Python
python --version
# Debe ser Python 3.8 o superior
```

**Si no tienes Python instalado:**
1. Descargar desde: https://www.python.org/downloads/
2. Durante la instalación, MARCAR "Add Python to PATH"
3. Reiniciar la terminal

---

### PASO 2: CREAR ENTORNO VIRTUAL (RECOMENDADO)
```powershell
# Navegar a la carpeta de tu proyecto
cd C:\ruta\a\tu\proyecto

# Crear entorno virtual
python -m venv venv_aprendizaje_web

# Activar el entorno virtual
venv_aprendizaje_web\Scripts\activate

# Verás (venv_aprendizaje_web) al inicio de la línea
```

---

### PASO 3: INSTALAR DEPENDENCIAS
```powershell
# Con el entorno virtual activado:
pip install --upgrade pip

# Instalar todas las librerías del requirements.txt
pip install -r requirements.txt

# Esto puede tardar varios minutos
```

---

### PASO 4: DESCARGAR RECURSOS ADICIONALES

#### Para NLTK (procesamiento de lenguaje):
```python
# Ejecutar en Python:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

#### Para spaCy (modelo en español):
```powershell
python -m spacy download es_core_news_sm
```

---

### PASO 5: VERIFICAR INSTALACIÓN
```python
# Crear archivo test_install.py y ejecutar:
import requests
import bs4
import sklearn
import pandas
import streamlit
print("✅ Todas las librerías están instaladas correctamente!")
```

---

### SOLUCIÓN DE PROBLEMAS COMUNES

**Error: "pip no se reconoce"**
- Reinstalar Python marcando "Add to PATH"
- O añadir manualmente: `C:\Python3X\Scripts` al PATH

**Error al instalar lxml en Windows:**
```powershell
pip install lxml‑4.9.3‑cp311‑cp311‑win_amd64.whl
# Descargar .whl desde: https://www.lfd.uci.edu/~gohlke/pythonlibs/
```

**Error de permisos:**
```powershell
# Ejecutar PowerShell como Administrador
# O usar: pip install --user -r requirements.txt
```

---

### ESTRUCTURA DE CARPETAS RECOMENDADA
```
proyecto_aprendizaje_web/
│
├── venv_aprendizaje_web/     # Entorno virtual
├── requirements.txt           # Dependencias
├── data/                      # Datos extraídos
│   ├── raw/                   # Datos crudos
│   └── processed/             # Datos procesados
├── models/                    # Modelos entrenados
├── notebooks/                 # Jupyter notebooks (exploración)
├── src/                       # Código fuente
│   ├── scraping.py
│   ├── preprocessing.py
│   ├── model.py
│   └── app.py
└── results/                   # Resultados y visualizaciones
```

---

### COMANDOS ÚTILES

```powershell
# Activar entorno virtual
venv_aprendizaje_web\Scripts\activate

# Desactivar entorno virtual
deactivate

# Ver librerías instaladas
pip list

# Actualizar una librería específica
pip install --upgrade nombre_libreria

# Ejecutar la aplicación Streamlit
streamlit run src/app.py
```

---

### PRÓXIMOS PASOS
Una vez completada la instalación:
1. ✅ Ejecutar el script de prueba
2. ✅ Revisar el código de ejemplo
3. ✅ Comenzar con el proyecto práctico
4. ✅ Crear la aplicación web con Streamlit

---

**Nota**: Si encuentras algún error específico, copia el mensaje completo del error para buscar la solución en Google o StackOverflow.
