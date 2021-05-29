import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("marks.csv")
fig = px.bar(df, x = "Marks In Percentage", y = "Days Present", color = "Roll No")
fig.show()