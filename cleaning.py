import pandas as pd
import numpy as np

# Xử lý các giá trị bị thiếu
def clean_missing_values(data):
    data = data.dropna()  # Hoặc sử dụng data.fillna(value) để thay thế giá trị
    return data

# Chuẩn hóa các cột văn bản (nếu cần)
def normalize_text_columns(data, columns):
    for col in columns:
        data[col] = data[col].str.lower().str.strip()
    return data

# Loại bỏ dữ liệu trùng lặp
def remove_duplicates(data):
    data = data.drop_duplicates()
    return data

# Chuẩn hóa giá trị số bằng phương pháp Max-Abs Scaling
def normalize_numeric_columns(data, columns):
    df_max_scaled = data[columns].copy()
    for column in df_max_scaled.columns:
        df_max_scaled[column] = df_max_scaled[column] / df_max_scaled[column].abs().max()
    data[columns] = df_max_scaled
    return data
