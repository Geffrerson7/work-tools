import pandas as pd

# Cargar el archivo Excel
archivo_excel = "CATEGORIA.xlsx"
df = pd.read_excel(archivo_excel)


# Definir la función para asignar los valores según las palabras clave
def asignar_valores(row):
    keywords = str(row["_Keywords"]).lower()  # Convertir a minúsculas para comparación
    if "comida" in keywords and ("gato" in keywords or "gatos" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 368
        row["_CategoryName"] = "Comida para gatos"
    elif "paté" in keywords and (
        "gato" in keywords
        or "gatos" in keywords
        or "gatitos" in keywords
        or "gatito" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 368
        row["_CategoryName"] = "Comida para gatos"
    elif "paté" in keywords and (
        "perro" in keywords
        or "perros" in keywords
        or "cachorros" in keywords
        or "cachorro" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif "comida" in keywords and ("gatitos" in keywords or "gatito" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 368
        row["_CategoryName"] = "Comida para gatos"
    elif "comida" in keywords and ("cachorros" in keywords or "cachorro" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif "comida" in keywords and ("perro" in keywords or "perros" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif "alimento" in keywords and ("perro" in keywords or "perros" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif ("snacks" in keywords or "snack" in keywords) and (
        "perro" in keywords or "perros" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif ("snacks" in keywords or "snack" in keywords) and (
        "cachorro" in keywords or "cachorros" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 369
        row["_CategoryName"] = "Comida para perros"
    elif "alimento" in keywords and ("gato" in keywords or "gatos" in keywords):
        row["_DepartamentId (Not changeable)"] = 356
        row["_DepartamentName"] = "Alimentos"
        row["_CategoryId"] = 368
        row["_CategoryName"] = "Comida para gatos"
    elif (
        "collar" in keywords
        or "bandana" in keywords
        or "collares" in keywords
        or "bandanas" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 355
        row["_DepartamentName"] = "Accesorios"
        row["_CategoryId"] = 360
        row["_CategoryName"] = "Collares y bandanas"
    elif "juguete" in keywords and ("perro" in keywords or "perros" in keywords):
        row["_DepartamentId (Not changeable)"] = 358
        row["_DepartamentName"] = "Juguetes"
        row["_CategoryId"] = 375
        row["_CategoryName"] = "Juguetes para perros"
    elif "juguete" in keywords and ("gato" in keywords or "gatos" in keywords):
        row["_DepartamentId (Not changeable)"] = 358
        row["_DepartamentName"] = "Juguetes"
        row["_CategoryId"] = 374
        row["_CategoryName"] = "Juguetes para gatos"
    elif "rascador" in keywords or "rascadores" in keywords:
        row["_DepartamentId (Not changeable)"] = 358
        row["_DepartamentName"] = "Juguetes"
        row["_CategoryId"] = 374
        row["_CategoryName"] = "Juguetes para gatos"
    elif "desenredante" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 385
        row["_CategoryName"] = "Shampoo y acondicionadores"
    elif "shampoo" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 385
        row["_CategoryName"] = "Shampoo y acondicionadores"
    elif "acondicionador" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 385
        row["_CategoryName"] = "Shampoo y acondicionadores"
    elif "colonia" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 379
        row["_CategoryName"] = "Colonias y perfumes"
    elif "perfume" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 379
        row["_CategoryName"] = "Colonias y perfumes"
    elif "antipulga" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 388
        row["_CategoryName"] = "Antipulgas y Antiparásitos"
    elif "antiparasito" in keywords or "antiparásito" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 388
        row["_CategoryName"] = "Antipulgas y Antiparásitos"
    elif "pulgas" in keywords or "antiparásitos" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 388
        row["_CategoryName"] = "Antipulgas y Antiparásitos"
    elif "arena" in keywords or "arenero" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 378
        row["_CategoryName"] = "Areneros y arena para gatos"
    elif "suplemento" in keywords or "suplementos" in keywords or "vitamínico" in keywords or "vitamínicos" in keywords:
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 386
        row["_CategoryName"] = "Vitaminas y suplementos"
    elif (
        "cepillo" in keywords
        or "peine" in keywords
        or "cortadora" in keywords
        or "cepillos" in keywords
        or "peines" in keywords
        or "cortadoras" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 359
        row["_DepartamentName"] = "Salud e higiene"
        row["_CategoryId"] = 378
        row["_CategoryName"] = "Cortadoras, peines y cepillos"
    elif (
        "correa" in keywords
        or "arnés" in keywords
        or "pechera" in keywords
        or "correas" in keywords
        or "arneses" in keywords
        or "pecheras" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 355
        row["_DepartamentName"] = "Accesorios"
        row["_CategoryId"] = 361
        row["_CategoryName"] = "Correas, arneses y pecheras"
    elif (
        "plato" in keywords
        or "platos" in keywords
        or "bebedero" in keywords
        or "dispensador" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 355
        row["_DepartamentName"] = "Accesorios"
        row["_CategoryId"] = 363
        row["_CategoryName"] = "Platos y bebederos"
    elif (
        "transportador" in keywords
        or "kennel" in keywords
        or "bolso" in keywords
        or "transportadores" in keywords
        or "kennels" in keywords
        or "bolsos" in keywords
    ):
        row["_DepartamentId (Not changeable)"] = 355
        row["_DepartamentName"] = "Accesorios"
        row["_CategoryId"] = 362
        row["_CategoryName"] = "Kennels, bolsos y transportadores"
    return row


# Aplicar la función a cada fila del DataFrame
df = df.apply(asignar_valores, axis=1)

# Reordenar las columnas según el requisito
df = df[
    [
        "_DepartamentId (Not changeable)",
        "_DepartamentName",
        "_CategoryId",
        "_CategoryName",
        "_Keywords",
    ]
]

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel("categoria-final.xlsx", index=False)
