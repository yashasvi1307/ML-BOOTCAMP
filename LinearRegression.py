from sklearn.Linear_model impact LinearRegression
battery=[[2000],[3000],[7000],[9000]]
backup=[8,12,16,20,24]
model=LinearRegression()
model.fit(battery,backup)
prediction=model.predict([[8000]])
print(prediction)
