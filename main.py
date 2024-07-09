import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from geopy.geocoders import Nominatim

pd.options.display.max_columns = None
pd.set_option('display.max_rows', 500)

df = pd.read_csv("cab_data.csv")

# print(df.head())  # Img_16

df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Day_of_Week'] = df['Date/Time'].dt.dayofweek
df['Hour'] = df['Date/Time'].dt.hour
df_clean = df.drop(['Date/Time', 'Base'], axis=1)

sample = df.sample(10000)
sample = sample.sort_values("Hour", ascending=True)

# fig = px.density_mapbox(sample, lat='Lat', lon='Lon',
#                         mapbox_style="carto-darkmatter", zoom=9,
#                         color_continuous_scale='magma', opacity=0.6, radius=15)
# fig.update_layout(width=1100, height=700)
# fig.show()  # Img_17

sample = df_clean.sample(300000)
scaler = StandardScaler()
X_all = scaler.fit_transform(sample)
# print(X_all[:5])  # Img_18

kmeans = KMeans(n_clusters=12, random_state=0)
kmeans.fit(X_all)
cluster_centers_all = scaler.inverse_transform(kmeans.cluster_centers_)
c = kmeans.predict(X_all)

df_cleaned_all = sample.copy()
df_cleaned_all['cluster_id'] = c
figure_sample = df_cleaned_all.sample(20000)

# check = px.scatter_mapbox(figure_sample, lat='Lat', lon='Lon', mapbox_style="carto-darkmatter",
#                           zoom=10, color='cluster_id', width=1200, height=700)
# check.show()  # Img_19
# print(X_all.shape)  # Img_20

db = DBSCAN(eps=0.20, min_samples=20)
db.fit(X_all)
sample_db = sample.copy()
sample_db['Cluster_id'] = db.labels_
sample_db['Cluster_id'].value_counts() / sample_db.shape[0] * 100

sample_db_f = sample_db.loc[sample_db['Cluster_id'] >= 0, ['Lat', 'Lon', 'Day_of_Week', 'Hour']]
cluster_counts = sample_db['Cluster_id'].value_counts()
num_noise_points = (sample_db['Cluster_id'] == -1).sum()
percent_noise_points = num_noise_points / sample_db.shape[0] * 100
# print(f"Number of rows: {sample_db_f.shape[0]}")
# print("------head------")
# print(sample_db_f.head())
# print("----------------")
# print(f"Number of noise points: {num_noise_points}")
# print(f"Percentage of noise points: {percent_noise_points:.2f}%")  # Img_21

wcss = []
k = []
h = 12
scaler_2 = StandardScaler()
sample_db_f = sample_db_f.sort_values('Hour')
X_h = sample_db_f.loc[sample_db_f['Hour'] == h, ['Lat', 'Lon']]
X_h_n = scaler_2.fit_transform(X_h)

for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_h)
    wcss.append(kmeans.inertia_)
    k.append(i)
    # print("WCSS for K={} --> {}".format(i, wcss[-1]))  # Img_22

wcss_frame = pd.DataFrame(wcss)
k_frame = pd.Series(k)
# display_k = px.line(wcss_frame, x=k_frame, y=wcss_frame.iloc[:, -1])
#
# display_k.update_layout(yaxis_title="Inertia", xaxis_title="# Clusters", title="Inertia per cluster")
# display_k.show()  # Img_23

sil = []
k = []
for i in range(2, 20):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_h_n)
    sil.append(silhouette_score(X_h_n, kmeans.predict(X_h_n)))
    k.append(i)
    # print("Silhouette score for K={} is {}".format(i, sil[-1]))  # Img_24

cluster_scores = pd.DataFrame(sil)
k_frame = pd.Series(k)

# fig = px.bar(data_frame=cluster_scores, x=k, y=cluster_scores.iloc[:, -1])
# fig.update_layout(yaxis_title="Silhouette Score", xaxis_title="# Clusters", title="Silhouette Score per cluster")
# fig.show()  # Img_25


scaler_2 = StandardScaler()
labels_hour = []
coord_hour = {}
cluster_size = {}
sample_db_f = sample_db_f.sort_values('Hour')

# Dictionary to hold percentage information
percentage_clusters = {}

for i in range(0, 24):
    X_i = sample_db_f.loc[sample_db_f['Hour'] == i, ['Lat', 'Lon']]
    X_i_n = scaler_2.fit_transform(X_i)
    kmeans = KMeans(n_clusters=12, random_state=0)
    kmeans.fit(X_i_n)
    labels = kmeans.labels_.tolist()
    X_i['cluster_id'] = labels
    coordinates = kmeans.cluster_centers_
    coord_hour[i] = scaler_2.inverse_transform(coordinates)
    cluster_counts = X_i['cluster_id'].value_counts(sort=False).sort_index()
    cluster_size[i] = cluster_counts.to_numpy()
    total_points = cluster_counts.sum()
    percentage_clusters[i] = (cluster_counts / total_points * 100).to_numpy()
    labels_hour.extend(labels)

