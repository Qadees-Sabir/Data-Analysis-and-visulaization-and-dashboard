import pandas as pd
#create a dataframe
df= pd.read_csv("data.csv")
#print(df.info())
# print(df.head(8))
# print(df.describe())

# large_cities=df[df["Population (2024)"] > 20000000]
# print("cities larger than 20 million",large_cities)

# vietnam=df[df["Country"]== "Vietnam"]
# print(vietnam)

# growing_cities_in_china=df[(df["Country"]=="China")& (df["Growth Rate"]>0)]
# print(growing_cities_in_china)



# cities_india=df[df["Country"]== "India"]["Population (2024)"].sum()
# # print(cities_india)



# decline_cities=df[df["Growth Rate"]<0]["Growth Rate"].median()
# print(decline_cities)


# min_china_city_population = df[(df["Country"]=="China")& (df["Growth Rate"]>0)]['Population (2024)'].min()
# min_city_row = df[(df['Country'] == 'China') & (df['Population (2024)'] == min_china_city_population)]

# print("City with the minimum population in China:", min_city_row['City'].values[0],min_china_city_population )



# country_group=df.groupby(by="Country")["City"].count()
# print(country_group)



# avg_pop=df.groupby(by="Country")["Population (2024)"].mean()
# print("avg population in countries:",avg_pop)

# growing_countries=df[df["Growth Rate"]>0]
# country_growth=growing_countries.groupby("Country")["Growth Rate"].sum().reset_index()
# print(country_growth)



# avg_pop_growth=df.groupby(by=["Country","Growth Rate"])["Population (2024)"].mean().reset_index()
# print(avg_pop_growth)


# country_stats=df.groupby("Country")["Population (2024)"].agg(["mean","sum","max","min"])
# print(country_stats)



# def growth_catagory(growth):
#     if growth>0.2:
#         return "High Growth"
#     elif growth>0:
#         return"Moderate Growth"
#     else:
#         return"Negative Growth"
# df["Growth catagory"]=df["Growth Rate"].apply(growth_catagory)
# growth_count=df.groupby(by=["Country","Growth catagory"])["City"].count()
# print(growth_count)



data= pd.read_csv("uncleaned.csv")
print(data.info())
print("Initial data shape",data.shape)
print("Missing values in each column before cleaning",data.isnull().sum())
print("No of  duplicate rows before cleaning",data.duplicated().sum())


data.replace("?",pd.NA , inplace=True)


critical_col=["Company","Cpu","Memory","Gpu","OpSys","Weight","Price"]
data=data.dropna(subset=critical_col)


data=data.drop_duplicates()
# print("Initial data shape",data.shape)
# print(data.info()

data["Weight"]=data["Weight"].str.replace("kg","",regex=False)
data["Weight"]=pd.to_numeric(data["Weight"], errors="coerce")

data["Price"]=pd.to_numeric(data["Price"], errors="coerce")

data["OpSys"]=data["OpSys"].str.lower().str.replace("_","")


def extract_cpu(cpu_info):
    try:
        return float(cpu_info.split()[-1][:-3])
    except Exception as e:
        return None
    

data["Cpu_Speed"]=data["Cpu"].apply(extract_cpu)


def convert_memory(memory):
    try:
        if "GB" in memory:
            return int(memory.replace("GB",""))*1024
        elif "TB" in memory:
            return int(memory.replace("TB",""))*1024*1024
    except Exception as e:
        return None
    
data["Memory_MB"]=data["Memory"].apply(convert_memory)



data["Weight"].fillna(data["Weight"].mean(), inplace=True)
data["Price"].fillna(data["Price"].mean(), inplace=True)
data["Cpu_Speed"].fillna(data["Cpu_Speed"].mean(), inplace=True)
data["Memory_MB"].fillna(data["Memory_MB"].mean(), inplace=True)  


print(data.info())
print("Final data shape",data.shape)
print("Missing values in each column after cleaning",data.isnull().sum())
print("No of  duplicate rows after cleaning",data.duplicated().sum())
