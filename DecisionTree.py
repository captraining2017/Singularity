# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier , export_graphviz
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import os
import pydotplus 

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

# Load dataset
url = "bank_trans.csv"
names = ['CUST_ID','SAL','TXN_TYPE','TXN_DATE','TXN_CREDIT_CNT','SUM_AMT','FRAUD_FLAG']
dataset = pandas.read_csv(url, names=names)

array = dataset.values
X = array[:,0:6]
Y = array[:,6]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


with open("iris.dot", 'w') as f:	
	f = tree.export_graphviz(clf, out_file=f)

os.unlink('iris.dot')

from IPython.display import Image  
dot_data = tree.export_graphviz(clf)  
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png())  

