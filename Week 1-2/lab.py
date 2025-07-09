import pandas as pd
dataset = 'pima_diab.csv'
df = pd.read_csv(dataset)

#โชว์20เรคอดแรก
print("show record 20")
print(df.head(20))

#แสดงอายุและผิวหนังที่มากกว่า30 35
selectageskin = df.loc[(df['age'] > 30) & (df['skin'] > 35)]
print("show age > 30 and skin > 35")
print(selectageskin)

#ลบคอลั่ม unnamed
df = df.drop(columns = ['Unnamed: 0'])
print('drop unnamed')
print(df)

#แทนที่ค่าโดยค่าmean
df = df.fillna(df.mean())