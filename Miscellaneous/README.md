<b>ANTICAPTCHA</b> : 250 points <br>

<b>Description:</b><br>
Wow, this is a big captcha. Who has enough time to solve this? Seems like a lot of effort to me!


So in this challenge we have been given a lot of questions and by looking at the first time i thought i have to solve all the questions to get the flag and all questions were looking similar either to fing gcd of 2 number or tell the nth word or to tell number is prime or not.

This is the image of the website having questions:
<a href="https://drive.google.com/open?id=1cvXYFnLKrfmjdjefDrDFY7LTksUUKdoi"><img src="https://drive.google.com/open?id=1cvXYFnLKrfmjdjefDrDFY7LTksUUKdoi" style="width: 300px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

![](https://drive.google.com/open?id=1cvXYFnLKrfmjdjefDrDFY7LTksUUKdoi)

But when i did not answer any question and submitted it, it displayed messages "You got 6 worng!" which gave me a hint that there are only 6 questions that are been evaluating so i once again saaw the questions and then i saw few questions that were completely different so to find these question i used <b>Browser automation using selenium inn  python</b>.I have attached a python3 implemention of it.  <b> (File name : sel.py)</b>
![](https://drive.google.com/open?id=1np5g02xBMf0sG9t-T2vTGFhJfhyOIDK5)

In the python file i am collecting all question from site 5 times and then found the intersection strings i.e. common questions  that site was generating (collected by refreshing site 5 times)

So the common questions were

[ 'How many planets are between Earth and the Sun? number', 'What year is it? number', 'Who directed the movie Jaws? word', What is the capital of Germany? word', 'What color is the sky? word', 'What is the tallest mountain on Earth? word', 'What is the capital of Hawaii? word', 'How many strings does a violin have? number']

Then i answered the above questions manually and found the flag !!!!! 


<b>IceCTF{ahh_we_have_been_captchured}<//b>
