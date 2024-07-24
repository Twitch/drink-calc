#!/usr/bin/env python3

import math

# Default values for preferences and consumption rate
DEFAULT_GUESTS = 50
DEFAULT_HOURS = 4
DEFAULT_BEER_PREFERENCE = 1.0
DEFAULT_WINE_PREFERENCE = 1.0
DEFAULT_COCKTAIL_PREFERENCE = 1.0
DEFAULT_CONSUMPTION_RATE = 1.0  # 1.0 is average, >1.0 for heavier drinking, <1.0 for lighter drinking

# Standard drink calculations
DRINKS_PER_PERSON_PER_HOUR = 1
BEER_PERCENTAGE = 0.4
WINE_PERCENTAGE = 0.3
COCKTAIL_PERCENTAGE = 0.3

def get_input(prompt, default, input_type=float):
    user_input = input(f"{prompt} (default {default}): ")
    return input_type(user_input) if user_input else default

def calculate_drinks(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate):
    total_drinks = guests * hours * DRINKS_PER_PERSON_PER_HOUR * consumption_rate
    
    # Calculate preference weights
    total_preference = beer_pref + wine_pref + cocktail_pref
    beer_weight = beer_pref / total_preference
    wine_weight = wine_pref / total_preference
    cocktail_weight = cocktail_pref / total_preference
    
    # Calculate drinks by type
    beers = math.ceil(total_drinks * beer_weight * BEER_PERCENTAGE)
    wines = math.ceil(total_drinks * wine_weight * WINE_PERCENTAGE)
    cocktails = math.ceil(total_drinks * cocktail_weight * COCKTAIL_PERCENTAGE)
    
    return beers, wines, cocktails

def main():
    print("Welcome to the Open Bar Calculator!")
    print("Please enter the following information:")

    guests = get_input("Number of guests", DEFAULT_GUESTS, int)
    hours = get_input("Hours of service", DEFAULT_HOURS, int)
    beer_pref = get_input("Beer preference", DEFAULT_BEER_PREFERENCE)
    wine_pref = get_input("Wine preference", DEFAULT_WINE_PREFERENCE)
    cocktail_pref = get_input("Cocktail preference", DEFAULT_COCKTAIL_PREFERENCE)
    consumption_rate = get_input("Consumption rate", DEFAULT_CONSUMPTION_RATE)

    beers, wines, cocktails = calculate_drinks(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate)

    print(f"\nEvent Details:")
    print(f"Number of guests: {guests}")
    print(f"Hours of service: {hours}")
    print(f"\nPreference Settings:")
    print(f"Beer preference: {beer_pref}")
    print(f"Wine preference: {wine_pref}")
    print(f"Cocktail preference: {cocktail_pref}")
    print(f"Consumption rate: {consumption_rate}x average")
    print(f"\nRecommended Drinks:")
    print(f"Beers: {beers}")
    print(f"Wines: {wines}")
    print(f"Cocktails: {cocktails}")

if __name__ == "__main__":
    main()
