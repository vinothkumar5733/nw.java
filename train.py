station = 1
last_station = station
first_station = station
while station <= 80:
    if station % 3 == 0 and station % 5 == 0:
        last_station = station   #15   30   45  60  75
        if first_station == station:
            first_station = station
        # print(last_station)
        print(station)
    station+=1

# print("Last Common Station is", last_station)