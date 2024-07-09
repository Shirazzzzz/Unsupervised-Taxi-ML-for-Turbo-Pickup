# Urban-Mobility-Patterns-Unsupervised-Learning-Insights-from-Taxi-Data to boost Pickup and efficiency



https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/30bc2bef-9a42-4c40-a997-6268057fd403

Above video is just an example of how this project can be used.
(For my usecase dataset the range for optimal clusters was 4 to 6)

.............................................
Playing with Data 1 (and Visualization) [requires lat/lon type dataset] 
.............................................

This Python script performs comprehensive analysis of ride-sharing data using pandas, seaborn, matplotlib, and folium libraries. The script begins by loading the dataset into a pandas DataFrame, checking for and counting any duplicate entries to ensure data integrity. It then displays the data types of each column for initial inspection to understand the structure of the dataset.

For example:
![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/37c07ac5-16c1-423a-9443-a91a34532a8f)
The stark contrast between weekdays (Monday to Friday) and weekends (Saturday and Sunday) becomes evident around 7 am (hour 7), attributed to the number of people commuting to work on weekdays compared to weekends. Similarly, the peak at 5 pm (hour 5) reflects people leaving their workplaces and returning home.
This 5 pm peak indicates a significant number of bookings made by individuals as they finish their workday. A substantial portion of this data is contributed by "9 to 5" working professionals, highlighting the influence of typical work hours on cab booking patterns.

![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/144ecd3f-15ae-4407-99f6-86b25a3128be)

![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/63204835-fe20-4b94-b88d-95c869b959dc) ![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/77afd630-75dc-4fd5-88de-08459c60d392)




...................................................
Playing with Data 2 (and Visualization) [requires Dispatch type dataset] 
.............................................

![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/c917963e-5da6-468a-b4f4-bd6bbf3c0259)

• Variation in Dispatching Base Activity: The dispatching base B02764 stands out due to its wide distribution, indicating that it handles a much larger and more variable number of active vehicles compared to other bases.
• Consistency in Smaller Bases: Bases like B02512, B02765, B02682, B02617, and B02598 show narrower distributions, suggesting that these bases have more consistent and smaller numbers of active vehicles.
• Operational Focus: The wide distribution for B02764 might indicate a high-demand area or a larger operational focus, whereas the narrower distributions for other bases might suggest more localized or less variable demand.


![image](https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/ad0af2f0-2ec8-4a31-89cf-94017476d8e7)

• Variation in Dispatching Base Activity: B02764 has the highest median and the widest IQR, suggesting that this base handles a large and variable number of active vehicles.

• Consistency in Smaller Bases: Bases like B02512, B02765, B02682, B02617, and B02598 have lower medians and narrower IQRs, indicating more consistent and smaller numbers of active vehicles.
• Operational focus: The high variability and large number of active vehicles for B02764 might indicate a high-demand area or a larger operational focus, while other bases show more stable and lower demand.


These visualizations help in understanding the distribution and density of active vehicles across different dispatching bases. The HTML files can be easily shared or embedded in reports and presentations.


.............................................
main [requires dataset with lat/lon values] 
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

