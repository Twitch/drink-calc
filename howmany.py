#!/usr/bin/env python3
import argparse
import math

# Easily adjustable variables
BEER_PREFERENCE = 1.0
WINE_PREFERENCE = 1.0
COCKTAIL_PREFERENCE = 1.0
CONSUMPTION_RATE = 1.0  # 1.0 is average, >1.0 for heavier drinking, <1.0 for lighter drinking

# Standard drink calculations
DRINKS_PER_PERSON_PER_HOUR = 1
BEER_PERCENTAGE = 0.4
WINE_PERCENTAGE = 0.3
COCKTAIL_PERCENTAGE = 0.3

def calculate_drinks(guests, hours):
    total_drinks = guests * hours * DRINKS_PER_PERSON_PER_HOUR * CONSUMPTION_RATE
    
    # Calculate preference weights
    total_preference = BEER_PREFERENCE + WINE_PREFERENCE + COCKTAIL_PREFERENCE
    beer_weight = BEER_PREFERENCE / total_preference
    wine_weight = WINE_PREFERENCE / total_preference
    cocktail_weight = COCKTAIL_PREFERENCE / total_preference
    
    # Calculate drinks by type
    beers = math.ceil(total_drinks * beer_weight * BEER_PERCENTAGE)
    wines = math.ceil(total_drinks * wine_weight * WINE_PERCENTAGE)
    cocktails = math.ceil(total_drinks * cocktail_weight * COCKTAIL_PERCENTAGE)
    
    return beers, wines, cocktails

def main():
    parser = argparse.ArgumentParser(description="Calculate drinks for an open bar event.")
    parser.add_argument("guests", type=int, help="Number of guests")
    parser.add_argument("hours", type=int, help="Hours of service")
    args = parser.parse_args()

    beers, wines, cocktails = calculate_drinks(args.guests, args.hours)

    print(f"\nEvent Details:")
    print(f"Number of guests: {args.guests}")
    print(f"Hours of service: {args.hours}")
    print(f"\nPreference Settings:")
    print(f"Beer preference: {BEER_PREFERENCE}")
    print(f"Wine preference: {WINE_PREFERENCE}")
    print(f"Cocktail preference: {COCKTAIL_PREFERENCE}")
    print(f"Consumption rate: {CONSUMPTION_RATE}x average")
    print(f"\nRecommended Drinks:")
    print(f"Beers: {beers}")
    print(f"Wines: {wines}")
    print(f"Cocktails: {cocktails}")

if __name__ == "__main__":
    main()
