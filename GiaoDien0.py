import tkinter as tk
import pandas as pd
from tkinter import ttk
import CRUD
df = pd.read_csv("AppleStore.csv", sep=",")
root = tk.Tk()
root.geometry('1920x900')
root.resizable(True, True)
root.title("DataAnalysis")
ROWS_PER_PAGE = 10
current_page = 0
import tkinter as tk
def clear_window():
    #xoa mang hinh
    for widget in root.winfo_children():
        widget.destroy()
def show_menu():
    #hien menu
    clear_window()
    label = tk.Label(root, text="------ Data Analysis ------", font=("Times New Roman", 20, "bold"), 
                     bg="lightblue", fg="darkblue", padx=10, pady=10)
    label.pack(pady=20)
    label_menu = tk.Label(root, text="MENU", font=("Times New Roman", 20, "bold"))
    label_menu.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20) 
    button_view = tk.Button(button_frame, text="View Data", font=("Times New Roman", 15), width=15, command=lambda:show_page(current_page))
    button_view.grid(row=0, column=0, padx=10, pady=10)
    button_add = tk.Button(button_frame, text="Add Data", font=("Times New Roman", 15), width=15, command=show_add_form)
    button_add.grid(row=0, column=1, padx=10, pady=10)
    button_update = tk.Button(button_frame, text="Update Data", font=("Times New Roman", 15), width=15, command=show_update_form)
    button_update.grid(row=0, column=2, padx=10, pady=10)
    button_delete = tk.Button(button_frame, text="Delete Data", font=("Times New Roman", 15), width=15, command=show_delete_form)
    button_delete.grid(row=1, column=0, padx=10, pady=10)
    button_sort = tk.Button(button_frame, text="Sort Data", font=("Times New Roman", 15), width=15)
    button_sort.grid(row=1, column=1, padx=10, pady=10)
    button_search = tk.Button(button_frame, text="Search Data", font=("Times New Roman", 15), width=15)
    button_search.grid(row=1, column=2, padx=10, pady=10)

def next_page():
    #tien toi trang sau
    global current_page
    if (current_page + 1) * ROWS_PER_PAGE < len(df):
        current_page += 1
        show_page(current_page)

def prev_page():
    #lui ve trang truoc
    global current_page
    if current_page > 0:
        current_page -= 1
        show_page(current_page)


def show_page(page):
    #hien thi trang
    global current_page
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    #Tao bang treeview
    columns = list(df.columns)
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=ROWS_PER_PAGE)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    tree.pack(expand=True, fill=tk.BOTH)
    #Hien thi du lieu theo trang
    start = page * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE
    for index, row in df.iloc[start:end].iterrows():
        tree.insert("", "end", values=list(row))
    
    #Tao cac nut dieu huong
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    prev_button = tk.Button(button_frame, text="Previous Page", command=prev_page, state=tk.DISABLED)
    prev_button.pack(side=tk.LEFT, padx=5, pady=5)
    next_button = tk.Button(button_frame, text="Next page", command=next_page, state=tk.DISABLED)
    next_button.pack(side=tk.RIGHT, padx=5, pady=5)
    back_button = tk.Button(button_frame, text="Back", command=show_menu)
    back_button.pack(side= tk.LEFT, padx=5, pady=5)
    current_page = page
    prev_button.config(state=tk.NORMAL if current_page > 0 else tk.DISABLED)
    next_button.config(state=tk.NORMAL if (current_page + 1) * ROWS_PER_PAGE < len(df) else tk.DISABLED)
