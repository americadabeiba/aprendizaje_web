"""
=================================================
MÓDULO 1: WEB SCRAPING - Extracción de Contenido
=================================================
Este módulo se encarga de extraer texto de páginas web
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from typing import List, Dict
import pandas as pd


class WebScraper:
    """Clase para extraer contenido de sitios web"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def extraer_texto_url(self, url: str) -> Dict[str, str]:
        """
        Extrae el texto principal de una URL
        
        Args:
            url: La URL del sitio web
            
        Returns:
            Diccionario con título, texto y URL
        """
        try:
            print(f"📥 Extrayendo contenido de: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Extraer título
            titulo = soup.find('h1')
            titulo = titulo.get_text().strip() if titulo else "Sin título"
            
            # Extraer texto de párrafos
            parrafos = soup.find_all('p')
            texto = ' '.join([p.get_text().strip() for p in parrafos])
            
            # Limpiar texto
            texto = self.limpiar_texto(texto)
            
            return {
                'url': url,
                'titulo': titulo,
                'texto': texto,
                'longitud': len(texto.split())
            }
            
        except Exception as e:
            print(f"❌ Error al extraer {url}: {e}")
            return None
    
    def limpiar_texto(self, texto: str) -> str:
        """Limpia el texto eliminando caracteres extraños"""
        # Eliminar saltos de línea múltiples
        texto = re.sub(r'\n+', ' ', texto)
        # Eliminar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto)
        # Eliminar caracteres especiales extraños
        texto = re.sub(r'[^\w\s.,;:!?¿¡áéíóúüñÁÉÍÓÚÜÑ-]', '', texto)
        return texto.strip()
    
    def extraer_multiples_urls(self, urls: List[str], delay: float = 1.0) -> pd.DataFrame:
        """
        Extrae contenido de múltiples URLs
        
        Args:
            urls: Lista de URLs
            delay: Tiempo de espera entre peticiones (segundos)
            
        Returns:
            DataFrame con los contenidos extraídos
        """
        resultados = []
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Procesando URL...")
            resultado = self.extraer_texto_url(url)
            
            if resultado:
                resultados.append(resultado)
            
            # Pausa para no sobrecargar el servidor
            if i < len(urls):
                time.sleep(delay)
        
        df = pd.DataFrame(resultados)
        print(f"\n✅ Se extrajeron {len(df)} documentos exitosamente")
        return df


# ========================================
# EJEMPLO DE USO
# ========================================
if __name__ == "__main__":
    # URLs de ejemplo (noticias de tecnología)
    urls_ejemplo = [
        "https://es.wikipedia.org/wiki/Inteligencia_artificial",
        "https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico",
        "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programaci%C3%B3n)"
    ]
    
    # Crear scraper
    scraper = WebScraper()
    
    # Extraer contenido
    df_contenido = scraper.extraer_multiples_urls(urls_ejemplo)
    
    # Mostrar resultados
    print("\n" + "="*60)
    print("CONTENIDOS EXTRAÍDOS:")
    print("="*60)
    for idx, row in df_contenido.iterrows():
        print(f"\n📄 Documento {idx + 1}:")
        print(f"   Título: {row['titulo']}")
        print(f"   URL: {row['url']}")
        print(f"   Palabras: {row['longitud']}")
        print(f"   Preview: {row['texto'][:150]}...")
    
    # Guardar a CSV
    df_contenido.to_csv('data/raw/contenido_extraido.csv', index=False, encoding='utf-8')
    print("\n💾 Datos guardados en: data/raw/contenido_extraido.csv")
