import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("stock.csv")
# print(data.info())
# print(data.shape)
# print(data.head(5))

basic_agg=data["Open"].aggregate(['min','max','median','mean'])
# print(basic_agg)


multi_tier=data.aggregate({
    "Open":['min','max','median','mean'],
    "Close":['min','max','median','mean'],
    "Volume":['min','max','median','mean']
})
# print(multi_tier)

print(data['Date'].head())  # Replace 'column_name' with your actual column name
data = data.dropna(subset=['Date']) # Drop rows with NaNs in the date column
data = pd.read_csv('stock.csv', header=0)  # Adjust the header row if necessary

data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

def range_calc(x):
    return x.max()-x.min()
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='coerce')
print(data['Date'].head()) 

advanced_data=data.groupby(data["Date"].dt.year).agg(
    Open_Min=("Open","min"),
    Open_Max=("Open","max"),
    Close_Mean=("Close","mean"),
    Volume_Total=("Volume","sum"),
    Open_Range=("Open",range_calc)
)
# print(advanced_data)


plt.figure(figsize=(10,6))
plt.plot(advanced_data.index, advanced_data["Open_Range"], color="orange", marker='D')
plt.title("range of Opening prices")
plt.xlabel("Year")
plt.ylabel("Open Range")
plt.grid(True)
plt.show()



