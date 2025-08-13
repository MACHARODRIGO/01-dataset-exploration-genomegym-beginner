import pandas as pd

# Cargar el dataset
df = pd.read_csv("dna_sequences.csv")

# Mostrar cantidad de secuencias y primeras filas
print(f" Total de secuencias: {len(df)}\n")
print(" Primeras secuencias:")
print(df.head())

# Agregar columna con longitud
df["length"] = df["sequence"].apply(len)

# Calcular estadísticas de longitud
print("\n Estadísticas de longitud:")
print(df["length"].describe())

# Mostrar secuencias más largas que el promedio
mean_len = df["length"].mean()
print("\n Secuencias más largas que el promedio:")
print(df[df["length"] > mean_len])
