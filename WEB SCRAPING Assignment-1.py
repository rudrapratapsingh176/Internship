#!/usr/bin/env python
# coding: utf-8

# In[61]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[62]:


from bs4 import BeautifulSoup
import requests


# In[64]:


page=requests.get("https://www.wikipedia.org")
soup=BeautifulSoup(page.content)


# In[71]:


header=[]
for i in soup.find_all('h1'):
    header.append(i.text.split('\n\n')[1:3])
header


# In[17]:


page1=requests.get("https://www.imdb.com/list/ls055592025")
page1


# In[116]:


soup1=BeautifulSoup(page1.content)


# In[19]:


name=[]
for i in soup1.find_all('h3',class_="lister-item-header"):
    name.append(i.text.split('\n')[2])


# In[20]:


rating=[]
for i in soup1.find_all('div',class_="ipl-rating-widget"):
    rating.append(i.text.split('\n\n\n\n\n\n\n\n\n')[1])
    


# In[24]:


year=[]
for i in soup1.find_all('span',class_="lister-item-year text-muted unbold"):
    year.append(i.text[1:5])


# In[25]:


import pandas as pd


# In[26]:


df=pd.DataFrame({'name':name,'rating':rating,'year':year})
df


# In[27]:


page3=requests.get("https://www.imdb.com/list/ls056092300")
page3


# In[115]:


soup3=BeautifulSoup(page3.content)


# In[29]:


name=[]
for i in soup3.find_all('h3',class_="lister-item-header"):
    name.append(i.text.split('\n')[2])
    


# In[30]:


rating=[]
for i in soup3.find_all('div',class_="ipl-rating-widget"):
    rating.append(i.text.split('\n\n\n\n\n\n\n\n\n')[1])


# In[32]:


year=[]
for i in soup3.find_all('span',class_="lister-item-year text-muted unbold"):
    year.append(i.text[1:5])


# In[33]:


df=pd.DataFrame({"name":name,"rating":rating,"year of release":year})
df


# In[34]:


page2=requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page2


# In[114]:


soup2=BeautifulSoup(page2.content)


# In[37]:


name=[]
for i in soup2.find_all('h3'):
    name.append(i.text)   


# In[59]:


name1=[]
for i in soup2.find_all('div',class_="presidentListing"):
    name1.append(i.text.split('\n')[2][15:])


# In[60]:


df1=pd.DataFrame({'Name':name,'Term of office':name1})
df1


# In[2]:


page13=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup13=BeautifulSoup(page13.content)


# In[20]:


matches=soup13.find('td',class_="rankings-block__banner--matches").text
points=soup13.find('td',class_="rankings-block__banner--points").text
rating=soup13.find('td',class_="rankings-block__banner--rating u-text-right").text.split('\n')[1][28:]


# In[30]:


Matches=[matches]
for i in soup13.find_all('td',class_="table-body__cell u-center-text")[0:17:2]:
    Matches.append(i.text)    


# In[29]:


Points=[points]
for i in soup13.find_all('td',class_="table-body__cell u-center-text")[1:18:2]:
    Points.append(i.text)


# In[28]:


Rating=[rating]
for i in soup13.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    Rating.append(i.text)


# In[26]:


import pandas as pd


# In[27]:


df13=pd.DataFrame({'matches':Matches,'points':Points,'rating':Rating})
df13


# In[37]:


page5=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup4=BeautifulSoup(page5.content)


# In[38]:


table=soup4.find('tr',class_="rankings-block__banner")
matches=table.find('div',class_="rankings-block__banner--nationality").text.split('\n\n')[1][0:3]
table=soup4.find('tr',class_="rankings-block__banner")
rating=table.find('div',class_="rankings-block__banner--rating").text


# In[40]:


match=[matches]
for i in soup4.find_all('span',class_="table-body__logo-text")[0:9]:
    match.append(i.text)    


# In[41]:


ratings=[rating]
for i in soup4.find_all('td',class_="table-body__cell rating")[0:9]:
    ratings.append(i.text)   


# In[42]:


df5=pd.DataFrame({'team':match,'rating':ratings})
df5


# In[112]:


page6=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup6=BeautifulSoup(page6.content)


# In[67]:


table=soup6.find('tr',class_="rankings-block__banner")
team=table.find('div',class_="rankings-block__banner--nationality").text.split('\n\n')[1][0:2]


# In[68]:


table=soup6.find('tr',class_="rankings-block__banner")
rating=table.find('div',class_="rankings-block__banner--rating").text


# In[43]:


teams=[team]
for i in soup4.find_all('span',class_="table-body__logo-text")[0:9]:
    teams.append(i.text)


# In[44]:


ratings=[rating]
for i in soup4.find_all('td',class_="table-body__cell rating")[0:9]:
    ratings.append(i.text)


# In[45]:


df6=pd.DataFrame({'team':teams,'rating':ratings})
df6


# In[54]:


page14=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup14=BeautifulSoup(page14.content)


# In[55]:


