import pandas as pd
from IPython.display import display # type: ignore

vendas = {
    'data': ['16/02/2001', '14/10/2015'],
    'valor': [500, 300],
    'produto': ['feijao', 'macarrao'],
    'quantidade': [50, 70]
}

vendas_df = pd.DataFrame(vendas)

display(vendas_df)







import pandas as pd
import glob

# Listar os arquivos que seguem o padrão especificado
arquivos = glob.glob("*.txt")

# Criar listas para armazenar os resultados
configuracoes = []
medias = []
desvios = []

# Processar cada arquivo
for arquivo in arquivos:
    # Extrair p, r e iteração do nome do arquivo
    partes = arquivo.split("_")
    p = float(partes[2].split("=")[1])
    r = float(partes[3].split("=")[1])
    iteracao = int(partes[4].split("=")[1].split(".")[0])

    # Ler os valores do arquivo
    with open(arquivo, "r") as f:
        valores = [float(linha.strip()) for linha in f.readlines()]

    # Calcular média e desvio padrão
    media = pd.Series(valores).mean()
    desvio = pd.Series(valores).std()

    # Armazenar os resultados
    configuracoes.append(f"Iteração = {iteracao}\np = {p}\nr = {r}")
    medias.append(media)
    desvios.append(desvio)

# Criar DataFrame com os resultados
df_resultado = pd.DataFrame({
    "Configuração": configuracoes,
    "Média HC-Sphere": medias,
    "Desvio Padrão HC-Sphere": desvios
})

# Exibir a tabela
print(df_resultado)
