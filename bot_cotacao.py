import telebot # Importando a biblioteca do telegram // Comando para ininstalr a biblioteca telebot - pip install pytelegrambotapi
import requests # Importando a biblioteca requests
import json # Importando a biblioteca json

with open('/home/daniel/Documentos/Daniel/Arquivos/bots_telegram_python/tocken_bot_telegram.txt', 'r') as file: # Modo de Leitura 'r'
    TOKEN = str(file.read().rstrip()) # Constante para armazerna o tocken do bot do telegram que está em um rquivo txt

bot = telebot.TeleBot(TOKEN) # Instanciando a classe da biblioteca telebot que vai se conecar com a API de telegram através do token

@bot.message_handler(commands=['dollar']) # Criando um comando para ser digitado ou clicado no bot para execurar alguma função
def dollar(mensagem): # Função para executar no bot quanto for digitado o comando acima
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # fazendo uma requisissão para a api de cotações (retorna um json)
    cotacoes = cotacoes.json() # convertendo json para dicionario do python
    cotacao_dolar = cotacoes['USDBRL']['bid'] # Acessando o valor da cotação na biblioteca
    bot.send_message(mensagem.chat.id, f'R$ {cotacao_dolar}') # Enviando a mensagem para o usuario que solicitou

@bot.message_handler(commands=['euro'])
def euro(mensgem):
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_euro = cotacoes['EURBRL']['bid']
    bot.send_message(mensgem.chat.id, f'R$ {cotacao_euro}')

@bot.message_handler(commands=['bitcoin'])
def bitcoin(mensagem):
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_bitcoin = cotacoes['BTCBRL']['bid']
    bot.send_message(mensagem.chat.id, f'R$ {cotacao_bitcoin}')


def verificar(mensagem): # Função para verificar se o usuario digitou algum caractere no bot (Sempre vai vai retornar True se o usuario digitar qualquer coisa)
    return True

@bot.message_handler(func=verificar) # Verificando se  algum texto foi digitado no bot para fazer a função abaixo funcionar
def responder(mensagem):
    texto = """
    Escolha uma opção para visualizar a cotação da moeda em Reais (Clique no item)
    /dollar 
    /euro 
    /bitcoin  """ # """""" Serve para escrever uma mensagem em varias linhas
    bot.reply_to(mensagem, texto) # repy_to - Responde a mesnagem enviadoa para o bot



bot.polling() # Método para criar um loop infinito no bot (deixar o bot sempre em execução)
