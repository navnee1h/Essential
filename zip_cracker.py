
'''imports'''
import zipfile


count = 1

#                    wordlist
with open('rockyou.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:                        #zipfile
            with zipfile.ZipFile('Certified Ethical Hacker CEH v11 PDF.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass


