from src.loader.carga_datos import DataLoader
from src.preprocessing.preprocessor import Preprocessor
from src.analysis.bitcoin_analisis import BitcoinAnalyzer, bitcoin_valles_picos

def main():
    # Configuración con la ruta relativa del archivo CSV
    data_path = 'data/bitcoin_data.csv'
    
    print("Cargando datos desde el archivo CSV...")
    # Instanciar DataLoader y cargar datos
    data_loader = DataLoader(data_path)
    bitcoin_data = data_loader.load_data()
    
    # Verificar y procesar datos
    if bitcoin_data is not None:
        print("Datos de Bitcoin cargados exitosamente.")
        
        print("\nIniciando preprocesamiento de datos...")
        # Preprocesamiento
        preprocessor = Preprocessor(bitcoin_data)
        bitcoin_data = preprocessor.clean_data()
        print("Limpieza de datos completada.")
        bitcoin_data = preprocessor.filter_columns(['Date', 'Close'])
        print("Filtrado de columnas completado.")
        
        # Instanciar y ejecutar análisis de Bitcoin
        print("\nIniciando análisis de Bitcoin...")
        analyzer = BitcoinAnalyzer(bitcoin_data)
        bitcoin_data = analyzer.calculate_moving_average(window=30)
        print("Promedio móvil calculado.")
        bitcoin_data = analyzer.calculate_volatility()
        print("Volatilidad calculada.")
        
        # Generar gráficos interactivos y recomendaciones
        print("\nGenerando gráficos interactivos...")
        analyzer.plot_interactive_price_trends()
        print("Gráfico de tendencia de precios completado.")
        analyzer.plot_volatility()
        print("Gráfico de volatilidad completado.")
        analyzer.generate_insights()
        print("Recomendaciones generadas.")

        # Análisis avanzado de picos y valles con NumPy
        print("\nIniciando análisis avanzado de picos y valles...")
        advanced_analyzer = bitcoin_valles_picos(bitcoin_data)
        advanced_analyzer.plot_price_with_moving_average_and_peaks('Close', window=30)
        print("Gráfico de picos y valles completado.")
        advanced_analyzer.plot_volatility('Close')
        print("Gráfico de volatilidad avanzado completado.")

    else:
        print("No se pudieron cargar los datos de Bitcoin.")

if __name__ == "__main__":
    main()








