import numpy as np
import pandas as pd

data = pd.read_csv('TataMotorsData.csv')
arr = data.to_numpy()
print(arr[:5])


#Average of price
avgprice = np.nanmean(arr[:,1])
print("avearge price in a year", avgprice)

#median of price
median = np.nanmedian(arr[:,1])
print("median of a year", median)

#mac prioce in a year
maxprice = np.nanmax(arr[:,1])
print("max price  of a year", maxprice)

#min price in a year
minprice = np.nanmin(arr[:,1])
print("min price  of a year", minprice)


#avearge volume
volume_str = arr[:,5].astype(str)
cleaned = np.char.replace(volume_str, 'M', '')
a= [float(i) for i in cleaned]
avgvol = np.mean(a)
print("avg vol  of a year", minprice)

#standard daviation
print("Price Volatility:", np.std(arr[:,3]))

#daily returns
daily = arr[:,1]
daily_return = (daily[1:] - daily[:-1])
print([int(i) for i in daily_return])



