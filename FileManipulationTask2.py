import pandas as pd
from tabulate import tabulate

EXCEL_FILE = "/home/alishbach/Documents/Task 2 Data.xlsx"

def load_data():
    try:
        data = pd.read_excel(EXCEL_FILE)
        print("File found:", EXCEL_FILE)
        print("Total records:", len(data))
        return data
    except Exception as e:
        print("Error:", e)
        return None

def save_data(data):
    data.to_excel(EXCEL_FILE, index=False)
    print("Data saved!")

def authenticate_user(data):
    print("\n" + "="*40)
    print("LOGIN SYSTEM")
    print("="*40)
    
    print("Enter First Name: ", end="")
    name = input()
    name = name.strip()
    
    if not name:
        print("No name entered!")
        return None
    
    print("Searching for:", name)
    
    result = data[data["First Name"].str.lower() == name.lower()]
    
    if result.empty:
        print("User Not Found")
        return None
    
    print("\nUser Found")
    email = result.iloc[0]["Email"]
    print("Email:", email)
    
    print("Enter Password: ", end="")
    password = input()
    real_pass = str(result.iloc[0]["Password"])
    
    if password == real_pass:
        print("Authentication Successful!\n")
        return result.iloc[0]
    else:
        print("Wrong Password")
        return None

def creation_module(data):
    print("\n" + "="*40)
    print("CREATE NEW USER")
    print("="*40)
    
    new_user = {}
    new_user["S.No"] = data["S.No"].max() + 1 if not data.empty else 1
    
    print("First Name: ", end="")
    new_user["First Name"] = input().strip()
    
    print("Last Name: ", end="")
    new_user["Last Name"] = input().strip()
    
    while True:
        try:
            print("Age: ", end="")
            new_user["Age"] = int(input())
            break
        except:
            print("Please enter a valid number!")
    
    print("Gender (Male/Female/Other): ", end="")
    new_user["Gender"] = input().strip()
    
    print("Occupation: ", end="")
    new_user["Occupation"] = input().strip()
    
    print("Email: ", end="")
    new_user["Email"] = input().strip()
    
    print("Set Password: ", end="")
    new_user["Password"] = input()
    
    new_df = pd.DataFrame([new_user])
    data = pd.concat([data, new_df], ignore_index=True)
    save_data(data)
    
    print("\nNew user added!")
    return data

def data_retrieval(user_data):
    print("\n" + "="*40)
    print("DATA RETRIEVAL")
    print("="*40)
    
    print("Available fields:")
    fields = list(user_data.index)
    for i, field in enumerate(fields, 1):
        print(" ", i, ".", field)
    
    print("Which field? ", end="")
    field_name = input().strip()
    
    if field_name in user_data.index:
        print("\n", field_name, ":", user_data[field_name])
    else:
        print("Invalid field!")
    
    print("Press Enter to continue...", end="")
    input()

def system_report(data):
    print("\n" + "="*50)
    print("SYSTEM REPORT - All Users Data with Statistics")
    print("="*50)
    
    print("\nSTATISTICS")
    print("-" * 40)
    
    total_users = len(data)
    print("Total Users:", total_users)
    
    if "Age" in data.columns:
        min_age = data["Age"].min()
        max_age = data["Age"].max()
        avg_age = data["Age"].mean()
        print("\nAge Range:", min_age, "to", max_age, "years")
        print("Average Age:", round(avg_age, 1), "years")
        
        print("\nAge Groups:")
        children = len(data[data["Age"] < 18])
        young = len(data[(data["Age"] >= 18) & (data["Age"] <= 30)])
        adult = len(data[(data["Age"] >= 31) & (data["Age"] <= 50)])
        senior = len(data[data["Age"] > 50])
        
        print("  Under 18:", children, "users")
        print("  18-30 years:", young, "users")
        print("  31-50 years:", adult, "users")
        print("  50+ years:", senior, "users")
    
    if "Gender" in data.columns:
        print("\nGender Distribution:")
        males = len(data[data["Gender"].str.lower() == "male"])
        females = len(data[data["Gender"].str.lower() == "female"])
        others = len(data[~data["Gender"].str.lower().isin(["male", "female"])])
        
        print("  Male:", males, "users")
        print("  Female:", females, "users")
        print("  Other:", others, "users")
        
        if total_users > 0:
            print("\n  Male Percentage:", round((males/total_users)*100, 1), "%")
            print("  Female Percentage:", round((females/total_users)*100, 1), "%")
    
    if "Occupation" in data.columns:
        print("\nOccupation Distribution:")
        occupation_counts = data["Occupation"].value_counts()
        for occ, count in occupation_counts.items():
            print(" ", occ, ":", count, "users")
    
    print("\n" + "="*50)
    print("ALL USERS DATA")
    print("="*50)
    
    if "Password" in data.columns:
        report_data = data.drop(columns=["Password"])
    else:
        report_data = data.copy()
    
    print(tabulate(report_data, headers="keys", tablefmt="grid", showindex=False))
    
    print("\nPress Enter to continue...", end="")
    input()

def main_menu(data, user_data):
    while True:
        print("\n" + "="*40)
        print("MAIN MENU")
        print("="*40)
        print("1. CREATE - Add new user")
        print("2. READ")
        print("   2a. Data Retrieval - View your data")
        print("   2b. System Report - View all users with statistics")
        print("3. EXIT")
        print("="*40)
        
        print("Your choice (1/2a/2b/3): ", end="")
        choice = input().strip().lower()
        
        if choice == "1":
            data = creation_module(data)
        elif choice == "2a":
            data_retrieval(user_data)
        elif choice == "2b":
            system_report(data)
        elif choice == "3":
            print("\nGoodbye! Exiting system.")
            break
        else:
            print("Invalid choice!")

def main():
    print("\n" + "="*50)
    print("WELCOME TO USER MANAGEMENT SYSTEM")
    print("="*50)
    
    data = load_data()
    if data is None:
        return
    
    user_data = authenticate_user(data)
    if user_data is not None:
        main_menu(data, user_data)

if __name__ == "__main__":
    main()