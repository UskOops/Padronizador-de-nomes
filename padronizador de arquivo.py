#created by https://github.com/octaviolage commented and modify by https://github.com/UskOops 
import os # Importa o módulo os para acessar o sistema operacional
path = 'C:\\temp' # Define o caminho do diretório
files = os.listdir(path) # Lista os arquivos do diretório

for file in files: # Percorre a lista de arquivos
  if file[-27: -17] == file[-14: -4]: # Verifica se o nome do arquivo é igual ao nome do arquivo original
    old_name = path + '\\' + file # Cria o nome do arquivo antigo
    new_name = old_name.split('_a_')[0].replace('temp', 'temp2') + '.' + old_name.split('.')[1] # Define o novo nome do arquivo
    os.rename(old_name, new_name) # Renomeia o arquivo
  else:
    print('File: ' + file) # Imprime o nome do arquivo