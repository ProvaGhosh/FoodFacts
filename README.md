# FoodFacts

This Python project, **FoodFacts**, is designed to provide detailed nutritional information for various food ingredients. Utilizing a comprehensive nutrition database API, this tool fetches and displays macronutrient and micronutrient data for user-specified food items, making it an essential tool for anyone interested in dietary analysis and nutrition tracking.

The application allows users to input food ingredients and retrieve accurate nutritional data quickly. It presents information on key macronutrients like calories, protein, carbohydrates, and fats, as well as important micronutrients such as vitamins and minerals. This functionality makes FoodFacts valuable for nutritionists, dietitians, fitness enthusiasts, and individuals monitoring their dietary intake. With its user-friendly interface and robust data retrieval capabilities, FoodFacts streamlines the process of nutritional analysis, offering a practical solution for those seeking to understand the nutritional content of their food in detail.

## Key Features
- Real-time nutritional data retrieval
- Customizable ingredient quantity analysis
- Comprehensive macro and micronutrient breakdown
- Secure API key management using environment variables
- Error handling for API requests and data processing

## Technical Details
- Utilizes the `requests` library for API communication
- Implements environment variable management with `python-dotenv`
- Handles API request exceptions and unexpected response formats
- Provides a simple command-line interface for user interaction

## How It Works
1. Users input an ingredient, optionally specifying a quantity.
2. The application fetches nutritional data from the Edamam API.
3. Results are processed and displayed in a readable format.

## Code Structure
- API interaction is encapsulated in the `get_food_data` function.
- Data display logic is contained in the `display_food_info` function.
- User interaction is managed through the `analyze_single_ingredient` and `main` functions.

## Skills Demonstrated
- **API Integration**: Seamless connection with external data sources.
- **Data Processing**: Efficient parsing and presentation of complex nutritional data.
- **User Interface Design**: Creation of an intuitive command-line experience.
- **Error Handling**: Robust system for managing API and user input exceptions.
- **Security Best Practices**: Proper handling of API credentials.

This project showcases skills in API integration, data processing, and creating user-friendly command-line applications. It's a practical tool for anyone interested in quick nutritional analysis of food ingredients.

## Getting Started

### Prerequisites
- Python 3.x
- `requests` library
- `python-dotenv` library

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/foodfacts.git
    cd foodfacts
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Edamam API credentials:
    ```env
    API_KEY=your_api_key_here
    APP_ID=your_app_id_here
    ```

### Usage
Run the application:
```bash
python foodfacts.py
