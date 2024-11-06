import pandas as pd

class Preprocessor:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        """Limpia los datos eliminando duplicados y manejando valores nulos"""
        print("Iniciando limpieza de datos...")
        self.df = self.df.drop_duplicates()  # Eliminar duplicados
        self.df = self.df.fillna(0)          # Rellenar valores nulos con 0
        print("Limpieza de datos completada.")
        return self.df

    def filter_columns(self, columns):
        """Filtra el DataFrame para conservar solo las columnas necesarias"""
        print("Filtrando columnas necesarias...")
        self.df = self.df[columns]
        print("Filtrado de columnas completado.")
        return self.df
