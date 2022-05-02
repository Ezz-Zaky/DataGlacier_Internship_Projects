import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

"""## Importing the dataset"""

dataset = pd.read_csv('Healthcare_dataset.csv', header=None)
headers = pd.DataFrame(dataset.iloc[0, :].values)
X = pd.DataFrame(dataset.iloc[0:, :-1].values)
y = dataset.iloc[0:, -1].values


# Categorical boolean mask
categorical_feature_mask = X.dtypes == object
categorical_cols = X.columns[categorical_feature_mask].tolist()
# filter categorical columns using mask and turn it into a list
le = LabelEncoder()
X[categorical_cols] = X[categorical_cols].apply(lambda col: le.fit_transform(col))
ohe = OneHotEncoder(sparse=False )
#One-hot-encode the categorical columns.
array_hot_encoded = ohe.fit_transform(X)
#Convert it to df
X_hot_encoded = pd.DataFrame(array_hot_encoded)
#Extract only the columns that didn't need to be encoded

X_other_cols = X.drop(columns=categorical_cols)

#Concatenate the two dataframes :
data_out = pd.concat([X_hot_encoded, X_other_cols], axis=1)
le_y = LabelEncoder()
y = pd.DataFrame(le_y.fit_transform(y))
data_out = pd.concat([data_out, y], axis=1)
final_dataset = [headers, data_out]
final_dataset = pd.concat(final_dataset)
final_dataset.to_csv('Healthcare_processed_dataset.csv')
