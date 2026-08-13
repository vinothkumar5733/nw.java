station = 1
last_station = station
while station <= 15:
    if station % 3 == 0 and station % 5 == 0:
        print(station)
        print('First common station: ', station)
        break
    station+=1

    