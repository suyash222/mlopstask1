import pandas

data_set = pandas.read_csv("SalaryData.csv")

x = data_set['YearsExperience'].values.reshape(-1, 1)
y = data_set['Salary']

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x, y)

while True:

    predict = input("Enter years of experiences to predict salary or type exit to close the code: ")
    if predict == 'exit':
        break
    try:
        print(model.predict([[int(predict)]]))
    except ValueError:
        break