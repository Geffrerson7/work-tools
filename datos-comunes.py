import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("sku.xlsx")

# Obtener los datos de las columnas A y B
columna_a = df["SKU_gef"].tolist()
columna_b = df["SKU_va"].tolist()

# Encontrar los datos comunes
datos_comunes = list(set(columna_a) & set(columna_b))

# Agregar los datos comunes a la columna C
df["SKU"] = pd.Series(datos_comunes)

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel("datos-comunes.xlsx", index=False)
