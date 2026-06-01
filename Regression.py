from sklearn.linear_model import LinearRegression
area=[[500],[700],[800],[2200]]
price=[5,7,8,22]
model=LinearRegression()
model.fit(area,price)
prediction=model.predict([[1600]])
print("Predicted Price is :",prediction)
