def nextBirthdate(filename, date):
  f = open(filename,"r")
  lines = f.readlines()
  f.close()
  
  for i in range(len(lines)):
    lines[i] = lines[i].strip()

  inMonth=False
  days = []
  mon = []
  for i in range(len(lines)):
    line = lines[i].split(",")
    line2 = line[1].split()
    plop = line2[0].split("/")
    dateSplit = date.split("/")
    month = int(dateSplit[0])
    day = int(dateSplit[1])
    if month==int(plop[0]):
      if day==(int(plop[1])):
        return line[0]
      elif day<int(plop[1]):
        if not(inMonth):
          days=[]
          mon=[]
        days.append(int(plop[1]))
        inMonth=True
    if not(inMonth):
      if (int(plop[0])>month) or ((int(plop[0])==1) and (month==12)):
        days.append(int(plop[1]))
        mon.append(int(plop[0]))
  i=1
  while len(days)!=1:
    if not(inMonth):
      if month!=12:
        if mon[i-1]<mon[i]:
          mon.pop(i)
          days.pop(i)
        elif mon[i-1]>mon[i]:
          mon.pop(i-1)
          days.pop(i-1)
        else:
          i+=1
        if i>len(mon):
          inMonth=True
          i=1
      elif month==12:
        inMonth=True
    if inMonth:
      if days[i-1]<days[i]:
        days.pop(i)
      elif days[i-1]>days[i]:
        days.pop(i-1)
      else:
        i+=1
  if len(mon)>0:
    inMonth = False
  for i in range(len(lines)):
    line = lines[i].split(",")
    line2 = line[1].split()
    plop = line2[0].split("/")
    if not(inMonth):
      if mon[0]==int(plop[0]):
        if days[0]==int(plop[1]):
          return line[0]
    elif days[0]==int(plop[1]):
      return line[0]

x = nextBirthdate("birthdates.csv", "1/21/2022")
print(x)
