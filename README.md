
---

# Análisis de Bitcoin: Proyecto de Programación Orientada a Objetos

## Descripción del Proyecto
Este proyecto se centra en el análisis histórico de los precios de Bitcoin mediante técnicas de programación orientada a objetos (POO) y análisis de datos. El objetivo principal es ayudar a entender la tendencia de precios y la volatilidad de Bitcoin, además de explorar cómo factores externos, como eventos políticos o económicos, pueden influir en estos valores.

## Objetivos
1. **Visualización de la Tendencia de Precios**: Observar la evolución histórica de los precios de Bitcoin.
2. **Cálculo y Visualización de la Volatilidad**: Determinar la volatilidad histórica para identificar periodos de riesgo y oportunidad.
3. **Análisis de Factores Externos**: Explorar cómo eventos como la pandemia de COVID-19 o elecciones en EE.UU. pueden haber afectado el valor de Bitcoin.
4. **Implementación de POO**: Aplicar los cuatro pilares de la programación orientada a objetos en el análisis.

## Estructura del Proyecto

- `main.py`: Archivo principal que ejecuta el análisis completo.
- `src/loader/carga_datos.py`: Módulo encargado de cargar y preprocesar los datos de Bitcoin.
- `src/preprocessing/preprocessor.py`: Contiene funciones de limpieza y filtrado de datos.
- `src/analysis/bitcoin_analisis.py`: Módulo donde se realizan los análisis de tendencias, volatilidad, y detección de picos y valles en los precios.
  
## Instalación
1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/samusplay/invader_data.git
   cd invader_data
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del Proyecto
Para ejecutar el análisis, ejecuta el archivo `main.py`:
```bash
python main.py
```

## Secciones Principales del Análisis

### 1. **Tendencia de Precios con Promedio Móvil**
   - **Objetivo**: Visualizar el precio de cierre de Bitcoin con su promedio móvil (Moving Average) para identificar tendencias.
   - **Método**: Se calcula el promedio móvil de 30 días, el cual suaviza las fluctuaciones de corto plazo y permite visualizar tendencias a largo plazo.
   - **Interpretación**: Cuando el precio está por encima del promedio móvil, podría indicar una tendencia alcista. Lo contrario sugiere cautela.

### 2. **Volatilidad de Bitcoin**
   - **Objetivo**: Determinar los periodos de alta volatilidad.
   - **Método**: La volatilidad se calcula como la desviación estándar de los retornos diarios en una ventana de 30 días.
   - **Interpretación**: Picos de volatilidad sugieren periodos de riesgo elevado, mientras que baja volatilidad indica estabilidad en el precio.

### 3. **Análisis de Picos y Valles**
   - **Objetivo**: Identificar los puntos máximos (picos) y mínimos (valles) en el precio de Bitcoin.
   - **Método**: Se utiliza un método de detección de picos y valles basado en el valor relativo en el precio de cierre.
   - **Interpretación**: Los picos y valles permiten identificar periodos óptimos de compra o venta, ayudando en la toma de decisiones de inversión.

## Influencias Políticas y Económicas en Bitcoin

1. **Victoria de Donald Trump (2016)**: Este evento impulsó el valor de Bitcoin debido a la incertidumbre económica y la búsqueda de refugios alternativos de inversión. 
2. **Pandemia de COVID-19 (2020)**: La crisis global incrementó la volatilidad de activos financieros. Bitcoin se benefició como refugio frente a la inflación, ya que muchas personas buscaron alternativas a las monedas tradicionales.
3. **Eventos de Regulación**: Ciertos anuncios de regulación en distintos países han impactado la volatilidad y el precio de Bitcoin, ya sea aumentando o disminuyendo la confianza del mercado.

## Análisis Estadístico Realizado
Se calcularon los siguientes valores para comprender mejor los datos:
- **Media**: Representa el precio promedio de Bitcoin durante el periodo analizado.
- **Desviación Estándar**: Mide la dispersión de los precios respecto a la media, lo cual es crucial para entender la volatilidad.
- **Picos y Valles**: La identificación de máximos y mínimos locales en los datos históricos permite visualizar periodos de alta y baja actividad en el mercado.

## Interpretación del Análisis
Este análisis proporciona una herramienta de apoyo en la toma de decisiones financieras:
- **Alta volatilidad** implica mayores riesgos, pero también posibles grandes oportunidades de ganancia a corto plazo.
- **Precios por debajo del promedio móvil** podrían sugerir una oportunidad de compra, ya que el precio está "descontado" frente a su tendencia.
- **Eventos geopolíticos** tienen un impacto notable en Bitcoin, dado su rol como activo alternativo de inversión en tiempos de incertidumbre.

## Conclusión y Aplicación Práctica
Este proyecto ilustra cómo analizar datos financieros utilizando Python y técnicas de POO. Además, ofrece una visión sobre cómo factores externos pueden influir en activos como Bitcoin. Este conocimiento es valioso para cualquier persona interesada en comprender mejor el mercado de criptomonedas y en desarrollar herramientas para la toma de decisiones.

Este enfoque orientado a objetos permite la escalabilidad del proyecto, por lo que en el futuro se pueden agregar más tipos de análisis o incluso extender el análisis a otros activos.

## Futuras Extensiones
- **Modelos Predictivos (ARIMA)**: Incluir un modelo ARIMA para realizar predicciones sobre el precio futuro de Bitcoin.
- **Análisis de Sentimiento**: Incorporar datos de redes sociales para entender cómo las percepciones del público afectan el precio de Bitcoin.
- **Aplicación Educativa**: Desarrollar una plataforma donde usuarios puedan aprender sobre finanzas y análisis de criptomonedas de manera interactiva.

--- 
