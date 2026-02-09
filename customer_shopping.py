#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
df = pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\shopping_trends.csv')


# In[10]:


df.head()


# In[11]:


df.info()


# In[12]:


df.describe(include = 'all')


# In[13]:


df.isnull().sum()


# In[14]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[15]:


df.isnull().sum()


# In[16]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df =df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[17]:


df.columns


# In[18]:


#create a new column 
labels = ['Young Adult','Adult','Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels = labels)


# In[19]:


df[['age','age_group']].head(10)


# In[20]:


#create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df ['frequency_of_purchases'].map(frequency_mapping)


# In[21]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[22]:


df[['discount_applied','promo_code_used']].head(10)


# In[23]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[24]:


df = df.drop('promo_code_used',axis=1)


# In[25]:


df.columns


# In[26]:


print("Kernel is working")


# In[28]:


get_ipython().system('pip install psycopg2-binary sqlalchemy pandas')


# In[40]:


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "postgres"
password = quote_plus("Dolly@165")   # very important
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)


engine.connect()
print("✅ Connected to PostgreSQL successfully")


df.to_sql(
    name="customer",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data inserted into PostgreSQL")



df_sql = pd.read_sql("SELECT * FROM customer", engine)
df_sql.head()




# In[ ]:




