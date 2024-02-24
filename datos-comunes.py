import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("mi_archivo.xlsx")

# Obtener los datos de las columnas A y B
columna_a = df["Columna C"].tolist()
columna_b = df["Columna D"].tolist()

# Encontrar los datos comunes
datos_comunes = list(set(columna_a) & set(columna_b))

# Agregar los datos comunes a la columna C
df["Columna E"] = pd.Series(datos_comunes)

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel("datos-comunes.xlsx", index=False)
