from datetime import datetime
import requests
import threading
import random
import os
import time
import sys


thread = 15
wordlist = "word.txt"

def logo():
    l = '''\033[1m\033[94m
    ----------------------------------------------------------
      _______  _______  _______  __   __  _______  ______   
     |       ||   _   ||       ||  | |  ||       ||    _ |  
     |    _  ||  |_|  ||_     _||  |_|  ||    ___||   | ||  
     |   |_| ||       |  |   |  |       ||   |___ |   |_||_ 
     |    ___||       |  |   |  |       ||    ___||    __  |
     |   |    |   _   |  |   |  |   _   ||   |___ |   |  | |
     |___|    |__| |__|  |___|  |__| |__||_______||___|  |_|
     
                 Coded By SaharAvitan(AttacKit)            
                    attackit.hack@gmail.com
    ----------------------------------------------------------
    '''
    print(l)

def clear():
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
    else:
        os.system("cls")
def progress():
    for i in range(1, 20):
        print("\r\033[1m\033[91m" + "/-\|"[i % 4] + str(int((i / 20.0) * 100)) + "%" + "[" + ("#" * i).ljust(20, " ") + "]", time.sleep(0.1), end="")
        sys.stdout.flush()

clear()
logo()
progress()
clear()
logo()

with open(wordlist, "r") as file:
    lines = file.readlines()

len_lines = len(lines)
print("\033[1m\033[92mWordlist\033[0m: {} | \033[1m\033[92mWordlist size\033[0m: {} | \033[1m\033[92mThreads\033[0m:"
      " {}".format(wordlist,len(lines), thread ))

def target():
    url = "a"
    url = input("\033[1m\033[92mTarget\033[0m (http://example.com) : ")
    http = "http://"
    https = "https://"
    if http in url or https in url:
        url = url + "/"
    else:
        url = "http://" + url + "/"
    try:
        res = requests.get(url)
    except:
        print("Looks like the server is down, check the address")
        url = target()
    return url

url = target()

print("")

t1 = datetime.now()

def per():
    global lines
    global len_lines
    while lines != []:
        min = len(lines) - len_lines
        pres = min / len_lines
        num = int(pres * 100) * -1
        return "{}%".format(num)


def rand():
    try:
        global lines
        if lines == []:
            print("The scan is over")
            exit()
        else:
            word = random.choice(lines)
            lines.remove(word)
            return word[:-1]
    except:
        exit()

def brute(url,t1):
    while True:
        if lines == []:
            exit()
        try:
            payload = rand()
            response = requests.get(url + payload)
            if response.status_code == 200:
                t2 = datetime.now()
                total = t2 - t1
                print("\033[1m\033[92m[ {} ] [{}] |".format(per(),str(total)[:-4]), response.status_code, "| ", url + payload,"\033[0m")
            elif response.status_code == 403:
                t2 = datetime.now()
                total = t2 - t1
                print("\033[1m\033[94m[ {} ] [{}] |".format(per(),str(total)[:-4]), response.status_code, "| ", url + payload,"\033[0m")
        except:
            pass


for i in range(thread):
    try:
        a1 = threading.Thread(target=brute, args=[url, t1])
        a1.start()
    except:
        pass
