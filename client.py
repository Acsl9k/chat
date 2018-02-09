import socket,pickle,os
from threading import Thread
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = str(input("Insira o ip do servidor"))
s.connect(("127.0.0.1",9999))

def receber():		#A funçao receber() recebe novo array de dados junta a esse->
					#array a variavel data, limpa o ecra e manda toda a informaçao para o ecra
	while True:
		data = s.recv(1024)    #receber mensagem codificada, 
				#variavel data contem toda a informaçao dita no chat
		data = pickle.loads(data)	#encapsular dados
		print(data)
		os.system("clear")
		for item in data:
			print(item)


def enviar():
	try:
		msg = input(">>") #escrever mensagem RAW
	except msg=='/exit':
		s.shutdown()
		s.close()

	s.send(msg.encode()) # codificar mensagem
	time.sleep(0.1) #required line for ">>" to be printed


username = "axel" # input("Enter your username: ")
Thread(target=receber).start()	#executar thread da funçao receber
				#mandar para backgroudn funçao receber

s.send(username.encode()) #manda o username para o servidor
time.sleep(0.1)


while True:
	enviar()
