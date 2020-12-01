

import code as x 

x.create("harshitha",20)
x.create("ttl",50,5800) 
x.read("harshitha")
x.read("ttl")

x.create("harshitha",40)
x.delete("harshitha")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()


