import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('2022_02_08-02_30_31_AM.csv')
print(df)

#Generating Report
profile = ProfileReport(df)
profile.to_file(output_file="report.html")