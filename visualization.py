import pandas as pd
import matplotlib.pyplot as plt
from cleaning import check_missing_value, fill_na_value

# Bước 1: Đọc dữ liệu
df = pd.read_csv("AppleStore.csv")

# Bước 4: Trực quan hóa dữ liệu

# Biểu đồ 1: Phân phối thể loại ứng dụng
genre_counts = df['prime_genre'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(genre_counts.index, genre_counts.values, color='skyblue')
plt.title('Distribution of App Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Biểu đồ 2: Phân phối số lượt đánh giá
plt.figure(figsize=(10, 6))
plt.hist(df['rating_count_tot'], bins=50, color='orange', edgecolor='black')
plt.title('Distribution of Total Ratings')
plt.xlabel('Total Ratings')
plt.ylabel('Frequency')
plt.yscale('log')  # Sử dụng thang log
plt.show()

# Biểu đồ 3: Phân phối kích thước ứng dụng
plt.figure(figsize=(10, 6))
plt.hist(df['size_bytes'], bins=50, color='green', edgecolor='black')
plt.title('Distribution of App Sizes')
plt.xlabel('App Size (bytes)')
plt.ylabel('Frequency')
plt.xscale('log')  # Sử dụng thang log
plt.show()

# Biểu đồ 4: Phân phối đánh giá trung bình
plt.figure(figsize=(10, 6))
plt.hist(df['user_rating'], bins=5, color='purple', edgecolor='black')
plt.title('Distribution of User Ratings')
plt.xlabel('User Rating')
plt.ylabel('Frequency')
plt.show()

# Biểu đồ 5: Đánh giá trung bình theo thể loại
avg_rating_by_genre = df.groupby('prime_genre')['user_rating'].mean().sort_values()
plt.figure(figsize=(12, 8))
avg_rating_by_genre.plot(kind='barh', color='coral', edgecolor='black')
plt.title('Average User Rating by Genre')
plt.xlabel('Average Rating')
plt.ylabel('Genre')
plt.show()

# Biểu đồ 6: Tổng số lượt đánh giá theo thể loại
total_rating_by_genre = df.groupby('prime_genre')['rating_count_tot'].sum().sort_values()
plt.figure(figsize=(12, 8))
total_rating_by_genre.plot(kind='barh', color='teal', edgecolor='black')
plt.title('Total Ratings by Genre')
plt.xlabel('Total Ratings')
plt.ylabel('Genre')
plt.show()

# Biểu đồ 7: Giá trung bình theo thể loại
avg_price_by_genre = df.groupby('prime_genre')['price'].mean().sort_values()
plt.figure(figsize=(12, 8))
avg_price_by_genre.plot(kind='barh', color='blue', edgecolor='black')
plt.title('Average Price by Genre')
plt.xlabel('Average Price (USD)')
plt.ylabel('Genre')
plt.show()

# Biểu đồ 8: Số ứng dụng theo xếp hạng nội dung
content_rating_counts = df['cont_rating'].value_counts()
plt.figure(figsize=(10, 6))
content_rating_counts.plot(kind='bar', color='cyan', edgecolor='black')
plt.title('Number of Apps by Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('Number of Apps')
plt.show()

# Biểu đồ 9: Số ứng dụng miễn phí và trả phí
df['is_free'] = df['price'] == 0
free_paid_counts = df['is_free'].value_counts()
plt.figure(figsize=(10, 6))
free_paid_counts.plot(kind='bar', color=['green', 'red'], edgecolor='black')
plt.title('Free vs Paid Apps')
plt.xlabel('Type')
plt.ylabel('Number of Apps')
plt.xticks([0, 1], ['Free', 'Paid'], rotation=0)
plt.show()

# Biểu đồ 10: Thể loại phổ biến nhất
genre_counts = df['prime_genre'].value_counts()
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Most Popular App Genres')
plt.ylabel('')
plt.show()

# Biểu đồ 11: Tỷ lệ các ứng dụng theo số thiết bị hỗ trợ
device_support_counts = df['sup_devices.num'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
device_support_counts.plot(kind='bar', color='gold', edgecolor='black')
plt.title('Number of Apps by Supported Devices')
plt.xlabel('Number of Supported Devices')
plt.ylabel('Number of Apps')
plt.show()
