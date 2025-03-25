import pandas as pd

df = pd.read_csv('heart.csv')
print("\nVeri Setinin İlk 5 Satırı:")
print(df.head())

print("\nEksik Veri Sayısı:")
print(df.isnull().sum())

df['thalach'].fillna(df['thalach'].mean(), inplace=True)
print("\nEksik veriler dolduruldu. Yeni veri boyutu:", df.shape)

print("\nTemel İstatistikler:")
print(df.describe())
