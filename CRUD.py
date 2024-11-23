import pandas as pd
import function as f
# 1. Tao moi
# CRUD.py
import pandas as pd

def Create(my_df, new_data):
    
    # Tạo DataFrame từ dữ liệu mới
    new_app_df = pd.DataFrame(new_data, index=[0])
    updated_df = pd.concat([my_df, new_app_df], ignore_index=True)

    # Lưu lại file CSV
    updated_df.to_csv("AppleStore.csv", index=False)



# 2. Doc
def Read(my_df):
    print()
    print("Reading dataset:")
    print(my_df.head(100))
    print(my_df.describe())


# 3. Sua
def Update(my_df, app_name, column_to_update, new_value):
    
    # Loc them track name
    idx_drop = my_df[my_df["track_name"] == app_name].index

    if len(idx_drop) == 0:
        return f"No item found with the name '{app_name}'."

    # Cap nhat lai gia tri
    my_df.loc[idx_drop, column_to_update] = new_value

    # Luu vao file
    my_df.to_csv("AppleStore.csv", index=False)

                      
# 4. Xoa
def Delete(my_df, app_name):
    
    # Loc 
    idx_drop = my_df[my_df["track_name"] == app_name].index

    if len(idx_drop) == 0:
        return f"No item found with the name '{app_name}'."

    # remove
    my_df.drop(idx_drop, inplace=True)

    # luu
    my_df.to_csv("AppleStore.csv", index=False)
