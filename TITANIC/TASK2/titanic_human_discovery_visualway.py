# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:24:27 2020

@author: Monika
"""

import pandas as pd
import seaborn as sns

#m- stands for module
abspath = "C:\\Users\\Jeevan\\Desktop\\Monika\\"

titanic_train = pd.read_csv(abspath+"TITANIC\\titanic_train.csv")
print(titanic_train.shape)
print(titanic_train.info())

#visual discovery of pattern
##univariate plots
#categorical columns: count/bar plot
#x: categories of feature, y: frequency
sns.countplot(x='Survived',data=titanic_train)
sns.countplot(x='Pclass',data=titanic_train)
sns.countplot(x='Sex',data=titanic_train)

#histogram to undertand continuous feature
#x: bins of continuous data, y: frequency
#issue: how do you select number of bins?
sns.distplot(titanic_train['Fare'], kde=False)
sns.distplot(titanic_train['Fare'], kde=True)
sns.distplot(titanic_train['Fare'], bins=20, rug=False, kde=False)
sns.distplot(titanic_train['Fare'], bins=20)
sns.distplot(titanic_train['Fare'], bins=100, kde=False)
#density plot to understand continuous feature
#it doesnt require bins argument
#x: fare y:density
sns.distplot(titanic_train['Fare'], hist=False)
sns.distplot(titanic_train['Fare'])
#box-whisker plot to understand continuous feature
sns.boxplot(x='Fare',data=titanic_train)

titanic_test = pd.read_csv(abspath+"TITANIC\\titanic_test.csv")
print(titanic_test.shape)

titanic_test['Survived'] = 0
titanic_test['test'] = 23
titanic_test.loc[titanic_test.Sex=='female', ['Sex','Survived']]

titanic_test.to_csv(abspath+"TITANIC\\TASK2\\titanic_submission.csv",columns=['PassengerId','Survived','test'], index=False)
#bi variate plots
sns.catplot(data=titanic_test,x='Sex')
