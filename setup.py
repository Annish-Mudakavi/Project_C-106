import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getdatasource(data_path):
    icecreamsales = []
    colddrinks = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            icecreamsales.append(float(i["Temperature"]))
            colddrinks.append(float(i["Ice-cream Sales"]))
    return{"x":icecreamsales, "y":colddrinks}
def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])
def start():
    data_path = "./icecreamsales.csv"
    data_source = getdatasource(data_path)
    findcorrelation(data_source)
start()