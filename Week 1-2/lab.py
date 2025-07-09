import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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

#เช็คค่าที่เป็นmiss
print('check miss')
print(df.isna().sum())

#แทนที่ค่าโดยค่าmean
print('refill by mean')
df = df.fillna(df.mean(numeric_only=True))
print(df)

#เช็คค่าที่เป็นmissอีกรอบ
print('check miss agian')
print(df.isna().sum())

#แปลงค่าให้อยู่ในระหว่าง01
print('make value to 0-1 from plas / skin')
scaler = MinMaxScaler(feature_range=(0,1))
cols_to_scale = ['plas', 'skin']
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
print(df)
