from socketserver import ThreadingTCPServer, BaseRequestHandler
from threading import Thread
import pickle,time,datetime,os


messages = []	#historico de todas as mensagens enviadas no servidor
temp = []		#1º
os.system("clear")
class Echo(BaseRequestHandler):	#handle function comes from BaseRequestHandler(which includes self.request
					#and self.client_address)

	def handle(self): 
		self.temp = [] #2º
		Thread(target=self.send).start()
		self.username = self.request.recv(1024)	#Receber mensagem codificada(tamanh da mensagem 1024)
		self.username = self.username.decode() # descodificar a mensagem
		print("Got connection from {}:{}".format(self.client_address[0],self.client_address[1])) 
		while True:
			msg = self.request.recv(1024) #Server recebe mensagem do cliente(1024 bytes max)	
			msg = "[{} {}]: {}".format(datetime.datetime.now().strftime("%H:%M:%S"),self.username,msg.decode())
					#linha acima serve para paremeterizar layout das mensagens
			messages.append(msg) #Server adds messagem recebida ao array messages
			print(msg)	# Linha para o servidor consultar mensagens enviados pelos clientes

			'''if not msg:
				print("LINHA DO \"IF NOT MSG\" A FUNCIONAR")
				break'''


	def send(self):

		global temp, messages  #3º
		while 1:

			if len(self.temp) != len(messages):

				data_string = pickle.dumps(messages)
				self.request.send(data_string)
				self.temp = [item for item in messages]

if __name__ == "__main__":
	try:
		serv = ThreadingTCPServer(("",9999), Echo) #
		serv.serve_forever()	#Listening to incoming requests until shutdown
	except:
		serv.shutdown()


## CORRIGIR BUG DE SAIDA NO SERVIDOR
# porque e que o  servidor recebe username e nao manda para os outros users?
# Reconhecer Objecto "temp"
