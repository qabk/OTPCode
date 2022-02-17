# su dung cac thu vien cua python de tao ham sinh otp
import time, hashlib, hmac
def truncate(hmac_res):
    offset = int(hmac_res[38:],16)&0xf
    return int(hmac_res[offset*2:offset*2+8],16)%10**6

password = "qA090296"
pivot = 1607048354.1137462 # thoi gian server dong bo voi client
"""
def truncate(hmac_res):
    offset = int(hmac_res[38:],16)&0xf
    return int(hmac_res[offset*2:offset*2+8],16)%10**6
"""
def otp_generate(mess):
    t = time.time()
    intput_key =  str(int((t-pivot)/30))
    h = hmac.new(key=bytes(intput_key.encode('utf-8')), msg=bytes(mess.encode('utf-8')), digestmod=hashlib.sha1)
    res = str(truncate(h.hexdigest()))
    return '0'*(6-len(res))+ res
def main():
    print("thay go get de lay ma otp")
    print("thay go end de ket thuc chuong trinh")
    while(True):
        x = input()
        if(x == "get"):
            print(otp_generate(password))
        if(x == "end"):
            break
if __name__ == "__main__":
    main()