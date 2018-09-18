<b>Name of the Question: LOCKED OUT(250)</b><br>
<b>DESCRIPTION<br>
This is a fancy looking lock, I wonder what would happen if you broke it open?</b>
<br>
<br>
In this question we have to crack the password so first i checked the functions in the gdb.The functions were :<br><br>
0x00000590  strcmp@plt<br>
0x000005a0  printf@plt<br>
0x000005b0  strcspn@plt<br>
0x000005c0  free@plt<br>
0x000005d0  fgets@plt<br>
0x000005e0  getegid@plt<br>
0x000005f0  puts@plt<br>
0x00000600  system@plt<br>
0x00000610  strlen@plt<br>
0x00000620  __libc_start_main@plt<br>
0x00000630  __strdup@plt<br>
0x00000640  memfrob@plt<br>
0x00000650  setresgid@plt<br>
0x00000660  __cxa_finalize@plt<br>
0x00000668  __gmon_start__@plt<br>
0x00000670  main

<br>
I noticed that strcmp is used in program so i first searched in the strings of the file but
there was nothing that validates the key.That means it is dynamically generating string and comparing it.
<br>
Then instead of using gdb i used <b>ltrace</b> and saw that in strcmp my string is compared to "aXat9r45UtyMjw4i5Wh8swVWmEg3vAbW" 
<br>

![image](https://user-images.githubusercontent.com/43247883/45688976-6466f380-bb70-11e8-9c02-be785c8ad780.png)

<br>
so first i thought that i have found the password !! but when i entered it in executable file it says key failed!!!!<br>
So i again used ltrace and this time i entered "aXat9r45UtyMjw4i5Wh8swVWmEg3vAbW" in key.Now this time strcmp was returning  : -90 !!
<br>

![image](https://user-images.githubusercontent.com/43247883/45688880-2bc71a00-bb70-11e8-8a97-199505fe5c15.png)


<br>
This resulted that the string is not complete password, there are more letters in it.And -90 indicates the alphabet : Z as it's ascii is 90 so that means our new string is "aXat9r45UtyMjw4i5Wh8swVWmEg3vAbWZ" and again i got some other negative integer in ltrace when i  entered new string.<br>
So i made a python script that collects the integer and add to the string and then again calls the ltrace untill strcmp return 0.<br>

![image](https://user-images.githubusercontent.com/43247883/45689070-9e37fa00-bb70-11e8-81a3-00d249c015cf.png)

<br>
<b>NOTE : YOU CAN FIND THIS PYTHON FILE IN THE SAME REPOSITORY WITH NAME "solution.py"</b><br>
So the final String i got was "aXat9r45UtyMjw4i5Wh8swVWmEg3vAbWZaijTWP8"
<br>
I entered the String in password and entered the shell.Then opened the flag.txt and got the flag.
<br>
<b>FLAG</b> : IceCTF{you_m3ddling_k1ds}
