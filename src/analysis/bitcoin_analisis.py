import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

class BitcoinAnalyzer:
    def __init__(self, df):
        self.df = df

    def calculate_moving_average(self, window=30):
        """Calcula el promedio móvil del precio de cierre"""
        if 'Close' in self.df.columns:
            self.df['Moving_Average'] = self.df['Close'].rolling(window=window).mean()
            print(f"Promedio móvil calculado con ventana de {window} días.")
        else:
            print("La columna 'Close' no se encuentra en los datos.")
        return self.df

    def calculate_volatility(self):
        """Calcula la volatilidad diaria de los precios de cierre"""
        if 'Close' in self.df.columns:
            self.df['Daily_Return'] = self.df['Close'].pct_change()  # Retorno diario
            self.df['Volatility'] = self.df['Daily_Return'].rolling(window=30).std()  # Volatilidad de 30 días
            print("Volatilidad diaria calculada.")
        else:
            print("La columna 'Close' no se encuentra en los datos.")
        return self.df

    def plot_interactive_price_trends(self):
        """Genera un gráfico interactivo de la tendencia de precios y el promedio móvil"""
        if 'Date' in self.df.columns and 'Close' in self.df.columns:
            fig = px.line(
                self.df,
                x='Date',
                y=['Close', 'Moving_Average'],
                title='Tendencia de Precios de Bitcoin con Promedio Móvil',
                labels={'Date': 'Fecha', 'value': 'Precio (USD)'},
                template='plotly_dark'
            )
            fig.update_layout(legend_title_text='Indicadores')
            fig.show()
        else:
            print("Columnas necesarias para el gráfico no encontradas en los datos.")

    def plot_volatility(self):
        """Genera un gráfico interactivo de la volatilidad"""
        if 'Date' in self.df.columns and 'Volatility' in self.df.columns:
            fig = px.line(
                self.df,
                x='Date',
                y='Volatility',
                title='Volatilidad de Bitcoin (30 días)',
                labels={'Date': 'Fecha', 'Volatility': 'Volatilidad'},
                template='plotly_dark'
            )
            fig.update_layout(legend_title_text='Indicadores')
            fig.show()
        else:
            print("Columnas necesarias para el gráfico de volatilidad no encontradas en los datos.")

    def generate_insights(self):
        """Genera recomendaciones basadas en el análisis de los datos"""
        last_close = self.df['Close'].iloc[-1]
        moving_avg = self.df['Moving_Average'].iloc[-1]

        if last_close > moving_avg:
            print("\nRecomendación: El precio de Bitcoin está por encima del promedio móvil. Esto puede indicar una tendencia al alza. Considere evaluar oportunidades de inversión.")
        elif last_close < moving_avg:
            print("\nRecomendación: El precio de Bitcoin está por debajo del promedio móvil. Esto puede ser una señal de precaución o una oportunidad de compra en el corto plazo.")
        else:
            print("\nRecomendación: El precio de Bitcoin está en línea con el promedio móvil. No se observan señales claras; considere monitorear las tendencias futuras.")

class bitcoin_valles_picos:
    """Clase para análisis específico de Bitcoin enfocado en picos y valles"""

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def identify_peaks_and_valleys(self, column: str) -> pd.DataFrame:
        """Identificar picos y valles en una columna dada, devuelve un DataFrame con los puntos"""
        prices = self.data[column].values
        peaks, valleys = [], []

        for i in range(1, len(prices) - 1):
            if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:  # Pico
                peaks.append((self.data.index[i], prices[i]))
            elif prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:  # Valle
                valleys.append((self.data.index[i], prices[i]))

        # Crear DataFrame para visualizar los picos y valles
        return pd.DataFrame(peaks, columns=['Fecha', 'Pico']).merge(
            pd.DataFrame(valleys, columns=['Fecha', 'Valle']), on='Fecha', how='outer'
        )

    def plot_price_with_moving_average_and_peaks(self, price_column: str, window: int = 30):
        """Genera una gráfica del precio con promedio móvil y puntos de picos y valles."""
        self.data['Moving_Avg'] = self.data[price_column].rolling(window=window).mean()
        peaks_valleys = self.identify_peaks_and_valleys(price_column)

        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data[price_column], label="Precio de Cierre")
        plt.plot(self.data.index, self.data['Moving_Avg'], label=f"Promedio Móvil ({window} días)", color='orange')
        plt.scatter(peaks_valleys['Fecha'], peaks_valleys['Pico'], color='green', label='Picos')
        plt.scatter(peaks_valleys['Fecha'], peaks_valleys['Valle'], color='red', label='Valles')
        plt.xlabel("Fecha")
        plt.ylabel("Precio (USD)")
        plt.title("Precio de Cierre de Bitcoin con Promedio Móvil y Picos/Valles")
        plt.legend()
        plt.show()

