#python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://96dmjlfiiameu26-anticaptcha.labs.icec.tf/")
totals_rows =driver.find_elements_by_xpath("html/body/div/form/table/tbody/tr")
total_rows_length = len(totals_rows)
print(len(totals_rows))
a=[]
b=[]
c=[]
d=[]
e=[]
import time
for i in range(5):
    driver.refresh()
    time.sleep(3)
    count = 1
    yes=0
    print(i)
    for row in totals_rows:
    	site =  "html/body/div/form/table/tbody/tr["+str(count)+"]"+"/td[2]"
    	content="html/body/div/form/table/tbody/tr["+str(count)+"]"
    	content=driver.find_element_by_xpath(content).text
    	z=driver.find_element_by_xpath(site).text
    	
    	if(i==0):
    		a.append(content)
    	if(i==1):
    		b.append(content)
    	if(i==2):
    		c.append(content)
    	if(i==3):
    		d.append(content)
    	if(i==4):
    		e.append(content)
    	yes+=1
    	count+=1
m=list(set(a).intersection(set(b)))
m=list(set(m).intersection(set(c)))
m=list(set(m).intersection(set(d)))
m=list(set(a).intersection(set(e)))
print(m)
