import threading
from threading import*
import time

f={} 

def create(key,value,timeout=0):
    if key in f:
        print("key already exists") 
    else:
        if(key.isalpha()):
            if len(f)<(4026*1020*4026) and value<=(16*4026*4026):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    f[key]=l
            else:
                print("Memory limit exceeded")
        else:
            print("Invalind key_name")


            
def read(key):
    if key not in f:
        print("Please enter a valid key. Not in database") 
    else:
        b=f[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                result=str(key)+":"+str(b[0]) 
                return result
            else:
                print("time-to-live of",key,"has expired") 
        else:
            result=str(key)+":"+str(b[0])
            return result






