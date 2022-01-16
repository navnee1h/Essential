import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import time

'''     in list.txt

        9539858340
        9539858341
        9539858342
        9539858343
        9539858344
        9539858345
        9539858346
        9539858347
        9539858348
        9539858349
'''

f=open("list.txt","r")
read=f.readlines()
for l in (read):
    time.sleep(0.1)
    #print(l)
    f.close
    #print(l)

        ###############################
    nm = "+91"

    a = (nm + str(l))
    time.sleep(0.1)
    # print(a)
    phonenumber = phonenumbers.parse(a)
    b = geocoder.description_for_number(phonenumber, "en")
    d=carrier.name_for_number(phonenumber,"en")
    c = "India"
    if b == c:
        print("True  " + str(l) + d)
        fo = open("output.txt", "a")
        fo.write(str(l))
        fo.close()
    else:
        print("False")

#print(carrier.name_for_number(phnmbr,"en"))
