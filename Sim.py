# Esse código Python é um script que conta a frequência de uma palavra em um texto. Vou explicar linha por linha:

# 1. `import argparse`: Importa o módulo `argparse`, que é usado para analisar argumentos de linha de comando.
# 2. `parser = argparse.ArgumentParser(description='procurar palavras')`: Cria um objeto `ArgumentParser` chamado `parser`, que será usado para analisar os argumentos passados para o script via linha de comando. O parâmetro `description` fornece uma descrição para o programa.
# 3. `parser.add_argument('--texto', action='store', dest='texto', required=True, help="Diga o texto que você quer ler: ")`: Adiciona um argumento ao `parser`. Este argumento é do tipo string e é designado pelo usuário com a flag `--texto`. O parâmetro `dest` especifica o nome do atributo onde o valor desse argumento será armazenado no namespace retornado por `parse_args()`. `required=True` indica que este argumento é obrigatório. O parâmetro `help` fornece uma mensagem de ajuda para o argumento.
# 4. `parser.add_argument('--palavra', action='store', dest='palavra', required=True, help="Diga a palavra que você quer descobrir a frequência: ")`: Similar ao anterior, mas para a palavra que será contada no texto.
# 5. `arguments = parser.parse_args()`: Analisa os argumentos da linha de comando usando o `parser` configurado anteriormente e armazena os valores no objeto `arguments`.
# 6. `texto = arguments.texto`: Atribui o valor do argumento `texto` ao objeto `texto`.
# 7. `palavra = arguments.palavra`: Atribui o valor do argumento `palavra` ao objeto `palavra`.			
# 8. `lista = []`: Inicializa uma lista vazia para armazenar as posições onde a palavra é encontrada no texto.
# 9. `print("Diretório: {}".format(texto))`: Imprime uma mensagem indicando o diretório do texto que está sendo analisado.
# 10. `arquivo = open(texto, "r")`: Abre o arquivo de texto especificado pelo usuário no modo de leitura (`"r"`).
# 11. `ler = arquivo.read().lower().strip().split(" ")`: Lê o conteúdo do arquivo, converte para minúsculas (`.lower()`), remove espaços em branco extras no início e no final (`.strip()`), e divide o texto em uma lista de palavras usando espaços como delimitador (`.split(" ")`).
# 12. `for i in range(len(ler)):`: Itera sobre os índices da lista `ler`.
# 13. `if ler[i] == palavra:`: Verifica se a palavra na posição atual é igual à palavra especificada pelo usuário.
# 14. `lista.append(i)`: Se a palavra for encontrada, adiciona o índice atual à lista `lista`.
# 15. `print(len(lista))`: Imprime o número de ocorrências da palavra no texto.
# 16. `arquivo.close()`: Fecha o arquivo após a leitura.