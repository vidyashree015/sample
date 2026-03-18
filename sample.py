import os

def calculate_area(radius):
    # Smell 1: Unused variable
    pi_value = 3.14159
    result = 3.14 * radius * radius
    return result

def main():
    # Smell 2: Hardcoded secret
    api_key = "12345-ABCDE-SECRET-KEY"
    
    # Smell 3: Duplicate logic
    r1 = 5
    area1 = 3.14 * r1 * r1
    print("Area is:", area1)
    
    r2 = 10
    area2 = 3.14 * r2 * r2 
    print("Area is:", area2)

    # Smell 4: Bare except block
    try:
        f = open("non_existent_file.txt")
    except:
        pass

if _name_ == "_main_":
    main()