matches=soup14.find('td',class_="rankings-block__banner--matches").text
points=soup14.find('td',class_="rankings-block__banner--points").text
rating=soup14.find('td',class_="rankings-block__banner--rating u-text-right").text.split('\n')[1][28:]


# In[56]:


Matches=[matches]
for i in soup14.find_all('td',class_="table-body__cell u-center-text")[0:17:2]:
    Matches.append(i.text)


# In[57]:


Points=[points]
for i in soup14.find_all('td',class_="table-body__cell u-center-text")[1:18:2]:
    Points.append(i.text)


# In[58]:


Rating=[rating]
for i in soup14.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
    Rating.append(i.text)


# In[59]:


df13=pd.DataFrame({'matches':Matches,'points':Points,'rating':Rating})
df13


# In[31]:


page7=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup7=BeautifulSoup(page7.content)


# In[32]:


table=soup7.find('tr',class_="rankings-block__banner")
team=table.find('div',class_="rankings-block__banner--nationality").text.split('\n\n')[1][0:3]


# In[33]:


table=soup7.find('tr',class_="rankings-block__banner")
rating=table.find('div',class_="rankings-block__banner--rating").text


# In[34]:


teams=[team]
for i in soup7.find_all('span',class_="table-body__logo-text")[0:9]:
    teams.append(i.text)    


# In[35]:


ratings=[rating]
for i in soup7.find_all('td',class_="table-body__cell rating")[0:9]:
    ratings.append(i.text)  


# In[36]:


df7=pd.DataFrame({'team':teams,'rating':ratings})
df7


# In[47]:


page8=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup8=BeautifulSoup(page8.content)


# In[48]:


table=soup8.find('tr',class_="rankings-block__banner")
team=table.find('div',class_="rankings-block__banner--nationality").text.split('\n\n')[1][0:3]


# In[49]:


table=soup8.find('tr',class_="rankings-block__banner")
rating=table.find('div',class_="rankings-block__banner--rating").text


# In[51]:



tables=[team]
for i in soup8.find_all('td',class_="table-body__cell nationality-logo rankings-table__team")[0:9]:
    tables.append(i.text.split('\n')[2])


# In[52]:


ratings=[rating]
for i in soup8.find_all('td',class_="table-body__cell rating")[0:9]:
    ratings.append(i.text)    


# In[53]:


df8=pd.DataFrame({'team':tables,'rating':ratings})
df8


# In[109]:


page9=requests.get('https://www.cnbc.com/world/?region=world')
soup9=BeautifulSoup(page9.content)


# In[85]:


headline=[]
for i in soup9.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    headline.append(i.text)
headline    


# In[86]:


time=[]
for i in soup9.find_all('div',class_="RiverByline-bylineContainer RiverByline-hasSeparator"):
    time.append(i.text[0:11])
time    


# In[87]:


news_link=[]
for i in soup9.find_all('span',class_="QuickLinks-quickLink"):
    news_link.append(i.text)
news_link    


# In[108]:


page10=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup10=BeautifulSoup(page10.content)


# In[89]:


paper_tittle=[]
for i in soup10.find_all('h2'):
    paper_tittle.append(i.text.split('\n'))
paper_tittle    


# In[90]:


Authors=[]
for i in soup10.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Authors.append(i.text)
Authors    


# In[91]:


Published_Date=[]
for i in soup10.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    Published_Date.append(i.text)
Published_Date    


# In[92]:


paper_url=[]
for i in soup10.find_all('div',class_="sc-1fdbg4d-0 GaNmj"):
    paper_url.append(i.text)
paper_url    


# In[155]:


page12=requests.get("https://www.dineout.co.in/delhi-restaurants?search_str=Restaurant")
soup12=BeautifulSoup(page12.content)


# In[156]:


Restaurant_name=[]
for i in soup12.find_all('a',class_="restnt-name ellipsis"):
    Restaurant_name.append(i.text)
Restaurant_name


# In[72]:


page11=requests.get("https://www.dineout.co.in/delhi-restaurants?search_str=Restaurant")
soup11=BeautifulSoup(page11.content)


# In[97]:


Cuisine=[]
for i in soup11.find_all('span',class_="double-line-ellipsis"):
    Cuisine.append(i.text.split('|')[1])
Cuisine


# In[147]:


page13=requests.get("https://www.dineout.co.in/delhi-restaurants?search_str=Restaurant")
soup13=BeautifulSoup(page13.content)


# In[150]:


Location=[]
for i in soup11.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)
Location


# In[151]:


Rating=[]
for i in soup11.find_all('div',class_="restnt-rating rating-4"):
    Rating.append(i.text)
Rating    


# In[154]:


Image_url=[]
for i in soup11.find_all("img",class_="no-img"):
    Image_url.append(i.get('data-src'))
Image_url  


# In[60]:


page12=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page12


# In[ ]:


soup12=BeautifulSoup(page12.content)
soup12


# In[ ]:


Rank=[]
for i in soup12.find_all('td',class_="gsc_mvt_p"):
    Rank.append(i.text)
Rank    

