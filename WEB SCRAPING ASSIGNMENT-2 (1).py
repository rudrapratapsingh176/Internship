#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


# In[2]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")


# In[3]:


driver.get("https://www.naukri.com/")


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[5]:


Designations=driver.find_element(By.CLASS_NAME,"suggestor-input ")
Designations.send_keys('Data Analyst')


# In[6]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys('Bangalore')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[6]')
search.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[9]:


title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title[0:10]:
    title1=i.text
    job_title.append(title1)


# In[10]:


loaction=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in loaction[0:10]:
    location1=i.text
    job_location.append(location1)


# In[11]:


company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company[0:10]:
    company1=i.text
    company_name.append(company1)


# In[12]:


experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
    experience1=i.text
    experience_required.append(experience1)


# In[13]:


import pandas as pd


# In[14]:


print(len(experience_required),len(company_name),len(job_location),len(job_title))


# In[15]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[16]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.naukri.com/")


# In[17]:


Designations=driver.find_element(By.CLASS_NAME,"suggestor-input ")
Designations.send_keys('Data Scientist')


# In[18]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys('Bangalore')


# In[19]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[6]')
search.click()


# In[20]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[21]:


title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title[0:10]:
    title1=i.text
    job_title.append(title1)


# In[22]:


loaction=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in loaction[0:10]:
    location1=i.text
    job_location.append(location1)


# In[23]:


company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company[0:10]:
    company1=i.text
    company_name.append(company1)


# In[24]:


experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
    experience1=i.text
    experience_required.append(experience1)


# In[25]:


print(len(experience_required),len(company_name),len(job_location),len(job_title))


# In[26]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[27]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.naukri.com/")


# In[28]:


Designation=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input')
Designation.send_keys('Data Scientist')


# In[29]:


Location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
Location.send_keys('Delhi / NCR')


# In[30]:


Search=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[6]')
Search.click()


# In[31]:


Salary=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]')
Salary.click()


# In[32]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[33]:


title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title[0:10]:
    title1=i.text
    job_title.append(title1)


# In[34]:


loaction=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in loaction[0:10]:
    location1=i.text
    job_location.append(location1)


# In[35]:


company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company[0:10]:
    company1=i.text
    company_name.append(company1)


# In[36]:


experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience[0:10]:
    experience1=i.text
    experience_required.append(experience1)


# In[37]:


print(len(experience_required),len(company_name),len(job_location),len(job_title))


# In[38]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[21]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")


# In[22]:


sun=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
sun.send_keys('sunglasses')


# In[23]:


Search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
Search.click()


# In[24]:


Brand=[]
product_description=[]
price=[]


# In[25]:



start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')[0:100]
    for i in brand:
        brand1=i.text
        Brand.append(brand1)
    product=driver.find_elements(By.XPATH,'//div[@class="_1xHGtK _373qXS"]')[0:100]
    for i in product:
        product1=i.text
        product_description.append(product1)
    Price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')[0:100]
    for i in Price:
        price.append(i.text)    
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click() 
    time.sleep(1)


# In[26]:


print(len(Brand),len(product_description),len(price))


# In[27]:


df=pd.DataFrame({'Brand':Brand,'Product Description':product_description,'Price':price})
df


# In[2]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART")


# In[4]:


Rating=[]
Review_summary=[]
Full_review=[]


# In[5]:


Rating1=[]
Rating2=[]


# In[6]:


start=0
end=10
for page in range(start,end):
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating:
        Rating1.append(i.text)
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1rdVr6 _1BLPMq"]')
    for i in rating:
        Rating2.append(i.text)    
    review=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in review:
        Review_summary.append(i.text)    
    full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full:
        Full_review.append(i.text)
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1rdVr6 _1BLPMq"]')
    for i in rating:
        Rating2.append(i.text)    
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]')
    next_button.click() 
    time.sleep(1)


# In[8]:


Rating=Rating1+Rating2


# In[9]:


print(len(Rating),len(Review_summary),len(Full_review))


# In[10]:


df=pd.DataFrame({'Rating':Rating,'Review_summary':Review_summary,'Full_review':Full_review})
df


# In[98]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")


# In[99]:


shoes=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
shoes.send_keys('sneakers')


# In[100]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search.click()


# In[101]:


Brand=[]
Product_Description=[]
Price=[]


# In[102]:


start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand[0:100]:
        brand1=i.text
        Brand.append(brand1)
    product=driver.find_elements(By.XPATH,'//div[@class="_1xHGtK _373qXS"]')
    for i in product[0:100]:
        product1=i.text
        Product_Description.append(product1)
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price[0:100]:
        price1=i.text
        Price.append(price1)    
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click() 
    time.sleep(1)


# In[103]:


print(len(Brand),len(Product_Description),len(Price))


# In[39]:


df=pd.DataFrame({'Brand':Brand,'Product_Description':Product_Description,'Price':Price})
df


# In[49]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")


# In[50]:


laptop=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
laptop.send_keys('Laptop')


# In[51]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[52]:


cpu=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/li[13]/span/a')
cpu.click()


# In[53]:


Title=[]
Rating=[]
Price=[]


# In[54]:


title=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title[0:18]:
    title1=i.text
    Title.append(title1)
