"""
=======================================================
MÓDULO 4: APLICACIÓN WEB - Interfaz Streamlit
=======================================================
Aplicación web interactiva para demostrar el sistema
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Añadir el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from scraping import WebScraper
from preprocessing import PreprocesadorTexto
from model import ModeloAprendizajeWeb
import plotly.express as px
import plotly.graph_objects as go


# Configuración de la página
st.set_page_config(
    page_title="Sistema de Aprendizaje Web",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        padding-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


def inicializar_sesion():
    """Inicializa variables de sesión"""
    if 'scraper' not in st.session_state:
        st.session_state.scraper = WebScraper()
    if 'preprocesador' not in st.session_state:
        st.session_state.preprocesador = PreprocesadorTexto()
    if 'modelo' not in st.session_state:
        st.session_state.modelo = ModeloAprendizajeWeb()
    if 'datos' not in st.session_state:
        st.session_state.datos = None
    if 'modelo_entrenado' not in st.session_state:
        st.session_state.modelo_entrenado = False


def pagina_inicio():
    """Página principal con información del sistema"""
    st.markdown('<h1 class="main-header">🌐 Sistema de Aprendizaje en la Web</h1>', 
                unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Extrae, Procesa y Aprende de Contenido Web Automáticamente</p>', 
                unsafe_allow_html=True)
    
    # Descripción del sistema
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📥 1. Extracción
        El sistema extrae contenido de páginas web utilizando técnicas de **web scraping**.
        
        - Extrae texto de URLs
        - Limpia HTML
        - Identifica contenido relevante
        """)
    
    with col2:
        st.markdown("""
        ### 🔧 2. Procesamiento
        Preprocesa el texto usando técnicas de **NLP** (Procesamiento de Lenguaje Natural).
        
        - Tokenización
        - Eliminación de stopwords
        - Vectorización TF-IDF
        """)
    
    with col3:
        st.markdown("""
        ### 🤖 3. Aprendizaje
        Aplica modelos de **Machine Learning** para clasificar y agrupar contenido.
        
        - Clasificación supervisada
        - Clustering automático
        - Predicciones en tiempo real
        """)
    
    st.divider()
    
    # Flujo del sistema
    st.subheader("🔄 Flujo del Sistema")
    
    flow_diagram = """
    ```
    URL/Texto → Web Scraping → Preprocesamiento → Vectorización → Modelo ML → Resultados
    ```
    """
    st.markdown(flow_diagram)
    
    # Instrucciones
    st.info("""
    👈 **Usa el menú lateral para navegar:**
    - **Extracción de Datos**: Extrae contenido de URLs
    - **Entrenamiento**: Entrena modelos de clasificación
    - **Predicción**: Clasifica nuevo contenido
    - **Análisis**: Visualiza resultados y estadísticas
    """)


