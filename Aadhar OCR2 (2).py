#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import re
import matplotlib.pyplot as plt
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


# In[2]:


import os
import os.path
import json
import sys
import pytesseract
import re
import csv
import dateutil.parser as dparser
from PIL import Image


# In[3]:


img=cv2.imread('aadhar.jpg')
plt.imshow(img)


# In[4]:


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')


# In[5]:


text=pytesseract.image_to_string(gray_img)


# In[6]:


print(text)


# In[7]:


name = None
gender = None
ayear = None
uid = None
yearline = []
genline = []
nameline = []
text0 = []
text1 = []
text2 = []
genderStr = '(Female|Male|emale|male|ale|FEMALE|MALE|EMALE)$'


# In[8]:


lines=text
lines.split('\n')


# In[9]:


# Searching for Year of Birth
lines = text
# print (lines)
for wordlist in lines.split('\n'):
    xx = wordlist.split()
    if [w for w in xx if re.search('(Year|Birth|irth|YoB|YOB:|DOB:|DOB)$', w)]:
        yearline = wordlist
        break
    else:
        text1.append(wordlist)
try:
    text2 = text.split(yearline, 1)[1]
except Exception:
    pass


# In[10]:


try:
    yearline = re.split('Year|Birth|irth|YoB|YOB:|DOB:|DOB', yearline)[1:]
    yearline = ''.join(str(e) for e in yearline)
    if yearline:
        ayear = dparser.parse(yearline, fuzzy=True).year
except Exception:
    pass


# In[11]:


yearline


# In[12]:


print(text1)


# In[13]:


print(text2)


# In[14]:


# Searching for Name and finding exact name in database
name=text1[1]
name


# In[15]:


# Searching for Gender
try:
    for wordlist in lines.split('\n'):
        xx = wordlist.split()
        if [w for w in xx if re.search(genderStr, w)]:
            genline = wordlist
            break

    if 'Female' in genline or 'FEMALE' in genline:
        gender = "Female"
    if 'Male' in genline or 'MALE' in genline:
        gender = "Male"

    text2 = text.split(genline, 1)[1]
except Exception:
    pass


# In[16]:


text2


# In[17]:


genline


# In[18]:


#Search for name


# In[19]:


# Searching for UID
try:
    newlist = []
    for xx in text2.split('\n'):
        newlist.append(xx)
    newlist = list(filter(lambda x: len(x) > 12, newlist))
    for no in newlist:
        print(no)
        if re.match("^[0-9 ]+$", no):
            uid.add(no)

except Exception:
    pass


# In[20]:


no


# In[21]:


data = {}
data['Name'] = name
data['Gender'] = gender
data['Date of Birth'] = yearline
data['Uid']=no


# In[22]:


data


# In[23]:


import pandas as pd


# In[24]:


df=pd.DataFrame(data, index=['']).transpose()


# In[25]:


print(df)


# In[26]:


img2=cv2.imread('aadhar_back.jpg')
plt.imshow(img2)


# In[27]:


gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img2, cmap='gray')


# In[28]:


text_back=pytesseract.image_to_string(gray_img2)


# In[29]:


print(text_back)


# In[30]:


addreSS_str='(Address|Address:|dress:|ress:|dress|ress)$'


# In[31]:


text1_back=[]
text2_back=[]


# In[32]:


lines_back = text_back.split('\n')
for lin in lines_back:
    s = lin.strip()
    s = lin.replace('\n','')
    s = s.rstrip()
    s = s.lstrip()
    text1_back.append(s)

text1_back = list(filter(None, text1_back))
print(text1_back)


lineno = 0  # to start from the first line of the text file.

for wordline in text1_back:
    xx = wordline.split('\n')
    if ([w for w in xx if re.search(addreSS_str, w)]):
        text1_back = list(text1_back)
        lineno = text1_back.index(wordline)
        break

# text1 = list(text1)
text0_back = text1_back[lineno+1:]
print(text0_back) 
print(lineno)


# In[33]:


text0_back


# In[34]:


try:
    village = text0_back[1]
    village = village.replace(",", "")
    village = re.sub('[^a-zA-Z] +', ' ', village)
except:
    pass


# In[35]:


village


# In[36]:


try:

    # Cleaning
    address = text0_back[0]
    address = address.rstrip()
    address = address.lstrip()
    address = address.replace("3/0", "S/O")
    address = address.replace(",", " ")
    address = re.sub('[^a-zA-Z] +', ' ', address)

except:
    pass


# In[37]:


print('Address:', address)


# In[38]:


print("City:", village)


# In[39]:


try:
    state = text0_back[2]
    state = state.replace(",", "")
    state = re.sub('[^a-zA-Z] +', ' ', state)
except:
    pass


# In[40]:


state_pc = state.split()


# In[41]:


state_pc


# In[42]:


state_back = state_pc[0]


# In[43]:


pincode = state_pc[1]


# In[44]:


pincode


# In[45]:


print("State & Pincode:", state)


# In[46]:


data2={}
data2['Address']=address
data2['City']=village
data2['State'] = state_back
data2['Pincode'] = pincode


# In[47]:


data2


# In[48]:


df2 = pd.DataFrame(data2, index=['']).transpose()


# In[49]:


df2


# In[50]:


pd.concat([df,df2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