title=driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')
for i in title[0:18]:
    title1=i.text
    Rating.append(title1)
    title=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in title[0:18]:
    title1=i.text
    Price.append(title1)    


# In[55]:


df=pd.DataFrame({'Title':Title,'Rating':Rating,'Price':Price})
df.drop([5,6,7,8,9,10,11,12],axis=0,inplace=True)
df


# In[61]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.azquotes.com/")


# In[62]:


top_quotes=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top_quotes.click()


# In[63]:


Quotes=[]
Author=[]
Type_Of_Quotes=[]


# In[64]:


start=0
end=10
for page in range(start,end):
    a=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in a:
        a1=i.text
        Quotes.append(a1)
    a=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in a:
        a1=i.text
        Author.append(a1)
    a=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in a:
        a1=i.text
        Type_Of_Quotes.append(a1)    
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a')
    next_button.click() 
    time.sleep(1)


# In[65]:


df=pd.DataFrame({'Quote':Quotes,'Author':Author,'Type_Of_Quotes':Type_Of_Quotes})
df


# In[66]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.jagranjosh.com/")


# In[67]:


Gk=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[6]/div/div[1]/header/div[3]/ul/li[9]/a')
Gk.click()


# In[68]:


news=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')
news.click()


# In[69]:


Name=[]
Born_Dead=[]
Terms_of_office=[]
Remarks=[]


# In[70]:


name1=[]
name2=[]
name3=[]
name4=[]
name5=[]


# In[71]:


a=driver.find_elements(By.XPATH,'//td[@style="width: 150px; height: 121px;"]')
for i in a:
    a1=i.text
    name1.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 150px; height: 80px;"]')
for i in a:
    a1=i.text
    name2.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 150px; height: 104px;"]')
for i in a:
    a1=i.text
    name3.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 150px; height: 87px;"]')
for i in a:
    a1=i.text
    name4.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 150px; height: 97px;"]')
for i in a:
    a1=i.text
    name5.append(a1)    


# In[72]:


Name=name1+name2+name3+name4+name5


# In[73]:


Born_Dead1=[]
Born_Dead2=[]
Born_Dead3=[]
Born_Dead4=[]
Born_Dead5=[]


# In[74]:


a=driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 121px;"]')
for i in a:
    a1=i.text
    Born_Dead1.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 80px;"]')
for i in a:
    a1=i.text
    Born_Dead2.append(a1) 
a=driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 104px;"]')
for i in a:
    a1=i.text
    Born_Dead3.append(a1) 
a=driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 87px;"]')
for i in a:
    a1=i.text
    Born_Dead4.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 97px;"]')
for i in a:
    a1=i.text
    Born_Dead5.append(a1)    


# In[75]:


Born_Dead=Born_Dead1+Born_Dead2+Born_Dead3+Born_Dead4+Born_Dead5


# In[77]:


Terms_of_office1=[]
Terms_of_office2=[]
Terms_of_office3=[]
Terms_of_office4=[]
Terms_of_office5=[]


# In[78]:


a=driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 121px;"]')
for i in a:
    a1=i.text
    Terms_of_office1.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 80px;"]')
for i in a:
    a1=i.text
    Terms_of_office2.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 104px;"]')
for i in a:
    a1=i.text
    Terms_of_office3.append(a1)   
a=driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 87px;"]')
for i in a:
    a1=i.text
    Terms_of_office4.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 97px;"]')
for i in a:
    a1=i.text
    Terms_of_office5.append(a1)    


# In[79]:


Terms_of_office=Terms_of_office1+Terms_of_office2+Terms_of_office3+Terms_of_office4+Terms_of_office5


# In[80]:


Remarks1=[]
Remarks2=[]
Remarks3=[]
Remarks4=[]
Remarks5=[]


# In[81]:


a=driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 121px;"]')
for i in a:
    a1=i.text
    Remarks1.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 80px;"]')
for i in a:
    a1=i.text
    Remarks2.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 104px;"]')
for i in a:
    a1=i.text
    Remarks3.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 87px;"]')
for i in a:
    a1=i.text
    Remarks4.append(a1)
a=driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 97px;"]')
for i in a:
    a1=i.text
    Remarks5.append(a1)    


# In[82]:


Remarks=Remarks1+Remarks2+Remarks3+Remarks4+Remarks5


# In[83]:


df=pd.DataFrame({'Name':Name,'Born-Dead':Born_Dead,'Terms_of_office':Terms_of_office,'Remarks':Remarks})
df.sort_values(by="Born-Dead")


# In[25]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.motor1.com/")


# In[26]:


menu=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/div[1]/div')
menu.click()


# In[27]:


feature=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[5]/a')
feature.click()


# In[28]:


view=driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div/div[1]/div[2]/a')
view.click()


# In[29]:


lists=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[1]/div[1]/div/div/div[9]/div/div[1]/h3/a')
lists.click()


# In[30]:


name=[]
price=[]


# In[31]:


a=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in a[0:50]:
    a1=i.text
    name.append(a1)
a=driver.find_elements(By.XPATH,"//strong")
for i in a[0:50]:
    a1=i.text
    price.append(a1)    


# In[32]:


df=pd.DataFrame({'Car name':name,'Price':price})
df


# In[ ]:




