import pandas as pd

def unique_column_values_to_excel(input_file_path, column_name, output_file_path):
    # Leer el archivo Excel
    df = pd.read_excel(input_file_path)
    
    # Obtener los valores únicos de la columna especificada
    unique_values = df[column_name].unique()
    
    # Crear un DataFrame con los valores únicos
    unique_df = pd.DataFrame({column_name: unique_values})
    
    # Guardar los valores únicos en un nuevo archivo Excel
    unique_df.to_excel(output_file_path, index=False)

# Ruta del archivo Excel de entrada y salida, y nombre de la columna
input_file_path = "marcas2.xlsx"
output_file_path = "valores_unicos.xlsx"
column_name = "marca"

# Llamar a la función para obtener y guardar los valores únicos en Excel
unique_column_values_to_excel(input_file_path, column_name, output_file_path)

print("Valores únicos guardados en '{}'.".format(output_file_path))