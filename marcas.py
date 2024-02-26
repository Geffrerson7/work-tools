import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('mi_archivo.xlsx')
Nombre_Columna="marca"

# Convertir la columna a mayúsculas y reemplazar valores vacíos por 'IBASA'
df[Nombre_Columna] = df[Nombre_Columna].str.upper().fillna('IBASA')

# Reemplazar 'generico' por 'GENÉRICO'
df[Nombre_Columna] = df[Nombre_Columna].replace('generico', 'GENÉRICO')

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('marcas-nuevas.xlsx', index=False)
