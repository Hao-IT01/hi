# Data Cleaning
import pandas
import numpy as np
import mlxtend

def check_missing_value (data):
    """Nhập vào dữ liệu là 1 data frame và xuất ra bảng các cột có giá trị null"""
    missing_values_count = data.isnull().sum()
    return missing_values_count

def fill_na_value (data):
    result = data.fillna(method='bfill', axis=0).fillna(0)
    return result
