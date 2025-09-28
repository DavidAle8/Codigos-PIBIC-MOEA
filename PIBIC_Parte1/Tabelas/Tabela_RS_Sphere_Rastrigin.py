import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

#"Meu Drive/Colab Notebooks/Arqs txt/HC_Sphere"

p_e_r = [(0.10, 0.1, 1000), (0.50, 1, 3000), (1, 100, 5000)]
iteracaoes = [1000, 10000, 50000]

configuracoes = []

medias_sp = []
desvios_sp = []

medias_rt = []
desvios_rt = []




caminhos_arquivos_sphere = [

    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/1-RS_Sphere_p=0.10_r=0.1_t=1000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/1-RS_Sphere_p=0.50_r=1_t=3000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/1-RS_Sphere_p=1_r=100_t=5000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/2-RS_Sphere_p=0.10_r=0.1_t=1000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/2-RS_Sphere_p=0.50_r=1_t=3000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/2-RS_Sphere_p=1_r=100_t=5000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/3-RS_Sphere_p=0.10_r=0.1_t=1000_i=50000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/3-RS_Sphere_p=0.50_r=1_t=3000_i=50000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Sphere/3-RS_Sphere_p=1_r=100_t=5000_i=50000.txt",
]


caminhos_arquivos_rastrigin = [

    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/1-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/1-RS_Rastrigin_p=0.50_r=1_t=3000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/1-RS_Rastrigin_p=1_r=100_t=5000_i=1000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/2-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/2-RS_Rastrigin_p=0.50_r=1_t=3000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/2-RS_Rastrigin_p=1_r=100_t=5000_i=10000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/3-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=50000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/3-RS_Rastrigin_p=0.50_r=1_t=3000_i=50000.txt",
    "/content/drive/MyDrive//Colab Notebooks/Arqs txt/RS_Rastrigin/3-RS_Rastrigin_p=1_r=100_t=5000_i=50000.txt",
]




def prenchendo_configuracoes(iteracao, lista_pr, lista_config):

    for i in iteracao:

        for p, r, t in lista_pr:
            config = f"iteração = {i} p = {p} r = {r} t = {t}"

            lista_config.append(config)



def prencher_media_desvio(caminhos, lista_medias, lista_desvios):

    for arquivo in caminhos:

        with open(arquivo, "r") as f:

            valores = [float(linha.strip()) for linha in f.readlines()]

            calc_media = pd.Series(valores).mean()
            calc_desvio = pd.Series(valores).std()

            lista_medias.append(calc_media)
            lista_desvios.append(calc_desvio)




prenchendo_configuracoes(iteracaoes, p_e_r, configuracoes)

prencher_media_desvio(caminhos_arquivos_sphere, medias_sp, desvios_sp)
prencher_media_desvio(caminhos_arquivos_rastrigin, medias_rt, desvios_rt)


resultado_tabela = {

    "Configurações": configuracoes,
    "Média Sphere-RS": medias_sp,
    "Média Rastrigin-RS": medias_rt,
    "DP Sphere-RS": desvios_sp,
    "DP Rastrigin-RS": desvios_rt
}

tabela_df = pd.DataFrame(resultado_tabela)
display(tabela_df)