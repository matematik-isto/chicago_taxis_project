# Chicago_taxis_project
## 📌 Summary
In this project I analyze the beahviour of taxi trips in Chicago 2017. Data is gathered from data.cityofchicago.org using csv files and API and saved into a local SQL database.

Do weather conditions have a positive or negative impact on the usage of taxis?
## 🗃️ Datasets
1. chicago-taxi-trips-2017
   * Records: > 24 million
   * Period: Nov 2017
   * Variables:
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-sk46{background-color:#E9E9ED;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-rc81{background-color:#E9E9ED;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-7h26{color:#00E;text-align:left;text-decoration:underline;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-sk46">Column Name</th>
    <th class="tg-7btt">Description</th>
    <th class="tg-rc81">API Field Name</th>
    <th class="tg-rc81">Data Type</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Trip ID</td>
    <td class="tg-0pky">A unique identifier for the trip.</td>
    <td class="tg-0lax">trip_id</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">Taxi ID</td>
    <td class="tg-0pky">A unique identifier for the taxi.</td>
    <td class="tg-0lax">taxi_id</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0pky">Trip Start Timestamp</td>
    <td class="tg-0pky">When the trip started, rounded to the nearest 15 minutes.</td>
    <td class="tg-0lax">trip_start_timestamp</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/floating_timestamp.html">Floating Timestamp</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Trip End Timestamp</td>
    <td class="tg-0lax">When the trip ended, rounded to the nearest 15 minutes.</td>
    <td class="tg-0lax">trip_end_timestamp</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/floating_timestamp.html">Floating Timestamp</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Trip Seconds</td>
    <td class="tg-0lax">Time of the trip in seconds.</td>
    <td class="tg-0lax">trip_seconds</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Trip Miles</td>
    <td class="tg-0lax">Distance of the trip in miles.</td>
    <td class="tg-0lax">trip_miles</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Pickup Census Tract</td>
    <td class="tg-0lax">The Census Tract where the trip began.&nbsp;&nbsp;For privacy, this Census Tract is not shown for some trips. This column often will be blank for locations outside Chicago.</td>
    <td class="tg-0lax">pickup_census_tract</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dropoff Census Tract</td>
    <td class="tg-0lax">The Census Tract where the trip ended.&nbsp;&nbsp;For privacy, this Census Tract is not shown for some trips. This column often will be blank for locations outside Chicago.</td>
    <td class="tg-0lax">dropoff_census_tract</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Pickup Community Area</td>
    <td class="tg-0lax">The Community Area where the trip began. This column will be blank for locations outside Chicago.</td>
    <td class="tg-0lax">pickup_community_area</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dropoff Community Area</td>
    <td class="tg-0lax">The Community Area where the trip ended. This column will be blank for locations outside Chicago.</td>
    <td class="tg-0lax">dropoff_community_area</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Fare</td>
    <td class="tg-0lax">The fare for the trip.</td>
    <td class="tg-0lax">fare</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Tips</td>
    <td class="tg-0lax">The tip for the trip. Cash tips generally will not be recorded.</td>
    <td class="tg-0lax">tips</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Tolls</td>
    <td class="tg-0lax">The tolls for the trip.</td>
    <td class="tg-0lax">tolls</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Extras</td>
    <td class="tg-0lax">Extra charges for the trip.</td>
    <td class="tg-0lax">extras</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Trip Total</td>
    <td class="tg-0lax">Total cost of the trip, the total of the previous columns.</td>
    <td class="tg-0lax">trip_total</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Payment Type</td>
    <td class="tg-0lax">Type of payment for the trip.</td>
    <td class="tg-0lax">payment_type</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Company</td>
    <td class="tg-0lax">The taxi company.</td>
    <td class="tg-0lax">company</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/text.html">Text</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Pickup Centroid Latitude</td>
    <td class="tg-0lax">The latitude of the center of the pickup census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">pickup_centroid_latitude</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Pickup Centroid Longitude</td>
    <td class="tg-0lax">The longitude of the center of the pickup census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">pickup_centroid_longitude</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Pickup Centroid Location</td>
    <td class="tg-0lax">The location of the center of the pickup census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">pickup_centroid_location</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/point.html">Point</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dropoff Centroid Latitude</td>
    <td class="tg-0lax">The latitude of the center of the dropoff census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">dropoff_centroid_latitude</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dropoff Centroid Longitude</td>
    <td class="tg-0lax">The longitude of the center of the dropoff census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">dropoff_centroid_longitude</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/number.html">Number</a></td>
  </tr>
  <tr>
    <td class="tg-0lax">Dropoff Centroid&nbsp;&nbsp;Location</td>
    <td class="tg-0lax">The location of the center of the dropoff census tract or the community area if the census tract has been hidden for privacy. This column often will be blank for locations outside Chicago.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-0lax">dropoff_centroid_location</td>
    <td class="tg-7h26"><a href="https://dev.socrata.com/docs/datatypes/point.html">Point</a></td>
  </tr>
</tbody></table>

2. comunity_areas
   * Records: 78
   * Variables:
     * area_numbe: community area id
     * community: community area name
3. weather
    * Records:
    * Variables:
     * Date and time : fecha y hora
     * Temperature : temperatura
     * Description : weather condition e.g. mist, sky is clear, etc.

## 🔬 Methodology

- Gather data from web, api and csv files
- Consolidate data into SQL databases
- Exploratory Data Analysis (EDA)
- Hypotesis test

## 💡 Results and Key Insights

- 4 out of 77 community areas concentrate 50% of all the trips.
- The number of trips increases when the weather is rainy.

## 📁 Repository Structure
```
├── datasets/
│   ├── megaline_calls.csv
│   ├── megaline_internet.csv
│   ├── megaline_messages.csv
│   ├── megaline_plans.csv
│   └── megaline_users.csv
├── notebooks/
|   ├── notebook_es.ipynb
├── README.md
└── requirements.txt
```
## ▶️ How to Run the Project

1. Clone the repository
2. Install dependencies (pip install -r requirements.txt)
3. Run the scripts located in the external folder to download data
4. Run the scripts located in the project folder to consolidate data into SQL database
5. Run the analysis notebooks in Jupyter

## 🚀 Future Improvements

- create english translation
- create process to export to csv filtered data
 
## 🛠️ Tools and Technologies

- Python: pandas, seaborn, scipy
- SQL: SQL Server, sqlite
