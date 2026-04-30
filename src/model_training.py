#importing libraries
from sklearn.model_selection import train_test_split
from data_preprococing import X,y
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix




#data split
X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=True,test_size=0.2,random_state=0)

#model
model = RandomForestClassifier(n_estimators=100,class_weight="balanced",random_state=0)
model.fit(X_train,y_train)
y_pred = model.predict_proba(X_test)[:,1]
threshold = 0.2
y_pred_new = (y_pred >= threshold).astype(int)

#result
print("result :")
print(classification_report(y_test, y_pred_new))
print("---------------------------------------------------------")
print("confusion matrix :")
print(confusion_matrix(y_test, y_pred_new))






