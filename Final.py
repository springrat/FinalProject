#Program to read Data Base of Allegheny County Lifetime Dog Licenses
import csv 
import pandas as pd

df = pd.read_csv('2099-05-01.csv')
reader = csv.DictReader(df)

def menu():
    
    print('Allegheny County Lifetime Dog License Data \n\n')
    print('1. View Full List of Breeds \n')
    print('2. View Specific Breeds \n')
    print('3. View Total Lifetime Licenses \n')
    print('4. View License per ZipCode \n')
    print('5. View Data Statistics \n')
    print('6. Exit \n\n')
    print('Enter Numeric Choice: \n')
    choice = (input())
    
# 1 --- Breeds - Full Doc
    if choice == "1":
        print("Do you wish to view: \n")
        full = print("a. Full Document")
        if full == "a":
            (print(df.sort_values('Breed')))
        restart = input(print('Return to Menu? y/n: \n'))
        if restart == "y":
            menu()            
        else: exit()            
                
# 2 --- Specific Breeds 
    if choice == "2":
        print('First 3: \n')
        print(df.set_index(['Breed']).LicenseType.head(3), '\n')
        print('Bottom 3: \n')
        print(df.set_index(['OwnerZip']).LicenseType.tail(3), '\n')
        print(df.sort_values(['Breed', 'ValidDate'], ascending=[1,0]))
        
        restart = input(print('Return to Menu? y/n: \n'))
        if restart == "y":
            menu()            
        else: exit()                
        
# 3 --- Total LifeTime Licenses Given    
    if choice == "3":
        print("Number of Licenses per ZipCode:")
        print(df.set_index(["LicenseType", "OwnerZip"]).count(level="OwnerZip"))
        
        restart = input(print('Return to Menu? y/n: \n'))
        if restart == "y":
            menu()            
        else: exit() 
               
# 4 --- License per Zipcode    
    if choice == "4":
        print('First 3: \n')
        print(df.set_index(['OwnerZip']).LicenseType.head(3), '\n')
        print('Bottom 3: \n')
        print(df.set_index(['OwnerZip']).LicenseType.tail(3), '\n')
        
        restart = input(print('Return to Menu? y/n: \n'))
        if restart == "y":
            menu()            
        else: exit()
        
#--- Zipcode - Full Doc        
        zpcd = print("To View Full Document Enter 'x': \n")
        if zpcd == "x":
            print(df.set_index(['OwnerZip']).LicenseType)
            
        restart = input(print('Return to Menu? y/n: \n'))
        if restart == "y":
            menu()            
        else: exit()    
            
# 5 --- Data Statistics       
    if choice == "5":
        print (df.describe())
        
        restart = input(print('Return to Menu? y/n: \n'))       
        if restart == "y":
            menu()            
        else: exit()
                        
# 6 --- Main Menu Exit    
    if choice == "exit" or "6":
        exit()
        
        
    else:
        print("Error! Please enter a value between 1-6")   
                
menu()
