from sklearn import tree

Features=[[35,1],[48,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
Lables=[1,1,2,1,2,1,1,1,1,1,2,1,2,1,2]

obj=tree.DecisionTreeClassifier()

obj=obj.fit(Features,Lables)
print(obj.predict([[97,0]]))