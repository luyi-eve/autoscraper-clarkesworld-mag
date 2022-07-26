#!/usr/bin/env python
# coding: utf-8

# # Clarkesworld
# 
# Source: https://clarkesworldmagazine.com/
# 
# Description: Sci-fi/fantasy magazine
# 
# **Topics:**
# 
# * Scraping

# ## Scrape the Clarkesworld homepage `4 points`
# 
# I want a CSV file that includes a row for each story, including the columns:
# 
# * Title
# * Byline
# * URL to story
# * Category (fiction/non-fiction/cover art)
# * Issue number (e.g. 180)
# * Publication date (e.g. September 2021)

# In[4]:


import requests
from bs4 import BeautifulSoup


# In[5]:


response = requests.get("https://clarkesworldmagazine.com/")
doc = BeautifulSoup(response.text, 'html.parser')
doc.select('.story')
# doc.find_all("p",class_="story")


# In[ ]:





# In[ ]:





# # Get urls

# In[13]:


for url in doc.select('.story'):
    print(url.find("a").get("href"))
    #print(url.find("a")["href"])
    print("------------")


# # Get titles

# In[14]:


for title in doc.select('.story'):
    print(title.text.strip())
    print("------------")


# # Get bylines

# In[15]:


for byline in doc.select('.byline .authorname'):
    print(byline.text.strip())
    print("------------")


# # Get categories

# In[16]:


categories = doc.select('.section')
#for category in categories:
    #print(category.text.strip())


# # Turn the data to a Dataframe

# In[17]:


import pandas as pd


# In[18]:


# FICTION

fictions = []

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "FICTION":
            for story in story.select('.index-col1'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "FICTION"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    fiction_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    fictions.append(fiction_dict)

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "FICTION":
            for story in story.select('.index-col2'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "FICTION"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    fiction_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    fictions.append(fiction_dict)

df_fiction = pd.DataFrame(fictions)
df_fiction


# In[21]:


# NON-FICTION

non_fictions = []

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "NON-FICTION":
            for story in story.select('.index-col1'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "NON-FICTION"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    non_fiction_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    non_fictions.append(non_fiction_dict)

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "NON-FICTION":
            for story in story.select('.index-col2'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "NON-FICTION"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    non_fiction_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    non_fictions.append(non_fiction_dict)

df_non_fiction = pd.DataFrame(non_fictions)
df_non_fiction


# In[22]:


# COVER ART

cover_arts = []

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "COVER ART":
            for story in story.select('.index-col1'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "COVER ART"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    cover_art_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    cover_arts.append(cover_art_dict)

for story in doc.select('.index-table'):
    for story in story.select('.index-table'):
        if story.select_one('.section').text == "COVER ART":
            for story in story.select('.index-col2'):
                byline = story.select_one('.byline').text
                for story in story.select('.story'):
                    title = story.text
                    url = story.find('a')["href"]
                    issue_number = 190
                    publication_date = "July 2022"
                    category = "COVER ART"
                    #print(issue_number, publication_date, category, title, byline, url)
                    
                    cover_art_dict = {
                        "issue_number": issue_number,
                        "publication_date": publication_date,
                        "category": category,
                        "title": title,
                        "byline": byline,
                        "url": url,
                    }
                    
                    cover_arts.append(cover_art_dict)

df_cover_art = pd.DataFrame(cover_arts)
df_cover_art 


# In[23]:


merged_df = pd.concat([df_fiction, df_non_fiction, df_cover_art ])
merged_df 


# In[ ]:





# ## Auto-updating scraper `3 points`
# 
# Using GitHub Actions, implement a scraper that will keep track of everything posted to the Clarkesworld homepage. For example, when issue 181 comes out it should *add to the CSV* instead of just replacing it.
# 
# > Tip: `drop_duplicates` might save you a lot of effort at one point or another.

# In[26]:


merged_df.to_csv("clarkesworld.csv")


# In[ ]:




