# importando as bibliotecas para configuração do Twitter
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# cadastrando as chaves

key = "Exemplo"
secretKey = "Exemplo"
token = "Exemplo"
tokenSecret = "Exemplo"

# Definindo um arquivo de saída para armazenar os tweets coletados
data = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
saida = open(f'./logs/tweetsColetados.txt_{data}', 'w')

#implementar uma classe para conexão com Twitter

class MinhaEscuta(StreamListener): 
    #este procedimento chamamos de Herança, pois a classeMinha Escuta extende a classe StreamLIstneter
    def on_data(self, data):
        
        itemString = json.dumps(data)
        saida.write(itemString + '\n')
        return True
    def on_error(self, status):
        print(status)

data = datetime.now().strftime("%Y-&m-%d-%H-%M-%S")
    
#############################
#iniciando a função:

if __name__ == '__main__':
    l = MinhaEscuta()
    auth = OAuthHandler(key,secretKey)
    auth.set_access_token(token,tokenSecret)
    
    stream = Stream(auth, l)
    
    stream.filter(track=['Bolsonaro'])
