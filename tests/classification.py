from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score   
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier 

df = pd.read_csv('kc2.csv', header = 0)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

def get_train_test_split(X,y, t_size = 0.33, rand_state = 1234567891):
    return train_test_split(
    X, y, test_size=0.33, random_state=42
)
X_train, X_test, y_train, y_test = get_train_test_split(X,y)
print(X_train.info())

print(y_train.info())
def build_model(X_train, y_train, model, **params):
    model_nb = model
    if params: model.set_params(**params)
    model_nb.fit(X_train, y_train)
    return model
def predict(model, X_test):
    return model.predict(X_test)

def stats(y_pred, y_test):
    print("Accuracy Score:", accuracy_score(y_pred, y_test))
    print(classification_report(y_pred, y_test))

args = {"n_estimators":10}    
modelrf = build_model(X_train, y_train,RandomForestClassifier(),**args)
args = {"n_neighbors":10}    
modelknn = build_model(X_train, y_train,KNeighborsClassifier(),**args)
modelNB = build_model(X_train, y_train,GaussianNB())
stats(predict(modelrf, X_test),y_test)
stats(predict(modelknn, X_test),y_test)
stats(predict(modelNB, X_test),y_test)