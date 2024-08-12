import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados Brutos
data = {
    "Grupo de idade": [
        "100 anos ou mais", "95 a 99 anos", "90 a 94 anos", "85 a 89 anos", "80 a 84 anos",
        "75 a 79 anos", "70 a 74 anos", "65 a 69 anos", "60 a 64 anos", "55 a 59 anos",
        "50 a 54 anos", "45 a 49 anos", "40 a 44 anos", "35 a 39 anos", "30 a 34 anos",
        "25 a 29 anos", "20 a 24 anos", "15 a 19 anos", "10 a 14 anos", "5 a 9 anos",
        "0 a 4 anos"
    ],
    "População feminina(pessoas)": [
        27244, 114859, 385388, 835554, 1465178, 2189593, 3243186, 4288180, 5338555, 
        6149601, 6584190, 7091003, 8291111, 8345458, 7935832, 7842265, 7699157, 7058427, 
        6682215, 6738158, 6243171
    ],
    "População masculina(pessoas)": [
        10570, 50319, 194341, 493649, 1009852, 1657786, 2615350, 3588052, 4605834, 
        5419505, 6014391, 6549109, 7781059, 7827333, 7537285, 7627458, 7767306, 7317515, 
        6992746, 7011282, 6461689
    ]
}

# Criação do 'data'
df = pd.DataFrame(data)

# Impressão dos dados brutos
print(df.head())

# Descrição dos dados
print(df.describe())


# Transformação de dados
df_melted = df.melt(id_vars=["Grupo de idade"], 
                    value_vars=["População feminina(pessoas)", "População masculina(pessoas)"], 
                    var_name="Sexo", 
                    value_name="População")

# Gráfico de barras
plt.figure(figsize=(12, 6))
sns.barplot(x="Grupo de idade", y="População", hue="Sexo", data=df_melted, palette="viridis")
plt.title("Distribuição da População por Faixa Etária e Sexo")
plt.xlabel("Grupo de idade")
plt.ylabel("População")
plt.xticks(rotation=45)
plt.show()


# Medidas descritivas
medidas_descritivas = df_melted.groupby('Sexo')['População'].describe()
print(medidas_descritivas)

# Mediana
mediana_faixa_etaria = df_melted.groupby('Grupo de idade')['População'].median()
print(mediana_faixa_etaria)