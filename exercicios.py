"""Exercício 1: Verificação de Qualidade de Dados Você está analisando um conjunto de dados de vendas e precisa garantir  que todos os registros tenham valores positivos para `quantidade` e `preço`. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário."""

#criando as variáveis:
# quantidade = 40
# preco = 20

#validação do positivo
# if quantidade > 0 and preco > 0:
#     print("valores validos")
# else:
#     print("valores inválidos")


"""Exercício 2: Classificação de Dados de Sensor Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 
'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'
"""

# temperatura = int(input("Escreva um valor para temperatura: "))

# if temperatura < 18:
#     print("temperatura baixa")
# elif 18 <= temperatura <= 26:
#     print("temperatura normal")
# else:
#     print("temperatura alta")



"""Exercício 3: Filtragem de Logs por Severidade - Você está analisando logs de uma aplicação e precisa filtrar mensagens  com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, escreva um programa que imprima a mensagem se a severidade for 'ERROR'."""

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

"""Exercício 4: Validação de Dados de Entrada - Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado."""

# idade = int(input("Coloque a sua idade"))
# email = str(input("Digite o seu email"))

# if not 18 <= idade <= 65:
#     print("Idade fora do intervalo permitido")
# elif "@" not in email or "." not in email:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")

"""Exercício 5: Detecção de Anomalias em Dados de Transações - Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se 
o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita."""

# transacao = {'valor': 10000, 'hora': 20}

# if transacao['valor'] > 10000:
#     print("Valor suspeito")
# elif 9 < transacao['hora'] > 18:
#     print("Horário suspeito")
# else:
#     print("Trasação aprovada")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "hoje e nossa segunda aula do bootcamp, bootcamp de python"

# novo_texto = texto.replace(",","")

# palavras = novo_texto.split()

# contagem_de_palavras = {}

# Eu quero percorrer todas as palavras dentro de palavras e checar se ela já está no meu contagem de palavras.

# for palavra in palavras:
#     if palavra in contagem_de_palavras:
#         contagem_de_palavras[palavra] = +1
#     else:
#         contagem_de_palavras[palavra] = 1

"""Exercício 7. Normalização de Dados - Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1."""

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

"""Exercício 8. Filtragem de Dados Faltantes - Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando"""

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuario (singular) é uma variável temporária que representa o elemento atual do loop. Essa variável é definida no momento em que o loop é iniciado pela compreensão de lista. 
# Para cada iteração do loop, usuario representa um dicionário diferente da lista usuarios.

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)

"""Exercício 9. Extração de Subconjuntos de Dados Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares."""

# numeros = range(1, 11)
# numeros_pares = [x for x in numeros if x % 2 == 0]
# print(numeros_pares)

"""Exercício 10. Agregação de Dados por Categoria Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria."""

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}

# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor
# print(total_por_categoria)

### Exercícios com WHILE

"""Exercício 11. Leitura de Dados até Flag Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida."""

# dados = []
# entrada = ""  # Inicializa a variável entrada como uma string vazia

# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":
#         dados.append(entrada)  # Adiciona o valor digitado à lista dados, se não for "sair"

# print("Você digitou os seguintes valores:", dados)


"""Exercício 12. Validação de Entrada - Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida."""

# dados = []
# numeros = int(input("Digite um número entre 1 e 10: "))

# while numeros  < 1 or numeros > 10:
#     print("Número fora do intervalo")
#     numeros = int(input("Digite um número entre 1 e 10: "))
# print("Número válido")


"""Exercício 13. Consumo de API Simulado - Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas."""

# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")
#     # Aqui iria o código para processar os dados da página
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")

"""### Exercício 14. Tentativas de Conexão - Simular tentativas de reconexão a um serviço com um limite máximo de tentativas."""

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")

"""Exercício 15. Processamento de Dados com Condição de Parada - Processar itens de uma lista até encontrar um valor específico que indica a parada."""

itens = [1, 2, 3, "parar", 4, 5]

i = 0 # Iniciar o Processamento - Você começa na posição inicial da fila (ou seja, o início da lista), representado pela variável i que inicia em 0.
while i < len(itens): # Esta linha diz: "Continue fazendo isso enquanto i (sua posição atual na fila) for menor que o comprimento da lista (len(itens) significa o número total de itens na lista)."
    if itens[i] == "parar": # Para cada pessoa (item) na fila, você verifica se ela está segurando o cartão "parar".
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}") # Se a pessoa (item) não estiver segurando o cartão "parar", você entrega o convite (processa o item).
    i += 1 # Após entregar um convite, você avança para a próxima pessoa na fila.