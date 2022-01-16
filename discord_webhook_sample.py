from dhooks import Webhook
'''
hook= Webhook("https://discord.com/api/webhooks/932280159262883872/k2UE-y_B0yUqz2njUPXE8cqYJbHPmn7MSpGc85Auczdk4JJdMC0seyHyY49B3d62iLhn")
data = input("enter something : ")
hook.send(data)'''
########

def send_data():
	hook= Webhook("https://discord.com/api/webhooks/838769118927781938/vZlNI9fl65xd_BsKnAusUVXiz1Ko8y6tSXfgFARvcmPRZFhn3yjKdBtMCDFo88ub6QmW")
	hook.send(data)
	
while (1==1):
	data=input("Enter something : ")
	if data == "exit":
		break
	send_data()
