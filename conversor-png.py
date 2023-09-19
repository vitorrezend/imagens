from PIL import Image
import os

def converter_webp_para_png(caminho_entrada, caminho_saida):
    # Verifica se o diretório de saída existe, caso contrário, cria-o
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)
    
    # Percorre todos os arquivos no diretório de entrada
    for arquivo in os.listdir(caminho_entrada):
        caminho_arquivo_entrada = os.path.join(caminho_entrada, arquivo)
        if os.path.isfile(caminho_arquivo_entrada) and arquivo.lower().endswith(".webp"):
            # Abre a imagem WebP usando o Pillow
            imagem_webp = Image.open(caminho_arquivo_entrada)
            
            # Converte a imagem para o formato PNG
            nome_arquivo = os.path.splitext(arquivo)[0] + ".png"
            caminho_arquivo_saida = os.path.join(caminho_saida, nome_arquivo)
            imagem_webp.save(caminho_arquivo_saida, "PNG")
            
            print(f"Arquivo convertido: {caminho_arquivo_saida}")

# Exemplo de uso
caminho_entrada = "/home/vitor/Documentos/dalaran/scripts/imagens/webp/sleeves"
caminho_saida = "/home/vitor/Documentos/dalaran/scripts/imagens/webp/sleeves-png"

converter_webp_para_png(caminho_entrada, caminho_saida)
