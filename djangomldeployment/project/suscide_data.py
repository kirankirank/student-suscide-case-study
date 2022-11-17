import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_excel("C:/Users/kiran/Downloads/Suicide Prevention (Responses).xlsx")
data.columns
data.info()
col = data.columns[2:]
for i in col:
    data[i]= np.where(data[i] =="Yes",1,0 )
output = []   
for i in range(len(data)):
    b = 0
    for j in range(2,len(data.columns)):
        a = data.iloc[i,j]
       # print(a)
        b=b+a
    print(b)    
    output.append(np.where(b>=7,1,0))
data['output']= output
data['output']=data['output'].astype('int32')    
sns.countplot(data['output'])
data.columns
data.info()
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data.drop(labels=['Timestamp', 'Name :','output'], axis=1), data['output'],test_size=0.30)

from sklearn.tree import DecisionTreeClassifier 
d = DecisionTreeClassifier(criterion='entropy')
d.fit(x_train,y_train)

from sklearn.metrics import accuracy_score 
accuracy_score(y_train,d.predict(x_train))
accuracy_score(y_test,d.predict(x_test))

from sklearn.model_selection import GridSearchCV
p = {'max_features': ['auto', 'sqrt', 'log2'],
              'max_depth' : [3,4,5, 6, 7, 8, 9],
              'criterion' :['gini', 'entropy']}
gsc = GridSearchCV(DecisionTreeClassifier(),param_grid=p, cv=5, verbose=True)
gsc.fit(x_train,y_train)
gsc.best_estimator_
ok= DecisionTreeClassifier(max_depth=7, max_features='auto')
ok.fit(x_train,y_train)
accuracy_score(y_train,ok.predict(x_train))
accuracy_score(y_test,ok.predict(x_test))



from sklearn.linear_model import LogisticRegression
log= LogisticRegression().fit(x_train,y_train)
accuracy_score(y_train,log.predict(x_train))
accuracy_score(y_test,log.predict(x_test))


# data.drop(labels=['output','Timestamp', 'Name :'],axis=1).columns
# x=data.drop(labels=['output','Timestamp', 'Name :'],axis=1)
# y= data[['output']]

# import statsmodels.formula.api as sm
# model = sm.logit('y.columns ~ x.columns', data= data).fit()

# #summary
# model.summary2() # for AIC
# model.summary()



import pickle
pickle.dump(log,open('model.pkl','wb'))
