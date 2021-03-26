#!/usr/bin/env python
# coding: utf-8

# In[103]:


import requests
from bs4 import BeautifulSoup
d={}
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFtWia9KhPZ")
page.status_code
soup= BeautifulSoup(page.content, 'html.parser')

p= body.find(id= "seven-day-forecast-container").get_text().replace("\n"," ").replace("\n\n", " ").replace("\n\n\n", " ").replace('Partly CloudyLow', "PartlyCloudyLow")
print(p)
list= p.strip().split(" ")


today= ['today']
for i in range(len(list)):
    
    if i%5 == 0:
        print(list[i])
        
    
        
    
#Sorry, could not make it, should work on strings



# for i in range(len(list)):
#     if i==" ":
#         break
#     d= { list[i]: list[i]}
#     print(d)
    

    
    


# In[ ]:


for p in data['response']:
    print(f"Duration: {p['duration']}")
    print(f"RiseTime: {p['risetime']}")


# In[ ]:


html= list(soup.children)[2]
body= list(html.children)[3]
p= list()

