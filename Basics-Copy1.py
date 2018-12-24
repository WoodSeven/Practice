#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
f = open("guns.csv","r")
data = csv.reader(f)
data = list(data)
print(data[:5])


# In[2]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:5])


# In[3]:


year = []
for row  in data:
    year.append(row[1])
years_counts = {}
for ele in year:
    if ele in years_counts:
        years_counts[ele] += 1
    else:
        years_counts[ele] = 1
print(years_counts)


# In[7]:


import datetime
dates = []
for row in data:
    date = datetime.datetime(year = int(row[1]),month = int(row[2]),day = 1)
    dates.append(date)
print(dates[:5])
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[10]:


sex_counts = {}
race_counts = {}
for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]] += 1
    else:
        sex_counts[row[5]] = 1
    if row[7] in race_counts:
        race_counts[row[7]] += 1
    else:
        race_counts[row[7]] = 1
print(sex_counts)
print(race_counts)


# In[11]:


f = open("census.csv","r")
census = list(csv.reader(f))
print(census)


# In[13]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
ace_per_hundredk = {}
for key,value in race_counts.items():
    ace_per_hundredk[key] = (value / mapping[key]) * 10000
print(ace_per_hundredk)


# In[15]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1
race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000
print(homicide_race_counts)


# In[ ]:




