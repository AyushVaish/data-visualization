# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ruc5HjJP4ULTTVfU-9CVDZv4pU5_8YQU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


!gdown 1z2TOGBLEkfrzZk9HmM_2jumTfqtJFoyQ
df = pd.read_csv("weight-height.csv")

sns.scatterplot(data=df,x="Height",y="Weight",hue="Gender")

sns.boxplot(data=df,x="Gender",y="Weight")

plt.figure(figsize=(20,5))


plt.subplot(1,3,1)
sns.scatterplot(data=df,x="Height",y="Weight",hue="Gender")
plt.xticks(rotation=90,size=20)

plt.subplot(1,3,2)
sns.boxplot(data=df,x="Gender",y="Weight")

plt.subplot(1,3,3)
sns.barplot(data=df,x="Gender",y="Height",estimator=np.min,ci=None)
plt.legend(["M","F"])

df[df["Gender"] == "Male"].describe()

Parties = ["INC","BJP","JDS", "Others"]
Data = [135,66,19,4]
plt.pie(Data,labels=Parties,autopct="%.0f%%")
plt.title('Karnataka 2023 Election')
plt.show()

t = sns.load_dataset("tips")

t.corr()

sns.heatmap(data=t.corr())

sns.jointplot(data=t,x="tip",y="total_bill",kind="reg")

