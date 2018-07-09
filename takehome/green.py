import pandas as pd
import requests
import io
from IPython.display import HTML
HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')

hideCode = lambda : HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<a href="javascript:code_toggle()">Toggle Code</a>.''')

def get_data():
    """this function will download the green taxi data from 
       https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2015-09.csv
       provided that the data.pkl does not exists
    """
    try:
        return pd.read_pickle("data.pkl")
    except:
        ## data url 
        src = "https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2015-09.csv"
        ## get data 
        data=requests.get(src).content
        data=pd.read_csv(io.StringIO(data.decode('utf-8')))
        ## convert the pickup and dropoff datetimes to datetimes
        ## this will aid in calc'ing day of week, time of day, hour of day, etc. 
        data["lpep_pickup_datetime"]  = pd.to_datetime(data["lpep_pickup_datetime"])
        data["Lpep_dropoff_datetime"]  = pd.to_datetime(data["Lpep_dropoff_datetime"])
        # pickling data so it doesn't have to be downloaded again. 
        data.to_pickle("data.pkl")
        return data

