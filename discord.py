from dhooks import Webhook, File
from io import BytesIO
import requests
import time
import os

hook = Webhook('https://discord.com/api/webhooks/932280159262883872/k2UE-y_B0yUqz2njUPXE8cqYJbHPmn7MSpGc85Auczdk4JJdMC0seyHyY49B3d62iLhn')
#                   webhook link


exit="exit"

def img_link():	
	print("\n")
	link=input("Enter the image link : ")
	if link == exit :
		os.system("clear")
		main()
	else :
	
		os.system("clear")
		image = link.replace("/", " ").split().pop()
		print("Sending...... ")
		response = requests.get(link)
		file = File(BytesIO(response.content), name=image)
		hook.send(file=file)
		os.system("clear")
		print("File sent! ")
	
def snd_file():
	print("\n")
	eg=input("Drag here any file ! :" ).strip()
	if eg == exit :
		os.system("clear")
		main()
	else :
		eg = eg.replace("'", '')
		name= eg.replace("/", " ")
		name = name.split()
		name= name.pop()
		name= name.replace("'", " ")
		#print(name)
		file = File(eg, name=name)  # optional name for discord
		os.system("clear")
		print("Sending...... ")
		hook.send(file=file)
		print("Operation Successful !")
	
	
def snd_txt():	
	while (1==1):
		print("\n")
		data=input("Type your text : ")
		if data == "exit":
			os.system("clear")
			main()
			break
		os.system("clear")
		print("Sending...... ")
		hook.send(data)
		os.system("clear")
		#print("Message sent successfully !",)
		print("Message sent! " + '  : ' + data)
		
#snd_txt()
#snd_file()
#img_link()


def main():
	
	loop = True
	
	#show options here
	print("|----------------------------------|")
	print("|    1) For sending text messages  |")
	print("|    2) For sending files          |")
	print("|    3) For send files from web    |")
	print("|__________________________________|\n")
	while loop == True:
		a="1"                #asking number
		b="2"		     #asking number
		c="3" 		     #asking number
		d="clear"
	
		inputt =input("Choose a number : ")
		#os.system("clear")
		if inputt == a :
			#print("You choose : snd_txt ")
			snd_txt()
			break
		elif inputt == b:
			#print("You choose : snd_file ")
			snd_file()
			break
		elif inputt ==c:
			#print("You chooose : img_link")
			img_link()
			break
		elif inputt == exit:
			os.system("clear")
			break
		else :
			print("Type Error!")

main()
