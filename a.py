import numpy as np
import pandas as pd

data = pd.read_csv('weatherAUS.csv')
arr = data.to_numpy()
print(arr)


#avearage temprature 
min = np.nanmean(arr[:, 2:3], axis=0)
print("minimum temprature is",min )


#avearage temprature 
max= np.nanmean(arr[:, 3:4], axis=0)
print("maximum temprature is",max )

#coldest day
min= np.min(arr[:,2:3])
idx= np.where(min==arr[:,2:3])
print(arr[idx],"temprature is", min)

#hottest day
max= np.max(arr[:,3:4])
idx= np.where(max ==arr[:,3:4])
print(arr[idx],"temprature is", max)

#avg temprature on rainy days
# 1. Convert column to float, replacing 'NA' with 0
arr[:, 4] = np.array([float(x) if x != 'NA' else 0 for x in arr[:, 4]])
find = np.where(arr[:, 4] > 1)
mean = (arr[find, 2]+arr[find, 3])/2
print(arr[9])
print(np.fix(mean))

#total rainfall
sum= np.nansum(arr[:,4]) 
print(sum)

#number of days in rainfall
count =0;
for x in arr[:,4]:
    if x>1:
        count = count +1
print(count)  
#avearge rainfall per day\
mean = np.nanmean(arr[:, 4])
print(mean)  

#max rainfall
maxs =np.nanmax(arr[:,4])
print(maxs)

# 8 average wind speed
wind = np.nanmean(arr[:,8])
print(wind)

#maximum wind
windmax =np.nanmax(arr[:,8])
print(windmax)


humidity = arr[:,13] + arr[:,14]
humMean= np.nanmean(humidity)
print(humMean)


mask = np.where(humidity > 121.00)
days = arr[mask, 0]
print(days)

# wind speed on hot days
hotdays= np.nanmean(arr[:,3])
find=np.where(arr[:,3]>hotdays)
print(find)
print(arr[find, 8])


#thresold
a=np.nanmean(arr[:,3]) +1.5
b=np.nanstd(arr[:,3])
c= a*b
print(c)

#hottest day accrodn to thresold
god = np.where(arr[:,3] > c)
print(arr[god, 3])

#coldest day accrodn to thresold
gods = np.where(arr[:,3] < c)
print(arr[gods, 3])

