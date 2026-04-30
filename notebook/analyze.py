#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data
path = "../Data/ai4i2020.csv"
data = pd.read_csv(path)


#analyze
print("10 rows")
print(data.head(10))

#remove unnecessary data
data = data.drop(columns=["UDI", "Product ID"])

#one hot encoder
data = pd.get_dummies(data,columns=["Type"],prefix=['Type'])

#feature engineering
data["temp_diff"] = data['Process temperature [K]'] - data['Air temperature [K]']
data["power"] = data["Rotational speed [rpm]"] * data["Torque [Nm]"] 
data = data.drop(columns = ['Process temperature [K]','Air temperature [K]','Rotational speed [rpm]','Torque [Nm]'])


#remove misleading data
data = data.drop(columns = ["PWF","TWF","HDF","OSF","RNF","Type_H","Type_L","Type_M"])



#heat map
sns.heatmap(data.corr(),cmap = 'coolwarm')
plt.show()

#target distribution
print(data["Machine failure"].value_counts())