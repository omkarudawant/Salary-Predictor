# Importing the libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pandas import read_csv
import joblib


# Importing the dataset
dataset = read_csv('../input/Salary_Data.csv')
X = dataset.drop(['Salary'], axis=1).values
y = dataset['Salary'].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.1,
                                                    random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Saving model to disk
joblib.dump(regressor, '../model/model.joblib')
