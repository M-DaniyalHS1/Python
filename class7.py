# # # # pandas 
# # # # filtering
# # # # sorting
# # # # useful methods
# # # # groupby
# # # # merge


# import pandas as pd
# import numpy as np

# # Generate random dates
# date_range = pd.date_range(start='2024-01-01', periods=1000, freq='D')

# # Generate random fees
# fees = np.random.randint(50, 5000, size=1000)

# # Create DataFrame
# data = {
#     'date': date_range,
#     'fee': fees
# }

# df = pd.DataFrame(data)

# # Display DataFrame
# print(df)
# # Display DataFrame with transaction counts
# new_data = pd.cut(df.fee,
# [1,500,1000,3000,5000]
# )

# print(new_data)
# # \ counting slabes of transactions
# new_data1 = pd.cut(df.fee,
# [1,500,1000,3000,5000]
# ).value_counts()

# print(new_data1)
# # takig percentage of transactions

# new_data2 =  pd.cut(df.fee,
# [1,500,1000,3000,5000]
# ).value_counts(normalize=True)*100

# print(new_data2)
# #  pdqcut
# pd.qcut(df.fee,[0.9,.7,.7,.5,.1])

import pandas as pd
from datetime import datetime

students_data = [
    {
        "roll_no": 101,
        "name": "Alice",
        "father_name": "John Doe",
        "course": "Computer Science",
        "date_of_admission": "2023-09-02",
        "fee": 1500
    },
    {
        "roll_no": 102,
        "name": "Bob",
        "father_name": "Michael Smith",
        "course": "Mathematics",
        "date_of_admission": "2023-10-11",
        "fee": 1400
    },
    {
        "roll_no": 103,
        "name": "Charlie",
        "father_name": "David Johnson",
        "course": "Physics",
        "date_of_admission": "2023-5-25",
        "fee": 1600
    },
    {
        "roll_no": 104,
        "name": "Diana",
        "father_name": "Edward Brown",
        "course": "Chemistry",
        "date_of_admission": "2024-09-17",
        "fee": 1550
    },
    {
        "roll_no": 105,
        "name": "Ethan",
        "father_name": "Frank Green",
        "course": "Biology",
        "date_of_admission": "2022-4-19",
        "fee": 1500
    },
    {
        "roll_no": 106,
        "name": "Fiona",
        "father_name": "George White",
        "course": "Mathematics",
        "date_of_admission": "2023-09-01",
        "fee": 1450
    },
    {
        "roll_no": 107,
        "name": "George",
        "father_name": "Henry Black",
        "course": "History",
        "date_of_admission": "2023-09-01",
        "fee": 1400
    },
    {
        "roll_no": 108,
        "name": "Hannah",
        "father_name": "Ian Grey",
        "course": "English",
        "date_of_admission": "2023-09-01",
        "fee": 1350
    }

    
]

studentsdf : pd.DataFrame = pd.DataFrame(students_data)
# studentsdf["date_of_admission"] = pd.to_datetime(studentsdf["date_of_admission"])
# print(studentsdf)

# filters =  studentsdf["course"] == "physics"
# print(filters)

# filters2 = studentsdf[ studentsdf["course"] == "physics"]
# print(filters2)
# studentsdf["course"].str.lower().str.contains("cs")
# filters3 = studentsdf[studentsdf["course"].str.lower().str.contains("cs")]
# print(filters3)

# filters4 = studentsdf[studentsdf["course"].str.lower().str.contains("cs") & studentsdf["course"].str.lower().str.contains("a")]
# print(filters4)


# filters5 = studentsdf[studentsdf["course"].str.lower().str.contains("cs") | studentsdf["course"].str.lower().str.contains("a")]
# print(filters5)

# # 
# dates = studentsdf["date_of_admission"]
# print(dates)

# from datetime import datetime
# date : datetime = datetime.now()
# print(date)

# s1 : pd.Series = pd.Series([date])
# print(s1)
# # strftime conerts from date to text
# print(s1.dt.strftime("%Y-%m-%d")) 
# s2 : pd.Series = pd.Series(["01 nov 2023", "01 nov 2025"])
# s3 = s2.apply(lambda x: datetime.strptime(x, "%d %b %Y") )
# # string to datetime datatype conversion
# print(s3)
# print(type(s3))

# # # ******************* Group by ********************
studentsdf['date_of_admission'] = pd.to_datetime(studentsdf['date_of_admission'])

print(studentsdf)
new2 = list(studentsdf.groupby(["course"]))[0][1]
print(new2)

for group in list(studentsdf.groupby(["course"])):
    print(f"Course: {group[0]}")
    print(group[1])
    print("----------------------------------------")



for group in list(studentsdf.groupby([studentsdf['date_of_admission'].dt.strftime("%Y-%m-%d")])):
    print(group[0])
    print(group[1])
    print("----------------------------------------")

for group in list(studentsdf.groupby([studentsdf['date_of_admission'].dt.strftime("%m")])):
    print(group[0])
    print(group[1])
    print("----------------------------------------")


