import pandas as pd
df = pd.read_csv("/Users/kylechristensen/Documents/IS-303/Class 9/world_development_data.csv")
print(df.head())
print(df.describe())
print(df.shape)
print(df.info())

water_crisis = df[df["clean_water_pct"] < 80]
print(water_crisis[["country", "clean_water_pct"]])

# Life expectancy below 60
life_exp = df[df["life_expectancy"] < 60]
print(life_exp[["country", "life_expectancy"]])
print(len(life_exp))

# Highest life expectancy
highest = df.loc[df["life_expectancy"].idxmax()]
print(highest[["country", "life_expectancy"]])

# Unique regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

# Null data
print(df.isnull().sum())

# Sub Saharan Africa
ssa = df[df["region"] == "Sub-Saharan Africa"]
print(ssa[["country", "region"]])

# Fill in water
df["clean_water_pct"] = df["clean_water_pct"].fillna(0)
print(df[["clean_water_pct"]])

assert df["clean_water_pct"].notna().all(), "Missing clean water data!"