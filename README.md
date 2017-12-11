
# Pyber Ride Sharing
## Analysis
* The most clear observation made from the data provided is that there is a large difference, on average, in the amount of rides made amongts the three different city types provided.
    * Urban cities use this service a lot more than the other two city types combined.
    * There is a large demand for this this service which is demonstrated by the heavy use it, and as a result from the a high demand is the large supply of drivers.
    * There may be a strong positive correlation between number of rides per city and drivers per city.
* The fare costs vary vastly between the three city types.
    * I believe that there may be a postive correlation between fare cost and distance driven to reach the final destination.
    * There may also be a negative correlation between number of rides and miles driven per ride, which may indicate that this service is optimal for short duration rides. To further investigate this hypothesis I would need data on mileage or time spent per ride.
* There are some outliers in this data that also needs to be explored, for instance there is a suburban city in this data that outperforms all of the cities, including all of the urban cities, in respect to the total number of rides provided. What is strange about this data point is that even though this city is number one in the amount of rides provided it has a very small amount of drivers providing those rides.


```python
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from axis_generator import city_type_plots, city_type_perc
```


```python
file_name1 = 'city_data.csv'
file_name2 = 'ride_data.csv'

csv_path1 = path.join('..','raw_data',file_name1)
csv_path2 = path.join('..','raw_data',file_name2)
```


```python
city_df = pd.read_csv(csv_path1)
ride_df = pd.read_csv(csv_path2)
```


```python
city_ride_df = pd.merge(ride_df, city_df, how='outer', on='city', sort=True)
city_ride_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>2016-04-18 20:51:29</td>
      <td>31.93</td>
      <td>4267015736324</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alvarezhaven</td>
      <td>2016-08-01 00:39:48</td>
      <td>6.42</td>
      <td>8394540350728</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alvarezhaven</td>
      <td>2016-09-01 22:57:12</td>
      <td>18.09</td>
      <td>1197329964911</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alvarezhaven</td>
      <td>2016-08-18 07:12:06</td>
      <td>20.74</td>
      <td>357421158941</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alvarezhaven</td>
      <td>2016-04-04 23:45:50</td>
      <td>14.25</td>
      <td>6431434271355</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>



## Bubble Plot of Ride Sharing Data


```python
# seperate each city type into individual dataframes
urban_df =    city_ride_df.loc[city_ride_df['type'] == 'Urban']
suburban_df = city_ride_df.loc[city_ride_df['type'] == 'Suburban']
rural_df =    city_ride_df.loc[city_ride_df['type'] == 'Rural']
```


```python
# use function to generate axis lists
urban_city_rides_axis, urban_city_fare_axis, urban_city_driver_axis = city_type_plots(urban_df)
suburban_city_rides_axis, suburban_city_fare_axis, suburban_city_driver_axis = city_type_plots(suburban_df)
rural_city_rides_axis, rural_city_fare_axis, rural_city_driver_axis = city_type_plots(rural_df)
```


```python
# plot the graph
plt.figure(figsize=(12,10))

# urban plot
plt.scatter(urban_city_rides_axis, urban_city_fare_axis,s=[x*5 for x in urban_city_driver_axis], 
                 edgecolors='black', facecolor='lightcoral', alpha=.6, zorder=3,  label='Urban')

# suburban plot
plt.scatter(suburban_city_rides_axis, suburban_city_fare_axis,s=[x*5 for x in suburban_city_driver_axis], 
                 edgecolors='black', facecolor='lightskyblue', alpha=.6, zorder=3,  label='Suburban')

# rural plot
plt.scatter(rural_city_rides_axis, rural_city_fare_axis,s=[x*5 for x in rural_city_driver_axis], 
                 edgecolors='black', facecolor='gold', alpha=.6, zorder=3,  label='Rural')


plt.xlim(0, max(max(suburban_city_rides_axis),max(urban_city_rides_axis),max(rural_city_rides_axis)) + 2)
plt.ylim(min(min(suburban_city_fare_axis),min(urban_city_fare_axis),min(rural_city_fare_axis)) - 2,
         max(max(suburban_city_fare_axis),max(urban_city_fare_axis),max(rural_city_fare_axis)))

plt.xticks(np.linspace(0,max(max(suburban_city_rides_axis),max(urban_city_rides_axis),max(rural_city_rides_axis)) + 2, 10, dtype=int))
plt.yticks(np.linspace(min(min(suburban_city_fare_axis),min(urban_city_fare_axis),min(rural_city_fare_axis)) - 2,
                       max(max(suburban_city_fare_axis),max(urban_city_fare_axis),max(rural_city_fare_axis)) + 2, 10, dtype=int))

plt.title('Pyber Ride Sharing Data (2016)', size=18)
plt.xlabel('Total Number of Rides (Per City)', size=14)
plt.ylabel('Average Fare ($)', size=14)
plt.annotate('Note:\nCircle size correlates with driver count per city',
            xy=(1, 0.5), xytext=(5, 10), xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points', size=12)
lgnd = plt.legend(fontsize=12, markerscale=1, frameon=False, title='City Types')
plt.setp(lgnd.get_title(),fontsize=14)
lgnd.legendHandles[0]._sizes = [100]
lgnd.legendHandles[1]._sizes = [100]
lgnd.legendHandles[2]._sizes = [100]

plt.grid(color='lightgray', zorder=0)
plt.show()
```


![png](output_8_0.png)


## Pie Charts for Percent Comparison


```python
# use function to generate axis zipped list
urban_percs =    city_type_perc(urban_df, 'Urban', city_ride_df)
suburban_percs = city_type_perc(suburban_df, 'Suburban', city_ride_df)
rural_percs =    city_type_perc(rural_df, 'Rural', city_ride_df)

zippidie_doo_dah = list(zip(urban_percs, suburban_percs, rural_percs))
```


```python
# pie attributes
labels = ['Urban','Suburban','Rural']
colors = ['lightcoral','lightskyblue','gold']
explode = (0.1,0,0)
```

## Total Fares by City Type


```python
plt.figure(figsize=(6,6))
plt.pie(zippidie_doo_dah[0], labels=labels, explode=explode, shadow=True, startangle=245,
        autopct='%.2f%%', colors=colors, textprops={'fontsize':12})
plt.title('% of Total Fares by City Type', size=16)
plt.axis('equal')
plt.show()
```


![png](output_13_0.png)


## Total Rides by City Type


```python
plt.figure(figsize=(6,6))
plt.pie(zippidie_doo_dah[1], labels=labels, explode=explode, shadow=True, startangle=240,
        autopct='%.2f%%', colors=colors, textprops={'fontsize':12})
plt.title('% of Total Fares by City Type', size=16)
plt.axis('equal')
plt.show()
```


![png](output_15_0.png)


## Total Drivers by City Type


```python
plt.figure(figsize=(6,6))
plt.pie(zippidie_doo_dah[2], labels=labels, explode=explode, shadow=True, startangle=220,
        autopct='%.2f%%', colors=colors, textprops={'fontsize':12})
plt.title('% of Total Fares by City Type', size=16)
plt.axis('equal')
plt.show()
```


![png](output_17_0.png)

