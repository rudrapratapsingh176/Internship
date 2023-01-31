#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import TimeoutException


# In[10]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")


# In[12]:


user_input=input('Enter the Product-')


# In[13]:


laptop=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
laptop.send_keys(user_input)


# In[14]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[15]:


lap=[]
start=0
end=3
for page in range(start,end):

    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        lap.append(i.get_attribute('href'))
    next_button=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[30]/div/div/span/a[3]')    


# In[17]:


Brand_Name=[]
Name_of_Product=[]
Price=[]
Return_Exchange=[]
Expected_Delivery=[]
Availability=[]


# In[19]:



for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[44]/div/div[1]/div/table/tbody/tr[1]/td[2]/span')
        Brand_Name.append(brand.text)
    except NoSuchElementException:
        Brand_Name.append('-')


# In[20]:


for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[1]/div/h1/span')
        Name_of_Product.append(brand.text)
    except NoSuchElementException:
        Name_of_Product.append('-')

   


# In[21]:


for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[10]/div[3]/div[1]/span[2]/span[2]/span[2]')
        Price.append(brand.text)
    except NoSuchElementException:
        Price.append('-')

  
       


# In[22]:


for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[1]/div/div[1]/h5/div[1]/span/span')
        Return_Exchange.append(brand.text)
    except NoSuchElementException:
        Return_Exchange.append('-')


# In[23]:


for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[2]/div[8]/div[1]/div')
        Expected_Delivery.append(brand.text)
    except NoSuchElementException:
        Expected_Delivery.append('-')
        


# In[24]:


for i in lap:
    driver.get(i)
    time.sleep(1)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[4]/div/div[1]')
        Availability.append(brand.text)
    except NoSuchElementException:
        Availability.append('-')


# In[25]:


len(Brand_Name),len(Availability),len(Expected_Delivery),len(Return_Exchange),len(Price),len(Name_of_Product)


# In[26]:


df=pd.DataFrame({'Brand Name':Brand_Name,'Name of the Product':Name_of_Product,'Price':Price,'Return/Exchange':Return_Exchange,'Expected Delivery':Expected_Delivery,'Availability':Availability})
df


# In[36]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://images.google.com/")


# In[6]:


fruit=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
fruit.send_keys('fruits')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()


# In[18]:


Fruits=[]

images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for i in images[0:10]:
    Fruits.append(i.get_attribute('src'))
Fruits    


# In[19]:


driver.back()


# In[20]:


fruit=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
fruit.send_keys('cars')


# In[21]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()


# In[22]:


cars=[]

images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for i in images[0:10]:
    cars.append(i.get_attribute('src'))
cars 


# In[23]:


driver.back()


# In[24]:


fruit=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
fruit.send_keys('Machine Learning')


# In[25]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()


# In[26]:


Machine_Learning=[]

images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for i in images[0:10]:
    Machine_Learning.append(i.get_attribute('src'))
Machine_Learning 


# In[27]:


driver.back()


# In[28]:


fruit=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
fruit.send_keys('Guitar')


# In[29]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()


# In[30]:


Guitar=[]

images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for i in images[0:10]:
    Guitar.append(i.get_attribute('src'))
Guitar


# In[31]:


driver.back()


# In[37]:


fruit=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
fruit.send_keys('Cakes')


# In[39]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search.click()


# In[40]:


Cakes=[]

images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for i in images[0:10]:
    Cakes.append(i.get_attribute('src'))
Cakes


# In[27]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")


# In[28]:


shoes=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
shoes.send_keys('Smartphone')


# In[29]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search.click()


# In[30]:


URL=[]    
url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    URL.append(i.get_attribute('href'))


# In[32]:


Brand_Name=[]
Smartphone_Name=[]
Colour=[]
RAM=[]
Storage_ROM1=[]
Primary_Camera=[]
Secondary_Camera=[]
Display_Size=[]
Battery_Capacity=[]
Price=[]
Product_URL=[]


# In[56]:



for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[5]/div/div[1]/div/img')
        Brand_Name.append(brand.text)
    except NoSuchElementException:
        Brand_Name.append('-')


# In[57]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
        Smartphone_Name.append(brand.text)
    except NoSuchElementException:
        Smartphone_Name.append('-')


# In[58]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[2]/ul/li')
        Colour.append(brand.text)
    except NoSuchElementException:
        Colour.append('-')


# In[59]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/ul/li')
        RAM.append(brand.text)
    except NoSuchElementException:
        RAM.append('-')


