"""     EDA    """
import pandas as pd
finance_data = pd.read_csv("Finance_data.csv")

print(finance_data.head())

print("Dataset shape: \n ******************** ")
print(finance_data.shape)

print("Dataset size: \n ******************** ")
print(finance_data.size)

print("Dataset information: \n ******************** ")
print(finance_data.info())

print("Check for Null values: \n ******************** ")
print(finance_data.isnull().sum())

print("Check Duplicates: \n ******************** ")
print(finance_data.duplicated().sum())
