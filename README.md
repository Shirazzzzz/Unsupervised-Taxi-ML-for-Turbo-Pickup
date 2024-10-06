# Urban-Mobility-Patterns-Unsupervised-Learning-Insights-from-Taxi-Data to boost Pickup and efficiency



https://github.com/Shirazzzzz/Unsupervised-Taxi-ML-for-Turbo-Pickup/assets/97777320/30bc2bef-9a42-4c40-a997-6268057fd403

Above video is a hourly dynamic plot fine tuned for big companies like uber that can afford to allocate their resources across multiple clusters.
The entire geography of New York City is divided into 8 broad clusters using k-means. 

Different clustering algorithms produce different types of clusters, but it is our responsibility to pick the best algorithm. But how do we do that?
We apply different algoirthms onto our dataset and decide which one suits our needs. Every type of cluster is a cluster, but our needs define what algorithm we'll pick.

<div style="align: center;"><img width="194" alt="image" src="https://github.com/user-attachments/assets/6ae1862f-6a06-4c78-9ced-1059e7f1a277"></div>

The above image shows how k-means and density based algorithms treat the same dataset. Again, no cluster is inherently "bad", but the result produced by k-means is what we are looking for (when it comes to dividing the area into broad clusters).


  <img width="281" alt="image" src="https://github.com/user-attachments/assets/706fc81c-f098-4edf-beb1-793dc6e967f1"> <img width="295" alt="image" src="https://github.com/user-attachments/assets/23a88dfd-e433-45bf-96e7-8469ac0c13b2">

  
The graphs above show the elbow plot and silhoette score plot.
The graphs suggest that the optimal number of k-means cluster = 2 ...
But how is that insightful or of any use?
Its like saying allocate 60% of cabs to North India and 40% to South India, but we need to be more specific and strike a balance between whats optimal and whats practical
Thats why we look at the next best option which is 8. Therefore we divide the region into 8 broad clusters using k-means.


Now that we have our broad clusters we now look for an algorithm to form clusters within each broad cluster. Refering back to the discussion on types of clusters, i realised that a density-based algorithm matches my needs ... but which one ?

<br>

<img width="282" alt="image" src="https://github.com/user-attachments/assets/46e8e79f-4e56-4188-9fb8-d3060e39c454">  <img width="281" alt="image" src="https://github.com/user-attachments/assets/d53e8b3e-b273-4986-ad31-21c94a6da5d3">
<br>
HDBSCAN was chosen for this part of the project as its a better match for the needs. It is a hierarchial algorithm that makes use of Minimum Spanning Trees to form clusters.
<br>
<img width="413" alt="image" src="https://github.com/user-attachments/assets/b7b80ee4-fd16-48c8-8fef-ca7ea5ba94a6">
<br>
MST in HDBSCAN

Next part of the project is to fine tune the parameters for the parameters for forming clusters with HDBSCAN. 
<br>
In this part we need to address 2 issues : 1)finding better ways to fine tune the parameters, and 2) fine tuning for different needs (Small Businesses and Big Businesses)
<br>
<br>
1)Binary Search on a 2D grid

Fine tuning min_samples and min_size for HDBSCAN on such a large dataset was computationally expensive, so i couldnt just go about trying different values as each run took around 30 minutes. So i figured out the ranges for the both the parameters in which the most optimal clusters would lie and performed a binary search on both of them to get the most optimal clusters with log(R) attempts for each (R = range), thereby making the process efficient.
<br>
2) Different types of business have different needs

A small business with just 30 cabs cannot afford to allocate its cab across 27 clusters as that wont be fruitful (approx. 1 cab per cluster), so the pickup coordinates must be rounded off to a certain degree to form bigger and more general clusters, and then i picked ONLY 2 of these bigger clusters. Parameters must be manually fine tuned 
for this.

<br>
<!-- https://github.com/user-attachments/assets/d29fc014-391c-4c6b-8799-bebaf063881d -->

Example: 16 cabs in North-East Delhi Region and 14 cabs in North-West Delhi Region.

<br>
A bigger business like uber on the other hand can afford to split lets say a cab force of 40k across 27 clusters.
<br>
<!-- https://github.com/user-attachments/assets/d53fa72e-4e82-4fdd-aa3e-146761a7675d -->
<br>
For each category: Weekly and Hourly Dynamic Plots were produced + Output was also logged for better readibility.

Example:
<br>
<img width="235" alt="image" src="https://github.com/user-attachments/assets/8ab17179-b036-4880-90ed-09ca6ed5fd82"> <img width="181" alt="image" src="https://github.com/user-attachments/assets/34c6c113-a5b6-4eec-9ec5-ec739d365a50">
<br>
<br>
I was also able to achieve an average cluster score of 1 (perfect) for both small and big businesses.
<br>
Image 1 = Big business                             Image 2 = Small Business
<br>
<br>
<img width="225" alt="big business validation" src="https://github.com/user-attachments/assets/259a41ec-ebce-4714-ba0f-b1e3eb2ef5b1"> 
<img width="218" alt="small business validation" src="https://github.com/user-attachments/assets/e5b05750-f6c3-432f-bfa7-f4862598b8a4">
<br>

Here ive described some other insights from the data:
<br>
<br>

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



