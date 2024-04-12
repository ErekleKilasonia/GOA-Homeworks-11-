#Number of People in the Bus
def number(bus_stops):
    sum = 0
    for i in bus_stops:
        sum = sum + i[0] -i[1]
    return sum
        