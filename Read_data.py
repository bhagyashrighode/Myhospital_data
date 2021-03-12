#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sqlite3
db = sqlite3.connect('C:\\Users\\admin\\Desktop\\Assignment.db')
cursor = db.cursor()
cursor.execute('SELECT * FROM My_hospital_data')
rows = cursor.fetchall()

for row in rows:
    print(row)
db.commit()


# In[ ]:




