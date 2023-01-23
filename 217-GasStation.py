'''PSCP Program'''
def main():
    '''8394-GasStation 30/10/2022'''
    total_dist = float(input())
    fuel_milage = float(input())
    gas_stations = int(input())
    station_dist = [float(input()) for _ in range(gas_stations)]
    station_dist.insert(0, 0)
    if station_dist[-1] != total_dist:
        station_dist.append(total_dist)
    stops = 0
    if fuel_milage >= total_dist:
        return 0
    if station_dist[0] > fuel_milage:
        return 'depleted'
    temp = 0
    i = 1
    while True:
        temp += station_dist[i] - station_dist[i-1]
        print(station_dist[i], station_dist[i-1], station_dist[i] - station_dist[i-1], temp)
        if temp >= fuel_milage:
            i += 1
            temp = station_dist[i] - station_dist[i-1]
            stops += 1
        else:
            i += 1
        if i >= len(station_dist) - 1:
            break
    return stops
print(main())
