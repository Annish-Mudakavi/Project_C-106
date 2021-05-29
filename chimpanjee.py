import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getdatasource(data_path):
    sizeoftv = []
    avgtimespent = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            sizeoftv.append(float(i["Average time spent watching TV in a week"]))
            avgtimespent.append(float(i["Size of TV"]))
    return{"x":sizeoftv, "y": avgtimespent}
def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])
def start():
    data_path = "./tv.csv"
    data_source = getdatasource(data_path)
    findcorrelation(data_source)
start()