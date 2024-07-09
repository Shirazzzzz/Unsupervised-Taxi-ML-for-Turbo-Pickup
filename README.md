# Urban-Mobility-Patterns-Unsupervised-Learning-Insights-from-Taxi-Data to boost Pickup and efficieny



https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/30bc2bef-9a42-4c40-a997-6268057fd403

Above video is just an example of how this project can be used.
(For my usecase dataset the range for optimal clusters was 4 to 6)


.............................................
Code 3 (requires dataset with lat/lon values) 
.............................................

<img width="294" alt="q6" src="https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/07099433-2683-49a7-9e6b-efe2dbf578b9">  <img width="286" alt="qq3" src="https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/fe388bc0-d7ee-4fd2-bf52-705198ddb345">

Percentage of Cab Strength that must alloted to clusters at any given time of the day or day of the week to boost pickup.

This code performs comprehensive data analysis and clustering on cab data, focusing on temporal and spatial patterns.

Data Preprocessing
Load and Clean Data: The dataset is loaded from cab_data.csv. The Date/Time column is converted to datetime format, and new columns for Day_of_Week and Hour are created. Unnecessary columns are dropped.

Clustering and Analysis
KMeans Clustering: A sample of 300,000 rows is standardized and clustered into 12 groups using KMeans. Cluster centers and assignments are stored.
DBSCAN Clustering: DBSCAN is applied to identify dense regions and noise, with the percentage of noise points calculated.

Optimization and Visualization
Cluster Optimization: The optimal number of clusters is determined using the elbow method (WCSS) and silhouette scores.
Hourly and Daily Clustering: Clusters are analyzed for each hour of the day and each day of the week. Cluster centers are reverse geocoded to identify neighborhoods.

Usage
Visualizations: The results are visualized using interactive scatter maps, showing cluster distributions across hours and days. These maps are saved as HTML files for easy sharing and analysis.

This code can be used to identify temporal and spatial hotspots in cab data, helping to understand patterns and optimize cab dispatching. The visualizations provide intuitive insights into how cab demand varies over time and location.