# In[60]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div[4]/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/ul/li')
        Storage_ROM1.append(brand.text)
    except NoSuchElementException:
        Storage_ROM1.append('-')


# In[61]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[2]/td[2]/ul/li')
        Primary_Camera.append(brand.text)
    except NoSuchElementException:
        Primary_Camera.append('-')


# In[62]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[3]/td[2]/ul/li')
        Secondary_Camera.append(brand.text)
    except NoSuchElementException:
        Secondary_Camera.append('-')


# In[63]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div[1]/div/div[2]/ul/li[4]')
        Battery_Capacity.append(brand.text)
    except NoSuchElementException:
        Battery_Capacity.append('-')


# In[64]:



for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div[1]/div/div[2]/ul/li[2]')
        Display_Size.append(brand.text)
    except NoSuchElementException:
        Display_Size.append('-')


# In[65]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
        Price.append(brand.text)
    except NoSuchElementException:
        Price.append('-')


# In[66]:


df=pd.DataFrame({'Brand Name':Brand_Name,'Smartphone Name':Smartphone_Name,'Colour':Colour,'RAM':RAM,'Storage(ROM)':Storage_ROM1,'Primary Camera':Primary_Camera,'Secondary Camera':Secondary_Camera,'Display Size':Display_Size,'Battery Capacity':Battery_Capacity,'Price':Price,'Product URL':URL})
df        


# In[5]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.googlemaps.com/")


# In[6]:


location=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]')
location.send_keys('Kanpur')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button')
search.click()


# In[17]:


get_url = driver.current_url
print('Latitude,Longitude of City- '+str(get_url.split('/')[6][1:22]))


# In[94]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://digit.in/")


# In[95]:


gaming=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[3]/a')
gaming.click()


# In[96]:


laptop=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[3]/div/div/div[2]/div/ul[2]/li[1]/a')
laptop.click()


# In[97]:


Laptop_Name=[]
Windows=[]
Display=[]
Processor=[]
RAM_ROM=[]


# In[98]:


title=driver.find_elements(By.XPATH,'//div[@class="left_side"]')
for i in title[0:10]:
    title1=i.text.split('\n')[1]
    Laptop_Name.append(title1)    


# In[99]:


title=driver.find_elements(By.XPATH,'//div[@class="product-detail"]')
for i in title[0:10]:
    title1=i.text.split('\n')[0]
    Windows.append(title1)
 


# In[100]:


title=driver.find_elements(By.XPATH,'//div[@class="product-detail"]')
for i in title[0:10]:
    title1=i.text.split('\n')[1]
    Display.append(title1)


# In[101]:


title=driver.find_elements(By.XPATH,'//div[@class="product-detail"]')
for i in title[0:10]:
    title1=i.text.split('\n')[2]
    Processor.append(title1)


# In[102]:


title=driver.find_elements(By.XPATH,'//div[@class="product-detail"]')
for i in title[0:10]:
    title1=i.text.split('\n')[3]
    RAM_ROM.append(title1)


# In[103]:


df=pd.DataFrame({'Name':Laptop_Name,'Windows':Windows,'Display':Display,'Processor':Processor,'RAM/ROM':RAM_ROM})
df


# In[62]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://forbes.com/")


# In[63]:


menu=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div/div/div')
menu.click()


# In[64]:


billionore=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div/div/div[2]/ul/li[1]/div[1]')
billionore.click()


# In[66]:


Billionore=driver.find_element(By.XPATH,'/html/body/div[1]/main/div/section/section[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/a/h2')
Billionore.click()


# In[76]:


rank=[]
name=[]
net_worth=[]
age=[]
citizenship=[]
source=[]
industy=[]


# In[77]:


brand=driver.find_elements(By.XPATH,'//div[@class="rank"]')
for i in brand:
    brand1=i.text
    rank.append(brand1)


# In[78]:


brand=driver.find_elements(By.XPATH,'//div[@class="personName"]')
for i in brand:
    brand1=i.text
    name.append(brand1)


# In[79]:


brand=driver.find_elements(By.XPATH,'//div[@class="netWorth"]')
for i in brand:
    brand1=i.text
    net_worth.append(brand1)


# In[80]:


brand=driver.find_elements(By.XPATH,'//div[@class="age"]')
for i in brand:
    brand1=i.text
    age.append(brand1)


# In[81]:


