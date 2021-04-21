import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
import numpy as np

mtcars = pd.read_csv("mtcars.csv")

print("Files Imported Sucessfully...!")

description = mtcars.describe()
print(description)

data_types = mtcars.dtypes
print(data_types)

missing_values = mtcars.isna().any()
print(missing_values)

#sns.boxplot(mtcars['hp'])

filt = mtcars["hp"].values<300

mtcars_filt = mtcars[filt]

sns.boxplot(mtcars_filt['hp'])