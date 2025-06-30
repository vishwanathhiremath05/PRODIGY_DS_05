git import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Use raw string (r"...") or forward slashes to fix the unicode escape error
df = pd.read_csv(r"C:\Users\ADMIN\Desktop\ACCIDENT PROJECT\accident_prediction_india.csv")

df['Hour'] = pd.to_datetime(df['Time of Day'], errors='coerce').dt.hour
df['Date'] = pd.to_datetime(df['Year'].astype(str) + ' ' + df['Month'] + ' ' + df['Day of Week'], errors='coerce')
df['DayOfWeek'] = df['Day of Week']

plt.figure(figsize=(7, 5))
sns.countplot(x='Accident Severity', data=df, order=df['Accident Severity'].value_counts().index, palette='Set2')
plt.title("Accidents by Severity")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 5))
order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='DayOfWeek', data=df, order=order_days, palette='Set3')
plt.title("Accidents by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Hour'].dropna(), bins=24, kde=True, color='skyblue')
plt.title("Accidents by Hour of the Day")
plt.xlabel("Hour")
plt.ylabel("Frequency")
plt.xticks(range(0, 24))
plt.show()

plt.figure(figsize=(10, 5))
top_weather = df['Weather Conditions'].value_counts().nlargest(10).index
sns.countplot(y='Weather Conditions', data=df[df['Weather Conditions'].isin(top_weather)], order=top_weather, palette='coolwarm')
plt.title("Top 10 Weather Conditions for Accidents")
plt.xlabel("Count")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Road Condition', data=df, order=df['Road Condition'].value_counts().index, palette='pastel')
plt.title("Accidents by Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
