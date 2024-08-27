import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("airbnb.csv")

# print(df.head())
# print(df.info())
# print("Initial data shape",df.shape)
# print(df.describe())


print("missinng values:\n",df.isnull().sum())
print("missinng values:\n",df.duplicated().sum())

df["reviews_per_month"].fillna(df["reviews_per_month"].mean(), inplace=True)
df["price"].fillna(df["price"].mean(), inplace=True)
df["reviews_per_month"].fillna(df["reviews_per_month"].mean(), inplace=True)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# print(df.head())
# print(df.info())
# print("Initial data shape",df.shape)
# print(df.describe())


# df["price"].plot()
# plt.ylabel("Price")
# plt.title("Plot of Prices")
# plt.show()

# df.plot(kind="scatter", x="price", y="number_of_reviews")
# plt.title("prices vs no of reviews")
# plt.show()


fig, axs=plt.subplots(2,3, figsize=(15,10))
axs[0,0].hist(["price"],bins=20, color="Lightblue")
axs[0,0].set_title("Price vs frequency")
axs[0,0].set_xlabel("Price")
axs[0,0].set_ylabel("Frequency")


axs[0,1].hist(["number_of_reviews"],bins=20, color="Red")
axs[0,1].set_title("Number of reviews vs Frequency")
axs[0,1].set_xlabel("number_of_reviews")
axs[0,1].set_ylabel("Frequency")


room_type1=df.groupby('room_type')['price'].mean().reset_index()
axs[0,2].bar(room_type1['room_type'],room_type1["price"],color="Lightgreen")
axs[0,2].set_title("Average price by Room type")
axs[0,2].set_xlabel("room_type")
axs[0,2].set_ylabel("price")


neighborhoods= df['neighbourhood_group'].value_counts().reset_index()
neighborhoods.columns=['neighbourhood_group','count']
axs[1,0].bar(neighborhoods['neighbourhood_group'],neighborhoods['count'],color="Orange")
axs[1,0].set_title("Listings by Neighborhood")
axs[1,0].set_xlabel("Neighborhood")
axs[1,0].set_ylabel("Number of Listing")


axs[1,1].scatter(df["price"],df['number_of_reviews'],color='Blue')
axs[1,1].set_title("Price Vs Reviews")
axs[1,1].set_xlabel("Price")
axs[1,1].set_ylabel("No of Reviews")


plt.tight_layout
plt.show()