brand=driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
for i in brand:
    brand1=i.text
    citizenship.append(brand1)


# In[82]:


brand=driver.find_elements(By.XPATH,'//div[@class="source"]')
for i in brand:
    brand1=i.text
    source.append(brand1)


# In[83]:


brand=driver.find_elements(By.XPATH,'//div[@class="category"]')
for i in brand:
    brand1=i.text
    industy.append(brand1)


# In[85]:


df=pd.DataFrame({'Rank':rank,'Name':name,'Net_Worth':net_worth,'Age':age,'Citizenship':citizenship,'Source':source,'Industy':industy})
df


# In[3]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.youtube.com/")


# In[4]:


name=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
name.send_keys('Mukesh Ambani')


# In[5]:


search=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon')
search.click()


# In[6]:


search1=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
search1.click()


# In[7]:


comments=[]
upvote=[]
time=[]


# In[10]:


brand=driver.find_elements(By.XPATH,'//yt-formatted-string[@class="style-scope ytd-comment-renderer"]')
for i in brand:
    brand1=i.text
    comments.append(brand1)


# In[12]:


product=driver.find_elements(By.XPATH,'//ytd-comment-action-buttons-renderer[@class="style-scope ytd-comment-renderer"]')
for i in product:
    product1=i.text.split('\n')[0]
    upvote.append(product1)


# In[13]:


Price=driver.find_elements(By.XPATH,'//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')
for i in Price:
    time.append(i.text)  


# In[14]:


len(comments),len(upvote),len(time)


# In[15]:


df=pd.DataFrame({'Comments':comments,'Upvote':upvote,'Time':time})
df


# In[297]:


driver=webdriver.Chrome(r"C:\Users\rudra\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://hostelworld.com/")


# In[298]:


Menu=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/header/div/button[2]')
Menu.click()


# In[299]:


Hostel=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/header/div[2]/div/div[2]/ul[2]/li[2]/a')
Hostel.click()


# In[300]:


Location=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[5]/ul/li[1]/a[2]')
Location.click()


# In[301]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[5]/button')
search.click()


# In[319]:


hostel_name=[]
distance=[]
rating=[]
total_reviews=[]
overall_reviews=[]
Privates_and_dorms=[]
facilities=[]
property_description=[]


# In[321]:


brand=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
for i in brand:
    brand1=i.text
    hostel_name.append(brand1)


# In[323]:


brand=driver.find_elements(By.XPATH,'//a[@class="show-on-map"]')
for i in brand:
    brand1=i.text
    distance.append(brand1)


# In[324]:


brand=driver.find_elements(By.XPATH,'//div[@class="rating rating-summary-container big"]')
for i in brand:
    brand1=i.text.split('\n')[0]
    rating.append(brand1)


# In[325]:


brand=driver.find_elements(By.XPATH,'//div[@class="reviews"]')
for i in brand:
    brand1=i.text
    total_reviews.append(brand1)


# In[326]:


brand=driver.find_elements(By.XPATH,'//div[@class="rating rating-summary-container big"]')
for i in brand:
    brand1=i.text.split('\n')[1]
    overall_reviews.append(brand1)


# In[327]:


brand=driver.find_elements(By.XPATH,'//div[@class="prices-col"]')
for i in brand:
    brand1=i.text
    Privates_and_dorms.append(brand1)


# In[328]:


brand=driver.find_elements(By.XPATH,'//div[@class="rating-factors prop-card-tablet rating-factors small"]')
for i in brand:
    brand1=i.text
    facilities.append(brand1)


# In[329]:


URL=[]    
url=driver.find_elements(By.XPATH,'//a[@class="view-button"]')
for i in url:
    URL.append(i.get_attribute('href'))


# In[330]:


for i in URL:
    driver.get(i)
    time.sleep(5)
    try:
        brand=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/section/div[6]/div/div[2]/div[2]/div/div[2]')
        property_description.append(brand.text)
    except NoSuchElementException:
        property_description.append('-')


# In[331]:


len(hostel_name),len(distance),len(rating),len(total_reviews),len(overall_reviews),len(Privates_and_dorms),len(facilities),len(property_description)


# In[332]:


df=pd.DataFrame({'Hostel Name':hostel_name,'Distance':distance,'Rating':rating,'Total Reviews':total_reviews,'Overall Reviews':overall_reviews,'Privates and Dorms':Privates_and_dorms,'Facilities':facilities,'Property Description':property_description})
df


# In[ ]:




