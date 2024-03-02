import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("datos-comunes.xlsx")

# Obtener los datos de las columnas SKU_gef y SKU_va
columna_va = df["SKU_va"].tolist()
columna = df["SKU"].tolist()

# Encontrar los datos que están en la columna SKU_va pero no en SKU
datos_en_va= list(set(columna_va).difference(columna))

# Guardar los datos encontrados en un nuevo archivo Excel
df_resultado = pd.DataFrame({"SKU_solo_va": datos_en_va})
df_resultado.to_excel("datos_en_va.xlsx", index=False)
