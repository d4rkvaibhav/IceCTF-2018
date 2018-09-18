from pwn import *
q="aXat9r45UtyMjw4i5Wh8swVWmEg3vAbW"
flag=0
while(flag==0):
	t='printf '+ str(q)+'|ltrace /home/vaibhav/Downloads/./lock'
	r= process(t, shell=True)
	s=r.recvuntil("free")
	s=s.split()
	if(int(s[-2])!=0):
		q+=chr(abs(int(s[-2])))
	else:
		flag=1

print("PASSWORD :" ,q)