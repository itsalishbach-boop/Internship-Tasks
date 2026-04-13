"""
USER MANAGEMENT SYSTEM
A complete system for managing user data from Excel files with authentication,
user creation, data retrieval, and reporting features.

Dependencies:
    - pandas: For Excel file handling and data manipulation
    - tabulate: For formatted table output in reports
"""

import pandas as pd
from tabulate import tabulate

# ============================================================================
# CONFIGURATION
# ============================================================================

# Path to the Excel file containing user data
EXCEL_FILE = "/home/alishbach/Documents/Task 2 Data.xlsx"


# ============================================================================
# DATA LOADING & SAVING FUNCTIONS
# ============================================================================

def load_data():
    """
    Load user data from Excel file into a pandas DataFrame.
    
    Attempts to read the Excel file specified by EXCEL_FILE constant.
    Displays success message with record count or error message if failed.
    
    Returns:
        pandas.DataFrame: DataFrame containing all user data if successful
        None: If file not found or any error occurs during loading
    """
    try:
        # Read Excel file using pandas
        data = pd.read_excel(EXCEL_FILE)
        print("File found:", EXCEL_FILE)
        print("Total records:", len(data))
        return data
    except Exception as e:
        # Handle any errors (file not found, corrupted file, etc.)
        print("Error:", e)
        return None


def save_data(data):
    """
    Save DataFrame back to the Excel file.
    
    Writes the modified DataFrame to the same Excel file,
    overwriting the existing data.
    
    Args:
        data (pandas.DataFrame): DataFrame to save to Excel file
    """
    data.to_excel(EXCEL_FILE, index=False)
    print("Data saved!")


# ============================================================================
# AUTHENTICATION FUNCTIONS
# ============================================================================

def authenticate_user(data):
    """
    Authenticate user by checking first name and password.
    
    Prompts user for first name and password, then validates against the database.
    Uses case-insensitive matching for first names.
    
    Args:
        data (pandas.DataFrame): DataFrame containing user records with columns:
            - First Name: User's first name
            - Email: User's email address
            - Password: User's password (plain text)
    
    Returns:
        pandas.Series: User's data row if authentication successful
        None: If user not found or password incorrect
    """
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


# ============================================================================
# USER CREATION FUNCTIONS
# ============================================================================

def creation_module(data):
    """
    Create a new user and add to the database.
    
    Prompts user for all required information, automatically generates
    a new serial number, and appends to existing data.
    
    Args:
        data (pandas.DataFrame): Current DataFrame with existing users
    
    Returns:
        pandas.DataFrame: Updated DataFrame with new user added
    """
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


# ============================================================================
# DATA RETRIEVAL FUNCTIONS
# ============================================================================

def data_retrieval(user_data):
    """
    Display specific field information for the authenticated user.
    
    Shows all available fields for the user and allows them to select
    which field to view.
    
    Args:
        user_data (pandas.Series): The authenticated user's data row
    """
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


# ============================================================================
# REPORTING FUNCTIONS
# ============================================================================

def system_report(data):
    """
    Generate comprehensive system report with statistics and all user data.
    
    Displays:
        - Total user count
        - Age statistics (min, max, average, age groups)
        - Gender distribution with percentages
        - Occupation distribution
        - Complete table of all users (excluding passwords)
    
    Args:
        data (pandas.DataFrame): Complete DataFrame with all user records
    """
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


# ============================================================================
# MENU SYSTEM
# ============================================================================

def main_menu(data, user_data):
    """
    Display and handle the main menu interface.
    
    Provides options for:
        1. CREATE - Add new user
        2a. READ - View specific user data
        2b. READ - View system report with all users
        3. EXIT - Exit the program
    
    Args:
        data (pandas.DataFrame): Complete DataFrame with all user records
        user_data (pandas.Series): Current authenticated user's data
    """
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


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """
    Main entry point for the User Management System.
    
    Orchestrates the entire program flow:
        1. Display welcome message
        2. Load data from Excel file
        3. Authenticate user
        4. Launch main menu if authentication successful
    """
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
