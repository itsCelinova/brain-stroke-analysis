#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')


# In[54]:


stroke_Data = pd.read_csv("C:/Users/OMEN/Downloads/healthcare-dataset-stroke-data.xls")


# In[55]:


stroke_Data.head()


# In[48]:


stroke_Data.shape
#so we have 5110 rows and 12 columns


# In[49]:


stroke_Data.dtypes


# In[58]:


stroke_Data['age'] = pd.to_numeric(stroke_Data['age']).astype('int64')


# In[60]:


stroke_Data['bmi'].fillna(stroke_Data['bmi'].median(), inplace=True)

print(stroke_Data['bmi'].isnull().sum())  # Should print 0


# In[61]:


stroke_Data.rename(columns={
    'id': 'Patient_ID',
    'gender': 'Gender',
    'age': 'Age',
    'hypertension': 'Has_Hypertension',
    'heart_disease': 'Has_Heart_Disease',
    'ever_married': 'Marital_Status',
    'work_type': 'Employment_Type',
    'Residence_type': 'Residence_Type',
    'avg_glucose_level': 'Avg_Glucose_Level',
    'bmi': 'BMI',
    'smoking_status': 'Smoking_Status',
    'stroke': 'Stroke_Occurred_Previously'
}, inplace=True)


# In[62]:


stroke_Data.head()


# In[63]:


stroke_Data.isna().sum()


# In[64]:


stroke_Data.loc[stroke_Data.duplicated(subset=['Patient_ID'])]


# In[70]:




plt.figure(figsize=(10,8))
sns.heatmap(stroke_Data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Stroke Dataset', fontsize=14, fontweight='bold')
plt.show()


# In[91]:


# Drop Patient_ID before correlation
data_for_corr = stroke_Data.drop(columns=['Patient_ID'])

# Calculate correlation with target
correlations = data_for_corr.corr()['Stroke_Occurred_Previously'].sort_values(ascending=False)

# Drop the target itself
correlations = correlations.drop('Stroke_Occurred_Previously')

colors = ['#CD2C58'] * len(correlations)

# Plot
plt.figure(figsize=(10,6), facecolor='#F5F5F0')  # figure background
ax = correlations.plot(kind='bar', color=colors)
ax.set_facecolor('#B3BFFF')  # plot background
plt.title('Correlation of Features with Stroke Occurrence', color='black', fontsize=20, fontweight='bold')
plt.ylabel('Correlation coefficient', color='black', fontsize=16)
plt.xlabel('Features', color='black', fontsize=16)


plt.xticks(rotation=45, color='black', fontsize=12)
plt.yticks(color='black', fontsize=12)

plt.show()


# In[97]:



# Select relevant features (exclude Patient_ID)
features = stroke_Data.drop(columns=['Patient_ID'])

# Pairplot with hue on target variable
sns.pairplot(
    features,
    hue='Stroke_Occurred_Previously',
    palette={0: '#4A90E2', 1: '#E94E4E'},
    diag_kind='kde',  # shows density plots on diagonal
    height=2.5  # size of each subplot
)

plt.suptitle('Pairplot of Stroke Dataset Features', fontsize=18, color='black', y=1.02)
plt.show()


# In[99]:


"""Age: Most stroke cases (red) occur in older age groups (~50+).

Avg_Glucose_Level: Stroke cases appear in higher glucose ranges, but many non-stroke patients also have high glucose.

BMI: Stroke cases are scattered across BMI, but slightly more in higher BMI ranges.

Has_Hypertension / Has_Heart_Disease: Very few stroke cases overall, but when stroke occurs, they often coincide with these conditions."""


# In[101]:


stroke_Data.to_csv('stroke_data_only.csv', index=False)


# In[102]:


import os
print(os.getcwd())


# In[ ]:




