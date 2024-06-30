import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and app ID from environment variables
API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

# Print environment variables to ensure they are loaded correctly (for debugging)
print(f"API_KEY: {API_KEY}")
print(f"APP_ID: {APP_ID}")

def get_food_data(food_name):
    base_url = "https://api.edamam.com/api/nutrition-data"
    params = {
        "app_id": APP_ID,
        "app_key": API_KEY,
        "ingr": food_name
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data.get("totalNutrients")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except KeyError:
        print("Unexpected response format")
        print(f"Response content: {response.text}")
        return None

def display_food_info(nutrients, quantity=100):
    if nutrients:
        factor = quantity / 100.0

        print("\n--- Nutrition Information for {}g ---".format(quantity))

        print("\nMacronutrients:")
        print(f"  - Calories: {nutrients.get('ENERC_KCAL', {'quantity': 0})['quantity'] * factor:.2f} kcal")
        print(f"  - Protein: {nutrients.get('PROCNT', {'quantity': 0})['quantity'] * factor:.2f} g")
        print(f"  - Carbohydrates: {nutrients.get('CHOCDF', {'quantity': 0})['quantity'] * factor:.2f} g")
        print(f"  - Fat: {nutrients.get('FAT', {'quantity': 0})['quantity'] * factor:.2f} g")

        print("\nMicronutrients:")
        print(f"  - Vitamin A: {nutrients.get('VITA_RAE', {'quantity': 0})['quantity'] * factor:.2f} µg")
        print(f"  - Vitamin C: {nutrients.get('VITC', {'quantity': 0})['quantity'] * factor:.2f} mg")
        print(f"  - Calcium: {nutrients.get('CA', {'quantity': 0})['quantity'] * factor:.2f} mg")
        print(f"  - Iron: {nutrients.get('FE', {'quantity': 0})['quantity'] * factor:.2f} mg")
    else:
        print("Food not found or no data available.")

def analyze_single_ingredient():
    ingredient = input("Enter an ingredient (e.g., '100g chicken'): ")
    quantity = 100
    food_name = ingredient

    # Check if quantity is specified
    parts = ingredient.split()
    if len(parts) > 1 and parts[0].isdigit() and parts[1].lower() in ['g', 'gram', 'grams']:
        quantity = int(parts[0])
        food_name = ' '.join(parts[2:])

    food_data = get_food_data(food_name)
    display_food_info(food_data, quantity)

def analyze_recipe():
    print("Recipe analysis is not implemented in this version.")

def main():
    print("Welcome to FoodFacts Analyzer")

    while True:
        print("\n1. Analyze a single ingredient")
        print("2. Analyze a recipe")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            analyze_single_ingredient()
        elif choice == '2':
            analyze_recipe()
        elif choice == '3':
            print("Thank you for using FoodFacts Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
