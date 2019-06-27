import csv
import pandas as pd
from datetime import datetime
from statistics import median


# Change Time Format to Millisecond for comparison
def change_time(time_input):
    return int(datetime.strptime(time_input, "%Y-%m-%dT%H:%M:%SZ").timestamp())


# Calculate median from csv file (if the request data is not in cache)
def get_median(location, time_start, time_end):

    # Open csv file
    with open("pickup_times.csv") as file:
        reader = csv.reader(file)

        # Skip the first line
        next(file)

        # Get data from csv with condition
        result_list = []
        for row in reader:
            if (int(row[0]) == location) & (change_time(row[1]) >= time_start) & (change_time(row[1]) <= time_end):
                result_list.append(int(row[2]))

        return median(result_list)


# Add data to Cache
def add_data(key, result):

    # open Cache file with overwrite mode
    hdf = pd.HDFStore("hdf5_data.h5", mode="a")

    # Generate dataframe with result (dtype to avoid the bug with type int and float64)
    df = pd.DataFrame({"result":[result]}, index=[key], dtype='float64')

    # Adding (or create) data to hdf
    hdf.append("request", df, format="table", data_colums=True)
    hdf.close()


# Get data from Cache if it is available
def get_data(key):
    # Open Cache file with reading mode
    hdf = pd.HDFStore("hdf5_data.h5", mode="r")
    data = hdf.get("/request")

    # # Print out dataset (for debug)
    # print(data)

    # Check if request history in Cache
    if key in data.index:
        result = data.loc[key, 'result']
        hdf.close()
        return int(result)
    else:
        hdf.close()
        return None


def main(location, start_time, end_time):
    start_time_millisec = change_time(start_time)
    end_time_millisec = change_time(end_time)
    # Key for searching/saving in Cache
    key = str(location) + "-" + str(start_time_millisec) + "-" + str(end_time_millisec)

    # Check data from Cache
    check_data = get_data(key)

    if check_data is None:
        result = get_median(location, start_time_millisec, end_time_millisec)

        # add request history to cache
        add_data(key, result)
    else:
        result = check_data

    return int(result)
