import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  
import seaborn as sns




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

#แปลงค่าให้อยู่ในZ-score 
print('make insu to z score')
scaler = StandardScaler()
df['insu'] = scaler.fit_transform(df[['insu']])
print(df['insu'])#ให้แสดงแค่ชา่องเดียวเพราะมันเป็น...กลัวอาจารย์ไม่เห็น


#แปลงเป็นเมตริกซ์correlation
print('make Correlation')
plt.figure(figsize=(9,7))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm') 
plt.title('Correlation')
plt.show()

#แปลงclassเป็น0 1 ก่อนแล้วค่อยมาเช็ค3อันดับแรก
df['class'] = df['class'].map({'tested_negative': 0, 'tested_positive': 1})
corr_matrix = df.corr(numeric_only=True)
top3 = corr_matrix['class'].drop('class').sort_values(ascending=False).head(3).index.tolist()##pandas + list dont do that use tolist
print('Top 3')
print(top3)


#สร้างข้อม฿ลใหม่
print('Make new data')
new_df = df[top3 + ['class']]
new_df.to_csv('new_data.csv', index=False)
print("create newdata succese")