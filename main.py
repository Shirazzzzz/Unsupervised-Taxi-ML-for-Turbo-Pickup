import plotly.express as px
import pandas as pd
from plotly.offline import plot

db = pd.read_csv("cab_data_2.csv")
print(db.head())  # Img_12


box = px.box(db, x='dispatching_base_number', y='active_vehicles', title='Box Plot')
plot(box, filename='db_box_plot.html')  # Img_13


violin = px.violin(db, x='dispatching_base_number', y='active_vehicles', title='Violin Plot')
plot(violin, filename='db_violin_plot.html')  # Img_14
