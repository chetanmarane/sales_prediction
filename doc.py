# necessary Imports
import pandas as pd
# import matplotlib.pyplot as plt
import pickle
# % matpllotlib inline

data= pd.read_csv('Advertising.csv')

# create X and y
feature_cols = ['TV', 'radio', 'newspaper']
X = data[feature_cols]
y = data.sales


from sklearn.model_selection import train_test_split
x_train,x_test,y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=100)


# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x_train, y_train)

# calucltaing the accuracy of the model
from sklearn.metrics import r2_score
score= r2_score(lm.predict(x_test),y_test)

# saving the model to the local file system
filename = 'finalized_model.pickle'
pickle.dump(lm, open(filename, 'wb'))

# prediction using the saved model.
loaded_model = pickle.load(open(filename, 'rb'))
prediction=loaded_model.predict(([[320,120,5]]))
print(prediction[0])