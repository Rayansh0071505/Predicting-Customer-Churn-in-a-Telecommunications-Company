from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np 


def model_training(X_train,X_test,y_train,y_test):
    """
    Fits and evaluate given ml model
    models: a dictionary of different scilit-learn machine learning models
    x_train : training data
    x_test : testing data
    """
    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'Gradient Boosting': GradientBoostingClassifier(),
        'SVM': SVC(),
        'K-Nearest Neighbors': KNeighborsClassifier(),
        'Naive Bayes': GaussianNB()
    }
    # set up random seed
    np.random.seed(42)
    # Make a dicitionary to keep models
    model_score = {}
    # Loop through models
    for name, model in models.items():
        #Fit the model to data
        model.fit(X_train,y_train)
        # Evaluate the model and append its score to model_score
        model_score[name]=model.score(X_test,y_test)
    return model_score
