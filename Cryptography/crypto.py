#python3
#Usage : In the terminal go to current directory and type "python3 crypto.py"
x="IjgJUO{P_LOUV_AIRUS_GYQUTOLTD_SKRFB_TWNKCFT}"
r="07271978"
s=''
w=0
for i in range(len(x)):
	q=ord(x[i])
	if((q>=97 and q<=122) or (q>=65 and q<=90)):
		e=q-int(r[w])
		if((e<65)):
			e=91-(65-e)

		s+=chr(e)
		w+=1
		if(w>7):
			w=0
	else:
		s+=x[i]
print(s)

#Flag :IceCTF{I_DONT_THINK_GRONSFELD_LIKED_MONDAYS}
