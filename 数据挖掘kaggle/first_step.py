import numpy as np
import pandas as pd
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt
train = pd.read_csv('train.csv')
# test = pd.read_csv('test.csv')
#
# display(train.head(n=1))
# train.info()

train = train.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
# test.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# sns.countplot(x='Pclass', hue='Survived', data=train)
# sns.violinplot(x='Survived', y='Age', data=train)
# plt.show()

# 0.Pclass&Fare

# 1.Embarked
# print(train['Embarked'][train['Embarked'].isnull()])
# print(train.groupby('Embarked')['Survived'].count())
train['Embarked'] = train['Embarked'].fillna("S")
Embarked_into_digi = {'S': 1, 'C': 10, 'Q': 100}
train['Embarked'] = train['Embarked'].map(Embarked_into_digi)

# 2.SibSp&Parch
train['Relatives'] = train['SibSp'] + train['Parch']
train = train.drop(['SibSp', 'Parch'], axis=1)

# 3.Sex
def get_person(people):
    age, sex = people
    return 'Child' if age < 16 else sex
train['Person_sex'] = train[['Age', 'Sex']].apply(get_person, axis=1)
train = train.drop(['Sex'], axis=1)
sex_into_digi = {'male': 1, 'female': 0, 'Child': -1}
train['Person_sex'] = train['Person_sex'].map(sex_into_digi)

# 4.Age
avgerage_age = train['Age'].mean()
std_age = train['Age'].std()  # 方差
count_age = train['Age'].isnull().sum()

rand_age = np.random.randint(avgerage_age - std_age, avgerage_age + std_age, count_age)
train['Age'][np.isnan(train['Age'])] = rand_age
train['Age'] = train['Age'].astype(int)

y_train = train['Survived']
x_train = train.drop(['Survived'], axis=1)

# print(y_train)
# print(x_train['Person_sex'])
# print(x_train.describe())



