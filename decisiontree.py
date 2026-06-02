from sklearn.tree import DecisionTreeClassifier
Salary=[[20],[30],[40],[60]]
loan_status=[0,0,1,1]
model=DecisionTreeClassifier()
model.fit(Salary,loan_status)
prediction=model.predict([[50]])
print(prediction)
