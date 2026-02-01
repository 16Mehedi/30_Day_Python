#Grocery list manager
banner="Your grocery list manager"
print(banner.title())
print("".ljust(20,"="))

#Holds all grocery in the list
grocery_list=[]

is_app_running= True

while is_app_running:
    print("""
    Select an option (1-4)
    1. Add item
    2. Remove item
    3. View list
    4. Quit"""

    )
    user_selection= input("Enter selection here:")

    if user_selection=="1":
        while True:
            print("Enter item name or enter 2 to go back")
            add_to_list=input()
            if add_to_list=="2":
                break
            else:
                add_to_list=add_to_list.capitalize()
                grocery_list.append(add_to_list)

                print(f"{add_to_list} successfully added")

                continue
    

    elif user_selection == "2":
        # Inner loop keeps the user in remove mode
        # until they choose to go back
        while True:
            print("Enter the item you wish to remove or enter 2 to go back: ")
            remove_from_list = input()

            # Exit remove-item mode and return to main menu
            if remove_from_list == "2":
                break

            # Normalize capitalization to match stored list values
            remove_from_list = remove_from_list.capitalize()

            # Check if the item exists before attempting removal
            if remove_from_list in grocery_list:
                grocery_list.remove(remove_from_list)

                # Confirm successful removal
                print(f"{remove_from_list} successfully removed")

                # Stay in remove-item mode
                continue
            else:
                # Graceful handling when item is not found
                print("Item not found!")

    # ---- VIEW LIST MODE ----
    # Displays the current contents of the grocery list
    elif user_selection == "3":
        print("Your current list:")
        print(grocery_list)
        continue

    # ---- QUIT APPLICATION ----
    # Flips the master control flag to exit the app loop
    elif user_selection == "4":
        is_app_running = False

    # ---- INVALID INPUT HANDLING ----
    # Catches any unexpected menu input
    else:
        print("Invalid selection")
        continue