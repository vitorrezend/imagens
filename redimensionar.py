import sys
from PIL import Image

try:
    # Verifica se o número correto de argumentos da linha de comando foi fornecido
    if len(sys.argv) != 2:
        raise ValueError("Uso incorreto. Sintaxe: python nome_do_script.py largura_desejada")

    # Nome do arquivo de entrada e saída
    arquivo_entrada = "promo-image.jpg"
    arquivo_saida = "new-promo.jpg"
    
    # Largura desejada para o arquivo de saída
    largura_desejada = int(sys.argv[1])

    # Abra a imagem de entrada
    imagem = Image.open(arquivo_entrada)

    # Calcule a nova altura proporcional
    largura_imagem = imagem.size[0]
    altura_imagem = imagem.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_desejada = int((altura_imagem * percentual_largura))

    # Redimensione a imagem (com antialiasing padrão)
    imagem = imagem.resize((largura_desejada, altura_desejada))

    # Salve a imagem redimensionada com o nome de saída
    imagem.save(arquivo_saida)
    print(f"Imagem redimensionada e salva como {arquivo_saida}")

except FileNotFoundError:
    print("Erro: O arquivo de entrada não foi encontrado.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
