import requests
import os
from zipfile import ZipFile


urls = {
    "Anexo_I.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN606_RN607.pdf",
    "Anexo_II.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/AnexoII_DUT2021_RN465.2021_RN627.2025.pdf"
}

# Pasta para salvar os PDFs
output_folder = "anexos"
os.makedirs(output_folder, exist_ok=True)

# Baixar os PDFs
for filename, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(output_folder, filename), 'wb') as f:
            f.write(response.content)
        print(f"{filename} baixado com sucesso.")
    else:
        print(f"Falha ao baixar {filename}.")

# Compactar os PDFs em um único arquivo ZIP
zip_filename = "anexos.zip"
with ZipFile(zip_filename, 'w') as zipf:
    for filename in urls.keys():
        filepath = os.path.join(output_folder, filename)
        if os.path.exists(filepath):
            zipf.write(filepath, filename)
            print(f"{filename} adicionado ao {zip_filename}.")
        else:
            print(f"{filename} não encontrado e não foi adicionado ao {zip_filename}.")

print(f"Processo concluído. Arquivos compactados em {zip_filename}.")