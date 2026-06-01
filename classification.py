from scikit-learn_model import LogisticRegression
hours = [[1],[2],[3],[4],[5]]
result = [0,0,0,1,1]
model=LogisticRegression()
model.fit(hours,result)
prediction=model.predict([[8]])
print("Result",prediction)
