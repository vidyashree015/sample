import math

# 1. We use 'math.pi' for better accuracy and no unused variables
def calculate_area(radius: float) -> float:
    """Calculates the area of a circle."""
    return math.pi * (radius ** 2)

def main():
    # 2. FIX: Hardcoded API Key removed (Security Hotspot resolved)
    
    # 3. FIX: Using a loop and a function to avoid duplication (Code Smell resolved)
    radii = [5, 10]
    for r in radii:
        area = calculate_area(r)
        print(f"Area for radius {r} is: {area:.2f}")

    # 4. FIX: Handling a specific error instead of a bare 'except' (Reliability improved)
    try:
        with open("non_existent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Note: Optional file not found, moving on.")

if _name_ == "_main_":
    main()

