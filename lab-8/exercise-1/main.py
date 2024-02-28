def lowestAverageTemperature(filename):
    f = open(filename, "r")
    weather = f.readlines()
    f.close()

    for i in range(len(weather)):
        weather[i] = weather[i].strip()

    days = []
    avgTemp = []

    for line in weather:
        parts = line.split(",")
        day = parts[0]
        low = int(parts[1])
        high = int(parts[2])
        averageTemperature = (low + high) / 2
        days.append(day)
        avgTemp.append(averageTemperature)

    m = avgTemp[0]
    mIndex = 0
    for i in range(1, len(avgTemp)):
        if(avgTemp[i] < m):
            m = avgTemp[i]
            mIndex = i
    return days[mIndex]

x = lowestAverageTemperature("weather.csv")
print(x)