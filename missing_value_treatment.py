import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.datasets import load_diabetes
%matplotlib inline
diabetes = load_diabetes()

print("Files Imported Sucessfully...!")

#print(diabetes.DESCR)
df=pd.DataFrame(data=diabetes.data,columns=diabetes.feature_names)

#df.head()

df.isna().any()


for col in df.columns:
    fil=df[col].values<-12
    df_new=df[fil]
    sns.boxplot(df[col])
    plt.show()
