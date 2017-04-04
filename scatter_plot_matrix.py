# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "bank_trans.csv"
names = ['CUST_ID','SAL','TXN_TYPE','TXN_DATE','TXN_CREDIT_CNT','SUM_AMT','FRAUD_FLAG']
dataset = pandas.read_csv(url, names=names)

# scatter plot matrix
scatter_matrix(dataset)
plt.show()