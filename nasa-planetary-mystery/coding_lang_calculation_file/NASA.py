import pandas as pd
import plotly.express as px
df = pd.read_csv('datasets/planet_weather.csv')
df.head()
df.shape
df.columns
df.info()
df.isnull().sum()
df.describe()
df = df.drop(columns=['wind_speed'])
df.head()
df['atmo_opacity'].value_counts()
df = df.drop(columns=['atmo_opacity'])
df.head()
df['month'].nunique()
avg_min_temp = df.groupby('month').agg({'min_temp':'mean'})
px.bar(avg_min_temp, title="Average Minimum Temperature for Each Month")
avg_pressure = df.groupby('month').agg({'pressure':'mean'})
px.bar(avg_pressure, title="Average Pressure for Each Month")
px.line(df, x='terrestrial_date', y='pressure', title="Daily Atmospheric Pressure by Date")
px.line(df, x='terrestrial_date', y='min_temp', title="Daily Minimum Temperature by Date")
before_2014 = df[df['terrestrial_date'] < '2014']
before_2014
before_2014.groupby('month').agg({'terrestrial_date': ['min', 'max']})