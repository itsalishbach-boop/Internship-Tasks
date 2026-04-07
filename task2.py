import pandas as pd

# Excel file read
data = pd.read_excel("Task 2 Data.xlsx")

# user se name lo
name = input("Enter First Name: ").strip().capitalize()

# search record
result = data[data["First Name"] == name]

if not result.empty:
    print("\nUser Found ✅")
    
    # email show karo
    email = result.iloc[0]["Email"]
    print("Email:", email)
    
    # user se password lo
    user_pass = input("Enter Password: ")
    
    # original password
    real_pass = str(result.iloc[0]["Password"])
    
    # check password
    if user_pass == real_pass:
        print("✅ Authenticated (Correct Password)")
    else:
        print("❌ Wrong Password")

else:
    print("❌ User Not Found")