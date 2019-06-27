# Wolt-median-pickuptime

## Quick Start

1. Clone the repo
```
$ git clone https://github.com/Thi-tran/Wolt-median-pickuptime.git
$ cd Wolt-median-pickuptime
```

2. Initialize and activate a virtualenv:
```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```
3. Install the dependencies:
```
$ pip install -r requirements.txt
```
4. Run the development server:
```
$ python app.py
```
5. Request for Median pickup time with location and given time range (127.0.0.1:8080 by default)
```
http://127.0.0.1:8080/median_pickup_time?location_id=12&start_time=2019-01-09T11:00:00&end_time=2019-01-09T12:00:00
```

### Test 
```
python tests.py
```

### Other issues: 
- Request history is stored in file hdf5_data.h5 as Cache 
- Step 2 might be optional if you have already had virtual environment

## Future Developments: 
Here are some ways that I think that could be done to develop this further: 
- Using Binary Search to speend up searching process in both CSV file and Cache 
- Using Machine Learning with data from previous weeks, months to predict pickup time in the future
- Using Prediction from previous stage to predict peak time (when pickup time is high, and other conditions) and prepare solutions to match with the demand (distribute couriers in specific area, increase incentives for courier at that time)