def pagina_extraccion():
    """Página para extraer datos de la web"""
    st.header("📥 Extracción de Datos Web")
    
    # Opciones de extracción
    modo = st.radio(
        "Selecciona el modo de extracción:",
        ["URLs individuales", "Texto directo", "Dataset de ejemplo"]
    )
    
    if modo == "URLs individuales":
        st.subheader("Ingresa las URLs a extraer")
        
        urls_text = st.text_area(
            "URLs (una por línea):",
            height=150,
            placeholder="https://ejemplo.com/articulo1\nhttps://ejemplo.com/articulo2"
        )
        
        if st.button("🚀 Extraer Contenido"):
            if urls_text:
                urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
                
                with st.spinner(f"Extrayendo contenido de {len(urls)} URLs..."):
                    df = st.session_state.scraper.extraer_multiples_urls(urls)
                    st.session_state.datos = df
                
                if not df.empty:
                    st.success(f"✅ Se extrajeron {len(df)} documentos exitosamente")
                    
                    # Verificar si hay categorías
                    if 'categoria' not in df.columns:
                        st.warning("""
                        ⚠️ **Nota importante:** Los datos extraídos no tienen categorías asignadas.
                        """)
                        
                        # NUEVO: Botón de categorización automática
                        st.info("""
                        💡 **¡Prueba la categorización automática!**
                        
                        Usa inteligencia artificial para identificar automáticamente 
                        las categorías de tus documentos sin necesidad de etiquetarlos manualmente.
                        """)
                        
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            if st.button("🤖 Categorizar Automáticamente", type="primary"):
                                with st.spinner("Analizando contenido y detectando categorías..."):
                                    from categorizador_auto import CategorizadorAutomatico
                                    from preprocessing import PreprocesadorTexto
                                    
                                    # Preprocesar si no está ya procesado
                                    if 'texto_procesado' not in df.columns:
                                        prep = PreprocesadorTexto()
                                        df['texto_procesado'] = df['texto'].apply(prep.procesar_texto)
                                    
                                    # Categorizar
                                    categorizador = CategorizadorAutomatico()
                                    df = categorizador.analizar_y_categorizar(df)
                                    
                                    # Renombrar columna
                                    df['categoria'] = df['categoria_auto']
                                    
                                    # Actualizar en session state
                                    st.session_state.datos = df
                                    
                                    st.success("✅ ¡Categorización automática completada!")
                                    st.rerun()
                        
                        with col2:
                            st.markdown("""
                            **Alternativas manuales:**
                            1. Usar el **Dataset de ejemplo** que ya tiene categorías
                            2. Agregar documentos con **"Texto directo"** y seleccionar categorías
                            """)
                    
                    st.dataframe(df)
                    
                    # Estadísticas
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("📄 Total Documentos", len(df))
                    with col2:
                        st.metric("📊 Promedio Palabras", int(df['longitud'].mean()))
                    with col3:
                        st.metric("📝 Total Palabras", int(df['longitud'].sum()))
                else:
                    st.error("❌ No se pudo extraer contenido")
            else:
                st.warning("⚠️ Por favor ingresa al menos una URL")
    
    elif modo == "Texto directo":
        st.subheader("Ingresa texto manualmente")
        
        col1, col2 = st.columns(2)
        with col1:
            titulo = st.text_input("Título del documento:")
        with col2:
            # Opción de categoría manual o automática
            modo_categoria = st.radio(
                "Modo de categoría:",
                ["Manual", "Automática"],
                horizontal=True,
                help="Manual: Tú seleccionas la categoría. Automática: IA la detecta."
            )
        
        texto = st.text_area("Contenido:", height=200)
        
        # Mostrar selector de categoría solo si es manual
        if modo_categoria == "Manual":
            categoria = st.selectbox("Categoría:", 
                                    ["Tecnología", "Ciencia", "Deportes", "Política", 
                                     "Música", "Arte", "Literatura", "Cine", "Otro"])
        else:
            st.info("💡 La categoría se detectará automáticamente al agregar el documento")
            categoria = None
        
        if st.button("➕ Agregar Documento"):
            if titulo and texto:
                # Si es automática, detectar la categoría
                if modo_categoria == "Automática":
                    with st.spinner("Detectando categoría..."):
                        from categorizador_auto import CategorizadorAutomatico
                        from preprocessing import PreprocesadorTexto
                        
                        prep = PreprocesadorTexto()
                        texto_procesado = prep.procesar_texto(texto)
                        
                        categorizador = CategorizadorAutomatico()
                        categoria_detectada, confianza = categorizador.detectar_categoria_por_keywords(texto_procesado)
                        
                        categoria = categoria_detectada
                        st.success(f"✅ Categoría detectada: **{categoria}** (confianza: {confianza:.2f})")
                
                nuevo_doc = pd.DataFrame([{
                    'titulo': titulo,
                    'texto': texto,
                    'categoria': categoria,
                    'longitud': len(texto.split())
                }])
                
                if st.session_state.datos is None:
                    st.session_state.datos = nuevo_doc
                else:
                    st.session_state.datos = pd.concat(
                        [st.session_state.datos, nuevo_doc], 
                        ignore_index=True
                    )
                
                st.success("✅ Documento agregado correctamente")
                st.dataframe(st.session_state.datos)
            else:
                st.warning("⚠️ Por favor completa todos los campos")
    
    else:  # Dataset de ejemplo
        st.subheader("Cargar Dataset de Ejemplo")
        st.info("Este dataset contiene artículos de ejemplo pre-clasificados")
        
        if st.button("📦 Cargar Dataset de Ejemplo"):
            # Crear dataset sintético
            df_ejemplo = crear_dataset_ejemplo()
            st.session_state.datos = df_ejemplo
            
            st.success(f"✅ Dataset cargado: {len(df_ejemplo)} documentos")
            st.dataframe(df_ejemplo)
            
            # Visualizar distribución
            fig = px.histogram(df_ejemplo, x='categoria', 
                             title='Distribución de Documentos por Categoría')
            st.plotly_chart(fig, use_container_width=True)