def show_add_form():
    #Hien thi form nhap du lieu
    clear_window()
    label = tk.Label(root, text="ADD DATA", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # Frame chua form nhap du lieu
    form_frame = tk.Frame(root)
    form_frame.pack(pady=20)
    # danh sach cac truong can nhap
    fields = [
        "id", "track_name", "size_bytes", "currency", "price",
        "rating_count_tot", "rating_count_ver", "user_rating", 
        "user_rating_ver", "ver", "cont_rating", "prime_genre", 
        "sup_devices.num", "ipadSc_urls.num", "lang.num", "vpp_lic"
    ]
    entries = {}
    # Tao cac o nhap du lieu
    for i, field in enumerate(fields):
        label = tk.Label(form_frame, text=field, font=("Times New Roman", 15))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(form_frame, font=("Times New Roman", 15), width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    # Tao nut save
    def save_data():
        # Tap hop du lieu tu cac truong nhap
        new_data = {field: entry.get() for field, entry in entries.items()}
        
        # Goi ham 
        CRUD.Create(df, new_data)
        label = tk.Label(root, text="Dataset updated and saved", font=("Times New Roman", 20, "bold"))
        label.pack(pady=10)
        

    save_button = tk.Button(root, text="Save", font=("Times New Roman", 15), command=save_data)
    save_button.pack(pady=10)

    # Nut back
    back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)

def show_update_form():
    #Hien thi giao dien
    clear_window()

    # Tieu de
    label = tk.Label(root, text="Update Data", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # frame tim kiem
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="track name:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 15), width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # frame hien thi thong tin
    info_frame = tk.Frame(root)
    info_frame.pack(pady=20)

    # Lay danh sach cac cot
    columns = list(df.columns)

    def search_app():
        #Tim kiem theo track name
        for widget in info_frame.winfo_children():
            widget.destroy()

        app_name = search_entry.get()
        filtered_df = df[df["track_name"].str.contains(app_name, case=False)]

        if filtered_df.empty:
            tk.Label(info_frame, text=f"No item found with name '{app_name}'.", font=("Times New Roman", 15), fg="red").pack()
            return

        # Hien thi thong tin tim kiem duoc
        tk.Label(info_frame, text=f"Found {len(filtered_df)} app(s):", font=("Times New Roman", 15, "bold")).pack()
        for idx, row in filtered_df.iterrows():
            tk.Label(info_frame, text=f"- {row['track_name']} (ID: {row['id']})", font=("Times New Roman", 15)).pack()

        # form cap nhat
        update_frame = tk.Frame(root)
        update_frame.pack(pady=20)

        tk.Label(update_frame, text="Select Column:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        column_combobox = ttk.Combobox(update_frame, values=columns, font=("Times New Roman", 15))
        column_combobox.grid(row=0, column=1, padx=10, pady=5)
        column_combobox.current(0)

        tk.Label(update_frame, text="New Value:", font=("Times New Roman", 15)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        value_entry = tk.Entry(update_frame, font=("Times New Roman", 15), width=30)
        value_entry.grid(row=1, column=1, padx=10, pady=5)

        def save_update():
            #Luu thay doi
            column_to_update = column_combobox.get()
            new_value = value_entry.get()

            for idx in filtered_df.index:
                message = CRUD.Update(df, filtered_df.loc[idx, "track_name"], column_to_update, new_value)
                tk.Label(root, text=message, font=("Times New Roman", 15), fg="green").pack(pady=10)

        save_button = tk.Button(update_frame, text="Save", font=("Times New Roman", 15), command=save_update)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)
    label = tk.Label(root, text="Dataset updated and saved", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)
    # Tao nut tim kiem
    search_button = tk.Button(search_frame, text="Search", font=("Times New Roman", 15), command=search_app)
    search_button.grid(row=0, column=2, padx=10, pady=5)

    # Tao nut back to menu
    back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)



def show_delete_form():
    """
    Hiển thị giao diện để xóa ứng dụng.
    """
    clear_window()

    # Tao tieu de
    label = tk.Label(root, text="Delete", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # Frame tim kiem
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="App Name:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 15), width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # Frame hien thi ke qua
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20)

    def search_app():
        #Tim kiem va hien thi ke qua tim kiem
        for widget in result_frame.winfo_children():
            widget.destroy()

        app_name = search_entry.get()
        filtered_df = df[df["track_name"].str.contains(app_name, case=False)]

        if filtered_df.empty:
            tk.Label(result_frame, text=f"No item found with name '{app_name}'.", font=("Times New Roman", 15), fg="red").pack()
            return

        tk.Label(result_frame, text=f"Found {len(filtered_df)} item(s):", font=("Times New Roman", 15, "bold")).pack()
        for idx, row in filtered_df.iterrows():
            tk.Label(result_frame, text=f"- {row['track_name']} (ID: {row['id']})", font=("Times New Roman", 15)).pack()

        # frame xoa
        delete_frame = tk.Frame(root)
        delete_frame.pack(pady=20)

        def delete_app():
            #Xoa khoi dataframe
            for idx in filtered_df.index:
                app_to_delete = filtered_df.loc[idx, "track_name"]
                message = CRUD.Delete(df, app_to_delete)
                tk.Label(root, text=message, font=("Times New Roman", 15), fg="green").pack(pady=10)
            search_app()
            label = tk.Label(root, text="Delete Successfully!", font=("Times New Roman", 20, "bold"))
            label.pack(pady=10)

        delete_button = tk.Button(delete_frame, text="Delete All", font=("Times New Roman", 15), command=delete_app)
        delete_button.pack(pady=10)

    # Tao nut tim kiem
    search_button = tk.Button(search_frame, text="Search", font=("Times New Roman", 15), command=search_app)
    search_button.grid(row=0, column=2, padx=10, pady=5)
    
    # Tao nut back to menu
    back_button = tk.Button(root, text="Back", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)

show_menu()
root.mainloop()
