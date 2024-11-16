import pandas as pd
import function as f

my_df = pd.read_csv("AppleStore.csv")
my_df = my_df.loc[:, ~my_df.columns.str.contains("^Unnamed")]


# 1. CREATE a new row in the data set
def Create(my_df):
    new_app = {}
    new_app["id"] = int(input("Enter the app ID: "))
    new_app["track_name"] = input("Enter the app name: ")
    new_app["size_bytes"] = int(input("Enter the app size (in bytes): "))
    new_app["currency"] = input("Enter the currency: ")
    new_app["price"] = float(input("Enter the app price: "))
    new_app["rating_count_tot"] = int(input("Enter the total rating count: "))
    new_app["rating_count_ver"] = int(input("Enter the version rating count: "))
    new_app["user_rating"] = float(input("Enter the user rating: "))
    new_app["user_rating_ver"] = float(input("Enter the user rating for the version: "))
    new_app["ver"] = input("Enter the version: ")
    new_app["cont_rating"] = input("Enter the content rating: ")
    new_app["prime_genre"] = input("Enter the primary genre: ")
    new_app["sup_devices.num"] = int(input("Enter the number of supported devices: "))
    new_app["ipadSc_urls.num"] = int(input("Enter the number of iPad screenshots: "))
    new_app["lang.num"] = int(input("Enter the number of languages: "))
    new_app["vpp_lic"] = int(input("Enter the VPP license (0 or 1): "))

    # create DataFrame from new application and merge into current DataFrame
    new_app_df = pd.DataFrame(new_app, index=[0])
    updated_df = pd.concat([my_df, new_app_df], ignore_index=True)

    # save data
    updated_df.to_csv("AppleStore.csv")
    print("Dataset updated and saved ")


# 2. READ data from the my_dfset
def Read(my_df):
    print()
    print("Reading dataset:")
    print(my_df.head(100))
    print(my_df.describe())


# 3. Update the information of the app
def Update(my_df):
    
    # Menu
    while True:
        print()
        print("Enter 0 to exit")
        print("Enter the name of the app you want to update: ", end="")
        f.Search(my_df["track_name"])

        if f.c == "0":
            break
        
        else:
            
            # Show app in list search for user to choice
            while True:
                print()
                idx = 0
                for i in f.list_search:
                    idx += 1
                    print(idx, i)

                if len(f.list_search) != 0:
                    print("Enter 0 to exit")
                    choice = int(input("Enter the number corresponding to the app name you want to update: "))

                    if choice == 0:
                        break

                    if choice < 0 or choice > len(f.list_search):
                        print("ERROR!")

                    else:
                        
                        # Get the row index of the selected app
                        idx_drop = my_df[my_df["track_name"] == f.list_search[choice - 1]].index

                        # Show option for user to choice
                        while True:
                            app_row = my_df.loc[idx_drop]
                            
                            index = 0
                            print()
                            for column in app_row.columns:
                                index += 1
                                print(f"{index} {column}: {app_row.iloc[0][column]}")

                            print("Enter 0 to exit")
                            update_choice = int(input("Enter the number corresponding to the information of the app you want to update: "))

                            if update_choice == 0:
                                break

                            if update_choice < 1 or update_choice > len(my_df.columns):
                                print("ERROR!")

                            else:
                                
                                # Update new information with the selected column
                                column_to_update = my_df.columns[update_choice - 1]
                                new_value = input(f"Enter the new information for '{column_to_update}': ")
                                my_df.loc[idx_drop, column_to_update] = new_value
                                
                                # Check if column_to_update is "track_name": update list search
                                if column_to_update == "track_name":
                                    if f.c.lower() not in new_value.lower():
                                        f.list_search.remove(f.list_search[choice - 1])
                                    else:
                                        f.list_search[choice - 1] = new_value
                                    
                                # Overwrite the file and update list search
                                my_df.to_csv("AppleStore.csv")
                                print("Updated successfully!")

                else:
                    print("No result!")
                    break

                      
# 4. Delete row
def Delete(my_df):
    
    # Menu
    while True:
        print()
        print("Enter 0 to exit")
        print("Enter the name of the app you want to delete: ", end="")
        f.Search(my_df["track_name"])
        
        if f.c == "0":
            break
        
        else:
            while True:
                
                # Show app in list search for user to choice
                print()
                idx = 0
                for i in f.list_search:
                    idx += 1
                    print(idx, i)

                if len(f.list_search) != 0:
                    print("Enter 0 to exit")
                    choice = int(input("Enter the number corresponding to the app name you want to delete: "))

                    if choice == 0:
                        break

                    if choice < 0 or choice > len(f.list_search):
                        print("ERROR!")

                    else:
                        
                        # Delete the row with the selected app name
                        idx_drop = my_df[my_df["track_name"] == f.list_search[choice - 1]].index
                        my_df.drop(idx_drop, inplace=True)
                        
                        # Overwrite the file and update list search
                        my_df.to_csv("AppleStore.csv")
                        f.list_search.remove(f.list_search[choice - 1])
                        print("Deleted successfully!")

                else:
                    print("No result!")
                    break
            