def crear_dataset_ejemplo():
    """Crea un dataset de ejemplo para demostración"""
    datos = {
        'titulo': [
            'Inteligencia Artificial en la Medicina',
            'Nuevos Algoritmos de Machine Learning',
            'Python para Ciencia de Datos',
            'Campeonato Mundial de Fútbol 2024',
            'Los Mejores Jugadores de Basketball',
            'Técnicas de Entrenamiento Deportivo',
            'Descubrimiento en Física Cuántica',
            'Avances en Biología Molecular',
            'Nueva Teoría sobre el Universo'
        ],
        'texto': [
            'La inteligencia artificial está transformando el diagnóstico médico mediante algoritmos avanzados de aprendizaje profundo que analizan imágenes y datos clínicos.',
            'Los nuevos algoritmos de machine learning permiten procesar grandes volúmenes de datos con mayor precisión y eficiencia en tiempo real.',
            'Python se ha consolidado como el lenguaje preferido para análisis de datos gracias a bibliotecas como pandas numpy y scikit-learn.',
            'El campeonato mundial de fútbol reúne a las mejores selecciones del planeta en un torneo emocionante con millones de espectadores.',
            'Los jugadores de basketball más destacados demuestran habilidades excepcionales en cancha y lideran a sus equipos hacia la victoria.',
            'Las técnicas modernas de entrenamiento deportivo combinan ciencia ejercicio y nutrición para optimizar el rendimiento de los atletas.',
            'Científicos han logrado avances significativos en física cuántica que podrían revolucionar la computación y las comunicaciones.',
            'La investigación en biología molecular revela nuevos mecanismos celulares que abren posibilidades para tratamientos médicos innovadores.',
            'Una nueva teoría cosmológica propone explicaciones alternativas sobre la formación y evolución del universo observable.'
        ],
        'categoria': [
            'Tecnología', 'Tecnología', 'Tecnología',
            'Deportes', 'Deportes', 'Deportes',
            'Ciencia', 'Ciencia', 'Ciencia'
        ]
    }
    
    df = pd.DataFrame(datos)
    df['longitud'] = df['texto'].apply(lambda x: len(x.split()))
    return df


