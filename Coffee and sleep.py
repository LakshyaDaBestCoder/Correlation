import csv
import numpy as np

def getDataSource(data_path):
    coffee_in_ml = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Marks In Percentage"]))
            hours_of_sleep.append(float(row["Days Present"]))

    return {"x" : coffee_in_ml, "y": hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = r"C:\Users\lenovo\Desktop\Python\Class 106\data\cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()