#створи тут свій індивідуальний проект!
import pandas as pd

df = pd.read_csv("train.csv")

def follower_count(fol_count):
    if fol_count == 0:
        return 0
    else:
        return 1

def lang_count(langs):
    l_count = 1
    for lang in langs:
        if lang == ";":
            l_count += 1
    return l_count

def uniq_value(lis,name):
    n_list = list()
    for value in lis:
        n_list.append((name + str(value)))
    return n_list

def change_education_status(string):
    if string == "Undergraduate applicant":
        return 1
    if string == "Student (Bachelor's)":
        return 2
    if string == "Alumnus (Bachelor's)":
        return 3
    if string == "Student (Specialist)":
        return 4
    if string == "Student (Master's)":
        return 5
    if string == "Alumnus (Specialist)":
        return 6
    if string == "Alumnus (Master's)":
        return 7
    if string == "Candidate of Sciences":
        return 8
    if string == "PhD":
        return 9

df.drop(["id", "bdate", "city", "last_seen", "occupation_name", "career_end", "graduation", "career_start"], axis= 1, inplace= True)

df["has_mobile"] = df["has_mobile"].apply(int)

df["followers_count"] = df["followers_count"].apply(int)

df["relation"] = df["relation"].apply(int)

df["langs"] = df["langs"].apply(lang_count)
df["followers_count"] = df["followers_count"].apply(follower_count)

df["education_form"] = df["education_form"].fillna("Full-time")
df["occupation_type"] = df["occupation_type"].fillna("university")

df[pd.get_dummies(df["education_form"]).columns] = pd.get_dummies(df["education_form"], dtype= int)
df.drop(["education_form"], axis = True, inplace= True)
df["education_status"] = df["education_status"].apply(change_education_status)
df[pd.get_dummies(df["education_status"]).columns] = pd.get_dummies(df["education_status"], dtype= int)
df.drop(["education_status"], axis = True, inplace= True)
df[pd.get_dummies(df["occupation_type"]).columns] = pd.get_dummies(df["occupation_type"], dtype= int)
df.drop(["occupation_type"], axis = True, inplace= True)

df[uniq_value(list(df["life_main"].value_counts().index), "life_main")] = pd.get_dummies(df["life_main"], dtype= int)
df.drop(["life_main"], axis = True, inplace= True)
df[uniq_value(list(df["people_main"].value_counts().index), "people_main")] = pd.get_dummies(df["people_main"], dtype= int)
df.drop(["people_main"], axis = True, inplace= True)
df[uniq_value(list(df["relation"].value_counts().index), "relation")] = pd.get_dummies(df["relation"], dtype= int)
df.drop(["relation"], axis = True, inplace= True)

df.info()
print(df.head(10))
