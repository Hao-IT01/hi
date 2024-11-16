import pandas as pd
import function as f

# Load the dataset and clean it up
try:
    my_df = pd.read_csv("AppleStore.csv")
    my_df = my_df.loc[:, ~my_df.columns.str.contains("^Unnamed")]
except FileNotFoundError:
    print("Error: AppleStore.csv not found! Please ensure the file is in the correct directory.")
    exit()

# 1. CREATE a new row in the dataset
def add_new_row(my_df):
    try:
        new_app = {
            'id': int(input("Enter the app ID: ")),
            'track_name': input("Enter the app name: "),
            'size_bytes': int(input("Enter the app size (in bytes): ")),
            'currency': input("Enter the currency: "),
            'price': float(input("Enter the app price: ")),
            'rating_count_tot': int(input("Enter the total rating count: ")),
            'rating_count_ver': int(input("Enter the version rating count: ")),
            'user_rating': float(input("Enter the user rating: ")),
            'user_rating_ver': float(input("Enter the user rating for the version: ")),
            'ver': input("Enter the version: "),
            'cont_rating': input("Enter the content rating: "),
            'prime_genre': input("Enter the primary genre: "),
            'sup_devices.num': int(input("Enter the number of supported devices: ")),
            'ipadSc_urls.num': int(input("Enter the number of iPad screenshots: ")),
            'lang.num': int(input("Enter the number of languages: ")),
            'vpp_lic': int(input("Enter the VPP license (0 or 1): "))
        }

        new_app_df = pd.DataFrame([new_app])
        updated_df = pd.concat([my_df, new_app_df], ignore_index=True)
        updated_df.to_csv("AppleStore.csv", index=False)
        print("New app added successfully!")
        return updated_df
    except ValueError:
        print("Error: Invalid input type. Please try again.")
        return my_df

# 2. READ data from the dataset
def read_data(my_df):
    print("\nReading dataset:")
    print(my_df.head(), "\n")
    print(my_df.describe())

# 3. Update the information of an app
def update_row(my_df):
    while True:
        print("\nEnter 0 to exit.")
        print("Enter the name of the app you want to update: ", end="")
        f.Search(my_df["track_name"])

        if f.c == "0":
            break
        elif len(f.list_search) == 0:
            print("No matching app found!")
        else:
            while True:
                print("\nAvailable apps:")
                for idx, app_name in enumerate(f.list_search, start=1):
                    print(f"{idx}. {app_name}")

                print("Enter 0 to exit.")
                choice = int(input("Select the app number to update: "))

                if choice == 0:
                    break
                elif 1 <= choice <= len(f.list_search):
                    selected_app = f.list_search[choice - 1]
                    app_index = my_df[my_df["track_name"] == selected_app].index[0]

                    print("\nCurrent details of the app:")
                    for i, column in enumerate(my_df.columns, start=1):
                        print(f"{i}. {column}: {my_df.at[app_index, column]}")

                    update_choice = int(input("\nSelect the field to update (0 to cancel): "))

                    if update_choice == 0:
                        break
                    elif 1 <= update_choice <= len(my_df.columns):
                        column_to_update = my_df.columns[update_choice - 1]
                        new_value = input(f"Enter the new value for '{column_to_update}': ")
                        my_df.at[app_index, column_to_update] = new_value
                        my_df.to_csv("AppleStore.csv", index=False)
                        print("App updated successfully!")
                    else:
                        print("Invalid choice!")
                else:
                    print("Invalid selection!")
    return my_df

# 4. DELETE a row
def delete_row(my_df):
    while True:
        print("\nEnter 0 to exit.")
        print("Enter the name of the app you want to delete: ", end="")
        f.Search(my_df["track_name"])

        if f.c == "0":
            break
        elif len(f.list_search) == 0:
            print("No matching app found!")
        else:
            print("\nAvailable apps:")
            for idx, app_name in enumerate(f.list_search, start=1):
                print(f"{idx}. {app_name}")

            print("Enter 0 to exit.")
            choice = int(input("Select the app number to delete: "))

            if choice == 0:
                break
            elif 1 <= choice <= len(f.list_search):
                selected_app = f.list_search[choice - 1]
                app_index = my_df[my_df["track_name"] == selected_app].index[0]
                my_df = my_df.drop(app_index).reset_index(drop=True)
                my_df.to_csv("AppleStore.csv", index=False)
                print("App deleted successfully!")
            else:
                print("Invalid selection!")
    return my_df

# Main execution for CRUD operations
while True:
    print("\nSelect an option:")
    print("1. Add a new app (Create)")
    print("2. View data (Read)")
    print("3. Update an app (Update)")
    print("4. Delete an app (Delete)")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        my_df = add_new_row(my_df)
    elif choice == "2":
        read_data(my_df)
    elif choice == "3":
        my_df = update_row(my_df)
    elif choice == "4":
        my_df = delete_row(my_df)
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
