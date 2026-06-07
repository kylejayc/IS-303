import pandas as pd
df = pd.read_csv("/Users/kylechristensen/Documents/IS-303/Class 10/security_log.csv")

# 1a. How many failures
# 1b. What % are failures
failures = df[df["status"] == "failed"]
print(len(failures))
print(f"{len(failures)/len(df)*100}%")
print(f"{failures["attempts"].sum()/df["attempts"].sum()*100}%")

# 2a. Which username has the most failed attempts?
# 2b. How many failures does that user have?
print(failures.groupby("username")["attempts"].sum().idxmax())
print(failures.groupby("username")["attempts"].sum().max())

# 3a. Which IP address is behind the most failures?
# 3b. What country is that IP from?

print(failures.groupby("ip_address")["attempts"].sum().idxmax())
print(failures.groupby("ip_address")["attempts"].sum().max())
# What country is that IP from?
print(failures.groupby("ip_address")["country"].first().loc[failures.groupby("ip_address")["attempts"].sum().idxmax()])