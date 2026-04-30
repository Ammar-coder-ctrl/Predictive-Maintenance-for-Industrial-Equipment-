# importing libraries
import pandas as pd

#data
path = "../Data/ai4i2020.csv"
data = pd.read_csv(path)
data = pd.get_dummies(data,columns=["Type"],prefix=['Type'])
data["temp_diff"] = data['Process temperature [K]'] - data['Air temperature [K]']
data["power"] = data["Rotational speed [rpm]"] * data["Torque [Nm]"] 
data = data.drop(columns = ['Process temperature [K]','Air temperature [K]','Rotational speed [rpm]','Torque [Nm]'])
data = data.drop(columns = ["PWF","TWF","HDF","OSF","RNF","Type_H","Type_L","Type_M"])
data = data.drop(columns=["UDI", "Product ID"])

X = data.drop(columns = ["Machine failure"])
y = data["Machine failure"]