import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap

db = pd.read_csv("cab_data.csv")
print(db)  # Img_1

print(db.duplicated().sum())  # Img_2

print(db.dtypes)  # Img_3
db['Date/Time'] = pd.to_datetime(db['Date/Time'])
db['month'] = db['Date/Time'].dt.month_name()
print(db['month'].value_counts())  # Img_4

db['month'].value_counts().plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Value Counts of Months')
plt.show()  # Img_5

db['weekday'] = db['Date/Time'].dt.day_name()
db['day'] = db['Date/Time'].dt.day
db['hour'] = db['Date/Time'].dt.hour
db['minute'] = db['Date/Time'].dt.minute
print(db.head())  # Img_6

piv = pd.crosstab(index=db['month'], columns=db['weekday'])
print(piv)  # Img_7

piv.plot(kind='bar', figsize=(8, 6))
plt.show()  # Img_8

together = db.groupby(['weekday', 'hour'], as_index=False).size()
print(together)  # Img_9

plt.figure(figsize=(10, 6))
sns.pointplot(x='hour', y='size', hue='weekday', data=together)
plt.show()  # Img_10

final = pd.read_csv("cab_data.csv")
rush = final.groupby(['Lat', 'Lon'], as_index=False).size()
base_map = folium.Map(location=[rush['Lat'].mean(), rush['Lon'].mean()], zoom_start=8)
heat_data = [[row['Lat'], row['Lon'], row['size']] for index, row in rush.iterrows()]

HeatMap(heat_data).add_to(base_map)

base_map.save('heatmap.html')  # Img_11