def pagina_entrenamiento():
    """Página para entrenar modelos"""
    st.header("🤖 Entrenamiento de Modelos")
    
    if st.session_state.datos is None or st.session_state.datos.empty:
        st.warning("⚠️ Primero debes extraer o cargar datos en la sección 'Extracción de Datos'")
        return
    
    st.subheader("Datos Disponibles")
    st.dataframe(st.session_state.datos)
    
    # Verificar si hay columna de categorías
    if 'categoria' not in st.session_state.datos.columns:
        st.error("""
        ❌ **Los datos no tienen etiquetas de categoría**
        
        ### Para poder entrenar un modelo necesitas:
        
        **Opción 1: Usar el Dataset de Ejemplo**
        - Ve a **"Extracción de Datos"**
        - Selecciona **"Dataset de ejemplo"**
        - Carga el dataset (tiene 9 documentos con 3 categorías)
        
        **Opción 2: Agregar Categorías Manualmente**
        - Ve a **"Extracción de Datos"**
        - Usa **"Texto directo"** para agregar documentos con categorías
        
        **Opción 3: Editar el CSV**
        - Descarga los datos actuales
        - Agrega una columna "categoria" en Excel
        - Vuelve a cargar el archivo (implementación futura)
        
        **Opción 4: Usar Clustering (No Supervisado)**
        - El clustering NO requiere categorías
        - Agrupa documentos similares automáticamente
        - (Implementación futura en esta app)
        """)
        return
    
    st.divider()
    
    # Preprocesamiento
    st.subheader("1️⃣ Preprocesamiento de Texto")
    
    if st.button("🔧 Procesar Textos"):
        with st.spinner("Procesando textos..."):
            prep = st.session_state.preprocesador
            
            # Procesar cada texto
            textos_procesados = []
            for texto in st.session_state.datos['texto']:
                texto_proc = prep.procesar_texto(texto)
                textos_procesados.append(texto_proc)
            
            st.session_state.datos['texto_procesado'] = textos_procesados
            
            # Vectorizar
            st.session_state.vectores = prep.vectorizar_textos(textos_procesados)
            
            st.success("✅ Preprocesamiento completado")
            
            # Mostrar ejemplo
            with st.expander("Ver ejemplo de procesamiento"):
                idx = 0
                st.write("**Texto original:**")
                st.write(st.session_state.datos.iloc[idx]['texto'][:200] + "...")
                st.write("**Texto procesado:**")
                st.write(st.session_state.datos.iloc[idx]['texto_procesado'])
    
    st.divider()
    
    # Entrenamiento
    st.subheader("2️⃣ Entrenar Modelo de Clasificación")
    
    if 'vectores' not in st.session_state:
        st.info("ℹ️ Primero procesa los textos usando el botón de arriba")
    else:
        # Calcular límites apropiados según el tamaño del dataset
        n_samples = len(st.session_state.datos)
        n_classes = st.session_state.datos['categoria'].nunique()
        
        # Información sobre el dataset
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total Muestras", n_samples)
        with col2:
            st.metric("🏷️ Categorías", n_classes)
        with col3:
            min_per_class = st.session_state.datos['categoria'].value_counts().min()
            st.metric("📉 Mínimo/Categoría", min_per_class)
        
        # Advertencias para datasets pequeños
        if n_samples < 15:
            st.warning(f"""
            ⚠️ **Dataset pequeño detectado ({n_samples} muestras)**
            
            Para mejores resultados:
            - Se recomienda al menos 15-20 documentos
            - Mínimo 3-5 ejemplos por categoría
            - Considera agregar más datos
            """)
        
        # Ajustar límites del slider
        if n_samples < 10:
            max_test = 40
            default_test = 30
            st.info("ℹ️ Usando 30% para test debido al tamaño pequeño del dataset")
        else:
            max_test = 40
            default_test = 20
        
        test_size = st.slider(
            "Porcentaje de datos para prueba:", 
            min_value=10, 
            max_value=max_test, 
            value=default_test, 
            step=5,
            help="""
            - 10-20%: Recomendado para datasets grandes (>100 muestras)
            - 20-30%: Recomendado para datasets medianos (20-100 muestras)
            - 30-40%: Recomendado para datasets pequeños (<20 muestras)
            """
        ) / 100
        
        if st.button("🚀 Entrenar Modelo"):
            with st.spinner("Entrenando modelo..."):
                X = st.session_state.vectores
                y = st.session_state.datos['categoria'].values
                
                modelo = st.session_state.modelo
                metricas = modelo.entrenar_clasificador(X, y, test_size=test_size)
                
                st.session_state.metricas = metricas
                st.session_state.modelo_entrenado = True
                
                # Mostrar resultados
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("🎯 Precisión", f"{metricas['accuracy']:.1%}")
                with col2:
                    st.metric("📊 Categorías", len(metricas['categorias']))
                with col3:
                    st.metric("📈 F1-Score", 
                             f"{metricas['reporte']['weighted avg']['f1-score']:.2f}")
                
                st.success("✅ Modelo entrenado exitosamente")
                
                # Reporte detallado
                with st.expander("📋 Ver Reporte Detallado"):
                    for cat in metricas['categorias']:
                        st.write(f"**{cat}:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Precision", 
                                    f"{metricas['reporte'][cat]['precision']:.2f}")
                        with col2:
                            st.metric("Recall", 
                                    f"{metricas['reporte'][cat]['recall']:.2f}")
                        with col3:
                            st.metric("F1-Score", 
                                    f"{metricas['reporte'][cat]['f1-score']:.2f}")


def pagina_prediccion():
    """Página para hacer predicciones con el modelo"""
    st.header("🔮 Predicción de Categorías")
    
    if not st.session_state.modelo_entrenado:
        st.warning("⚠️ Primero debes entrenar el modelo en la sección 'Entrenamiento'")
        return
    
    st.subheader("Ingresa un nuevo texto para clasificar")
    
    texto_nuevo = st.text_area(
        "Texto a clasificar:",
        height=150,
        placeholder="Escribe o pega aquí el texto que quieres clasificar..."
    )
    
    if st.button("🎯 Predecir Categoría"):
        if texto_nuevo:
            with st.spinner("Analizando texto..."):
                # Preprocesar
                prep = st.session_state.preprocesador
                texto_procesado = prep.procesar_texto(texto_nuevo)
                
                # Vectorizar
                vector = prep.vectorizer.transform([texto_procesado])
                
                # Predecir
                modelo = st.session_state.modelo
                prediccion, probabilidades = modelo.predecir_con_probabilidad(vector)
                
                # Mostrar resultado
                st.success(f"✅ Categoría Predicha: **{prediccion[0]}**")
                
                # Mostrar probabilidades
                st.subheader("📊 Probabilidades por Categoría")
                
                prob_df = pd.DataFrame({
                    'Categoría': modelo.categorias,
                    'Probabilidad': probabilidades[0]
                })
                prob_df = prob_df.sort_values('Probabilidad', ascending=False)
                
                fig = px.bar(prob_df, x='Categoría', y='Probabilidad',
                           title='Distribución de Probabilidades',
                           color='Probabilidad',
                           color_continuous_scale='Blues')
                st.plotly_chart(fig, use_container_width=True)
                
                # Mostrar texto procesado
                with st.expander("Ver texto procesado"):
                    st.write(texto_procesado)
        else:
            st.warning("⚠️ Por favor ingresa un texto")


