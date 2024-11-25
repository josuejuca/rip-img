import os
from PIL import Image

def reduzir_tamanho_imagens(diretorio, tamanho_max_mb=2):
    # Criar a pasta "rip" dentro do diretório atual
    pasta_saida = os.path.join(diretorio, "rip")
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Listar todas as imagens no diretório
    imagens = [f for f in os.listdir(diretorio) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

    for imagem in imagens:
        caminho_imagem = os.path.join(diretorio, imagem)
        caminho_saida = os.path.join(pasta_saida, imagem)

        # Abrir a imagem
        img = Image.open(caminho_imagem)

        # Ajustar qualidade para alcançar o tamanho máximo permitido
        qualidade = 95
        img_format = "JPEG" if img.format != "PNG" else "PNG"  # Determinar o formato original

        while True:
            # Salvar a imagem com a qualidade ajustada
            img.save(caminho_saida, format=img_format, quality=qualidade)
            
            # Verificar o tamanho do arquivo salvo
            tamanho = os.path.getsize(caminho_saida) / (1024 * 1024)  # Tamanho em MB
            
            if tamanho <= tamanho_max_mb or qualidade <= 10:
                break
            
            qualidade -= 5  # Reduzir a qualidade gradualmente

        print(f"Imagem: {imagem} | Tamanho final: {tamanho:.2f} MB | Qualidade final: {qualidade}")

    print(f"Imagens redimensionadas salvas em: {pasta_saida}")

# Definir o diretório atual
diretorio_atual = os.getcwd()

# Executar a função
reduzir_tamanho_imagens(diretorio_atual)