clusters = np.array([[0, 0, 0, 0]])
for i in range(0, 24):
    cluster_data = np.concatenate([np.full((12, 1), i), coord_hour[i], cluster_size[i].reshape(12, 1)], axis=1)
    clusters = np.concatenate([clusters, cluster_data], axis=0)

clusters = np.delete(clusters, 0, 0)
np.set_printoptions(suppress=True)
hour_hotspots = pd.DataFrame(clusters, columns=['Hour', 'Lat', 'Lon', 'Size'])

# Reverse geocoding
neighborhood = []
geolocator = Nominatim(user_agent="NY_hotspots")

for lat, lon in hour_hotspots.loc[:, ['Lat', 'Lon']].to_numpy():
    location = geolocator.reverse(f"{lat:.3f}, {lon:.3f}")
    try:
        neighborhood.append(location.raw['address']['neighbourhood'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['quarter'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['aeroway'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['amenity'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['suburb'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['commercial'])
        continue
    except KeyError:
        pass
    neighborhood.append(f"{lat} {lon}")

hour_hotspots['Location'] = neighborhood

# Printing the percentage of values in each cluster for each hour
for hour, percentages in percentage_clusters.items():
    print(f"Hour {hour}:")
    for cluster_id, percentage in enumerate(percentages):
        print(f"  {hour_hotspots.iloc[cluster_id]['Location']}: {percentage:.2f}%")

color_sequence = px.colors.qualitative.Plotly
fig = px.scatter_mapbox(hour_hotspots, lat='Lat', lon='Lon', size='Size', color='Size', hover_name='Location',
                        hover_data={"Size": False, "Hour": False, "Lat": False, "Lon": False},
                        animation_frame='Hour',  # color_continuous_scale=color_sequence,
                        size_max=50,
                        mapbox_style="carto-darkmatter", zoom=10,
                        width=1000, height=700)
fig.update_layout(margin={"r": 0, "t": 150, "l": 0, "b": 0})
fig.write_html("Hourly.html")
fig.show()

scaler_3 = StandardScaler()
labels_week = []
coord_week = {}
cluster_size_week = {}
sample_db_f = sample_db_f.sort_values('Day_of_Week')

# Clustering for each day of the week
for i in range(0, 7):
    X_i = sample_db_f.loc[sample_db_f['Day_of_Week'] == i, ['Lat', 'Lon']]
    X_i_n = scaler_3.fit_transform(X_i)
    kmeans = KMeans(n_clusters=12, random_state=0)
    kmeans.fit(X_i_n)
    labels = kmeans.labels_.tolist()
    X_i['cluster_id'] = labels
    coordinates = kmeans.cluster_centers_
    coord_week[i] = scaler_3.inverse_transform(coordinates)
    cluster_size_week[i] = X_i['cluster_id'].value_counts(sort=False).sort_index().to_numpy()
    labels_week.extend(labels)

clusters_week = np.array([[0, 0, 0, 0]])
for i in range(0, 7):
    cluster_data = np.concatenate([np.full((12, 1), i), coord_week[i], cluster_size_week[i].reshape(12, 1)], axis=1)
    clusters_week = np.concatenate([clusters_week, cluster_data], axis=0)

clusters_week = np.delete(clusters_week, 0, 0)
np.set_printoptions(suppress=True)
week_hotspots = pd.DataFrame(clusters_week, columns=['Day_of_Week', 'Lat', 'Lon', 'Size'])

# Reverse geocoding
geolocator = Nominatim(user_agent="NY_hotspots")
neighborhood = []
for lat, lon in week_hotspots.loc[:, ['Lat', 'Lon']].to_numpy():
    location = geolocator.reverse(f"{lat:.3f}, {lon:.3f}")
    try:
        neighborhood.append(location.raw['address']['neighbourhood'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['quarter'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['aeroway'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['amenity'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['suburb'])
        continue
    except KeyError:
        pass
    try:
        neighborhood.append(location.raw['address']['commercial'])
        continue
    except KeyError:
        pass
    neighborhood.append(f"{lat:.3f}, {lon:.3f}")

week_hotspots['Location'] = neighborhood

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Calculate and print percentage of bookings in each cluster for each day of the week
total_bookings_per_day = sample_db_f['Day_of_Week'].value_counts().sort_index().to_numpy()
for i in range(7):
    print(f"{weekday_names[i]}: ")
    cluster_percentages = (cluster_size_week[i] / total_bookings_per_day[i]) * 100
    for cluster_id, percentage in enumerate(cluster_percentages):
        location_name = week_hotspots[
            (week_hotspots['Day_of_Week'] == i) & (week_hotspots['Size'] == cluster_size_week[i][cluster_id])][
            'Location'].values[0]
        print(f"  {location_name}: {percentage:.2f}%")
    print()

color_sequence = px.colors.qualitative.Plotly

final = px.scatter_mapbox(week_hotspots, lat='Lat', lon='Lon', size='Size', color='Size',
                          hover_name='Location', animation_frame='Day_of_Week', size_max=50,
                          # color_continuous_scale=color_sequence,
                          mapbox_style="carto-darkmatter", zoom=10,
                          width=1000, height=700)
final.update_layout(margin={"r": 0, "t": 150, "l": 0, "b": 0})
final.write_html("Weekly.html")
final.show()
