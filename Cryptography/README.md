Name of question : DUMBONE

DESCRIPTION (as per the Icectf webste):

I joined a couple of hacking channels on IRC and I started recieving these strange messages. Someone sent me this image. Can you figure out if there's anything suspicous hidden in it?
-----------------------------------------------------------------------------------------------------------------------
Write up:

In this CRYPTO question we had been given 2 things in the picture garfeld.png

First the ciphered text : "IjgJUO{P_LOUV_AIRUS_GYQUTOLTD_SKRFB_TWNKCFT}"

and a key on the top right of the photo

KEY="07271978"

In the python file i have given the code.
In the code it is basically moving backward the current alphabet with the respective number given in the key.

Note: It is only for the alphabets not for the symbols

For example :
	Ijg will be deciphered as below:
	
	'I' : 'I'-0='I'
	'j'	: 'j'-7='c'
	'g'	: 'g'-2='e'
	

After running the python file the flag appeared :"IceCTF{I_DONT_THINK_GRONSFELD_LIKED_MONDAYS}" 
