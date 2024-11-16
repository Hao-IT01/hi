from data_processing.crud import load_data, create_entry, read_data, update_entry, delete_entry
from data_processing.cleaning import clean_missing_values, normalize_text_columns, remove_duplicates, normalize_numeric_columns
from data_processing.visualization import plot_average_rating_by_genre, plot_size_vs_rating, plot_free_vs_paid
import pandas as pd

# Đường dẫn tới file CSV
file_path = 'AppleStore.csv'
data = pd.read_csv(file_path)

# Bước 1: Làm sạch dữ liệu
data = clean_missing_values(data)
data = normalize_text_columns(data, columns=['track_name', 'prime_genre'])
data = remove_duplicates(data)

# Bước 2: Chuẩn hóa dữ liệu số
data = normalize_numeric_columns(data, columns=['rating_count_tot', 'rating_count_ver'])

# Bước 3: Trực quan hóa dữ liệu
plot_average_rating_by_genre(data)
plot_size_vs_rating(data)
plot_free_vs_paid(data)

# Lưu lại dữ liệu đã làm sạch và chuẩn hóa (tuỳ chọn)
data.to_csv('AppleStore_cleaned.csv', index=False)
print("Dữ liệu đã được lưu vào AppleStore_cleaned.csv")