def pagina_analisis():
    """Página de análisis y visualizaciones"""
    st.header("📊 Análisis y Visualizaciones")
    
    if st.session_state.datos is None:
        st.warning("⚠️ No hay datos disponibles para analizar")
        return
    
    df = st.session_state.datos
    
    # Estadísticas generales
    st.subheader("📈 Estadísticas Generales")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 Total Documentos", len(df))
    with col2:
        st.metric("📝 Total Palabras", int(df['longitud'].sum()))
    with col3:
        st.metric("📊 Promedio Palabras", int(df['longitud'].mean()))
    with col4:
        if 'categoria' in df.columns:
            st.metric("🏷️ Categorías", df['categoria'].nunique())
    
    st.divider()
    
    # Distribución de longitudes
    st.subheader("📏 Distribución de Longitud de Documentos")
    fig = px.histogram(df, x='longitud', nbins=20,
                      title='Distribución de Palabras por Documento')
    st.plotly_chart(fig, use_container_width=True)
    
    # Distribución por categoría (si existe)
    if 'categoria' in df.columns:
        st.divider()
        st.subheader("🏷️ Distribución por Categoría")
        
        cat_counts = df['categoria'].value_counts()
        fig = px.pie(values=cat_counts.values, names=cat_counts.index,
                    title='Proporción de Documentos por Categoría')
        st.plotly_chart(fig, use_container_width=True)
    
    # Métricas del modelo (si está entrenado)
    if st.session_state.modelo_entrenado:
        st.divider()
        st.subheader("🤖 Métricas del Modelo")
        
        metricas = st.session_state.metricas
        
        # Gráfico de métricas por categoría
        categorias = metricas['categorias']
        precision_vals = [metricas['reporte'][cat]['precision'] for cat in categorias]
        recall_vals = [metricas['reporte'][cat]['recall'] for cat in categorias]
        f1_vals = [metricas['reporte'][cat]['f1-score'] for cat in categorias]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=categorias, y=precision_vals, name='Precision'))
        fig.add_trace(go.Bar(x=categorias, y=recall_vals, name='Recall'))
        fig.add_trace(go.Bar(x=categorias, y=f1_vals, name='F1-Score'))
        
        fig.update_layout(
            title='Métricas del Modelo por Categoría',
            barmode='group',
            xaxis_title='Categoría',
            yaxis_title='Valor'
        )
        st.plotly_chart(fig, use_container_width=True)


def main():
    """Función principal de la aplicación"""
    inicializar_sesion()
    
    # Sidebar
    st.sidebar.title("🌐 Navegación")
    st.sidebar.markdown("---")
    
    pagina = st.sidebar.radio(
        "Selecciona una sección:",
        ["🏠 Inicio", 
         "📥 Extracción de Datos", 
         "🤖 Entrenamiento",
         "🔮 Predicción",
         "📊 Análisis"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Sistema de Aprendizaje Web**
    
    Proyecto académico que demuestra:
    - Web Scraping
    - Procesamiento NLP
    - Machine Learning
    - Aplicación Streamlit
    """)
    
    # Renderizar página seleccionada
    if "Inicio" in pagina:
        pagina_inicio()
    elif "Extracción" in pagina:
        pagina_extraccion()
    elif "Entrenamiento" in pagina:
        pagina_entrenamiento()
    elif "Predicción" in pagina:
        pagina_prediccion()
    elif "Análisis" in pagina:
        pagina_analisis()


if __name__ == "__main__":
    main()
