import datetime
def nextBirthdate(filename, date):
    with open("birthdates.csv", "r") as my_file:
        lines = my_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    parts = lines[0].split(',')
    closest_name, closest_date = parts[0], parts[1]
    closest_date = convert_to_datetime(closest_date)


    date = convert_to_datetime(date)

    for line in lines[1:]:
        parts = line.split(',')
        name, dDate = parts[0], parts[1]
        dDate = convert_to_datetime(dDate)
        closer = compare_dates(date, closest_date, dDate)
        if dDate == closer:
            closest_name = name
            closest_date = closer
    
    return closest_name

def convert_to_datetime(date):
    split = date.split('/')
    month, day, year = split[0],split[1],split[2]
    date = datetime.datetime(int(year), int(month), int(day))
    return date


def compare_dates(current_day, d1, d2):
    year = current_day.year
    origD1 = d1.year
    origD2 = d2.year
    d1 = d1.replace(year=year+1)
    d2 = d2.replace(year=year+1)
    if d1 < current_day:
        d1 = d1.replace(year = year+1)
    if d2 < current_day:
        d2 = d2.replace(year = year+1)
    if d1 < d2:
        return d1.replace(year=origD1)
    else:
        return d2.replace(year=origD2)

if __name__ == '__main__':
    x = nextBirthdate("birthdates.csv", "09/02/2022")
    print(x)