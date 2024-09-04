import pandas as pd

students = pd.read_csv('./challenge_day2/students.csv', header=None)

students.columns = ['name', 'LT']

students['name'] = students['name'].apply(lambda x: x.split()[0])
students['LT'] = students['LT'].apply(lambda x: x.split()[2])

def solution_station_5(name):

    if name == "Emma":
        name = "Emma-Rose"

    return int(students[students['name'] == name]['LT'].values[0])