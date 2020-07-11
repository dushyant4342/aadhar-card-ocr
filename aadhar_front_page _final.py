#!/usr/bin/env python
# coding: utf-8

# In[351]:


import re
import matplotlib.pyplot as plt
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import dateutil.parser as dparser
from PIL import Image
import io
import json

import difflib
import csv
import dateutil.parser as dparser
from dateutil.parser import _timelex, parser
from PIL import Image, ImageEnhance, ImageFilter


# In[510]:


img = cv2.imread("aadhar1.1.1.jpg")
plt.imshow(img)


# In[511]:


#alpha=1.5          #ContrastControl(1.0-3.0)
#beta= 10        #Brightness control (0-100)

#adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

#plt.imshow('original', img)
#plt.imshow(adjusted)


# In[512]:


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')


# In[513]:


text=pytesseract.image_to_string(gray_img)


# In[514]:


print(text)


# In[515]:


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


# In[16]:


lines=text
#lines.split('\n')


# In[17]:

# Searching for Year of Birth
lines = text
#print(lines)
for wordlist in lines.split('\n'):
    xx = wordlist.split()
    if [w for w in xx if re.search('(Year|Birth|irth|YoB|YOB:|DOB:|DOB|DO8:|DO8|D08:|DOR:)$', w)]:
        yearline = wordlist
        break
    else:
        text1.append(wordlist)
try:
    text2 = text.split(yearline, 1)[1]
except Exception:
    pass


try:
    yearline = re.split('Year|Birth|Birth |Birth :|Birth:|irth|YoB|DOB :|DOB:|DOB|DO8:|DO8 |D08:|DOR:', yearline)[1:]
    yearline = ''.join(str(e) for e in yearline)
    if(yearline):
        ayear = dparser.parse(yearline,fuzzy=True).year
except:
    pass
#print(yearline)
#print(text1)
#print(text2)


# In[18]:


lineno = 0  # to start from the first line of the text file.

for wordline in text1:
    xx = wordline.split('\n')
    if ([w for w in xx if re.search('(Government of India|vernment of India|overnment of India|ernment of India|India|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|GOVERNMENT OF INDIA|OVERNMENT OF INDIA|INDIA|NDIA)$', w)]):
        text1 = list(text1)
        lineno = text1.index(wordline)
        break

# text1 = list(text1)
text0 = text1[lineno+1:]
#print(text0) 

#name=text0[1]
#print(name)



try:
    for wordlist in lines.split('\n'):
        xx = wordlist.split( )
        if ([w for w in xx if re.search('(Female|Male|emale|male|ale|FEMALE|MALE|EMALE)$', w)]):
            genline = wordlist
            break
            
    if 'Male' in genline or 'MALE' in genline:
        gender = "Male"

    if 'Female' in genline or 'FEMALE' in genline:
        gender = "Female"
    

    text2 = text.split(genline,1)[1]

except:
    pass

text3= re.sub('\D', ' ', text2) #remove every character except numbers
text3=text3.replace(" ","")
text3=text3.replace("  ","")
text3=text3.replace("   ","")
text3=text3.replace("    ","")
text3=text3.replace("     ","")
text3[0:12]
no=text3[0:12]

print(no)


# In[516]:


no


# In[ ]:





# In[517]:


text0


# In[518]:


while("" in text0) : 
    text0.remove("") 
while(" " in text0) : 
    text0.remove(" ") 
while("  " in text0) : 
    text0.remove("  ") 
while("   " in text0) : 
    text0.remove("   ") 
print(text0)


# In[519]:


len(text0)


# In[520]:


name=text0[len(text0)-1]
name = name.replace('|', "")
name = name.replace('©)', "")
name = name.replace('-',"")
print(name)


# In[521]:


data1 = {}
data1['Name'] = name
data1['Gender'] = gender
data1['Date of Birth'] = yearline
data1['Uid']=no

data1


# In[522]:


data = data1


# In[523]:



try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Write JSON file
with io.open('data.json', 'w', encoding='utf-8') as outfile:
    str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json', encoding = 'utf-8') as data_file:
    data_loaded = json.load(data_file)

# print(data == data_loaded)

# Reading data back JSON(give correct path where JSON is stored)
with open('data.json', 'r', encoding= 'utf-8') as f:
    ndata = json.load(f)
    
    
print('\t', 'Name:', '\t', ndata['Name'])

print('\t', 'Gender:', '\t', ndata['Gender'])

print('\t', 'DOB:', '\t', ndata['Date of Birth'])

print('\t', 'Uid:', '\t', ndata['Uid'])

