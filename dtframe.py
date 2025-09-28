import pandas as pd

data = {"Name":["Daniel","Ben","Tracy"],"Age":[19,17,45]}
df = pd.DataFrame(data)
#print(df)
#     Name  Age
#0  Daniel   19
#1     Ben   17
#2   Tracy   45

#Add new columns
df["Job"] = ["Student","N/A","Instructor"]
#print(df)
#     Name  Age         Job
#0  Daniel   19     Student
#1     Ben   17         N/A
#2   Tracy   45  Instructor

#Add new rows
#new_row = pd.DataFrame([],[],[]) --> Add 3 rows
new_row = pd.DataFrame([{"Name":"Hippo","Age":34,"Job":"Tour"}],index=[3])
df = pd.concat([df, new_row])
#print(df)
#     Name  Age         Job
#0  Daniel   19     Student
#1     Ben   17         N/A
#2   Tracy   45  Instructor
#3   Hippo   34        Tour



