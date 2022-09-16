#!/usr/bin/env python
# coding: utf-8

# Pandas

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


pets = pd.DataFrame({'sex': np.array(['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M']),
                   'age': np.array([21, 45, 23, 56, 47, 70, 34, 30, 19, 62]),
                   'pets': np.array([['cat', 'dog'],
                                    ['hamster'],
                                    ['cat', 'gerbil'],
                                    ['fish', 'hamster', 'gerbil'],
                                    ['cat'],
                                    ['dog'],
                                    ['dog'],
                                    ['cat'],
                                    ['rabbit', 'cat'],
                                    ['dog']])})


# In[12]:


pets


# What sex was the youngest respondent?

# In[71]:




#df=pd.DataFrame(pets)
#print(df.min())

#pets.l

print(pd.DataFrame(pets).min())

pets.loc[pets['age'] == min(pets['age']), 'sex']


# What age was the person with the most pets?

# In[45]:


#df=pd.DataFrame(pets)
#Create new integer list, use lambda function to apply (start,finish) 
#y=len(pets)

pets['num_pets'] = pets['pets'].apply(lambda x: len(x))


# In[46]:


pets


# In[51]:


pets.loc[pets['num_pets'] == max(pets['num_pets']), 'age']


# In[61]:


#What was the most popular pet?

#pet_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)

pets_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)
pets_series


# In[64]:


pd.Series.value_counts(pets_series)


# What was the average age of dog owners?

# In[85]:


#pets.loc[pets['pets'].apply(lambda x: 'dog' in x), 'age']         #show only ages who have dog
                             
                             
pets.loc[pets['pets'].apply(lambda x: 'dog' in x), 'age'].mean()   #show mean of dogs only


# In[ ]:





# In[ ]:




