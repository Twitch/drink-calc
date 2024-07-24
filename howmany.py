#!/usr/bin/env python3

import argparse
import math
import signal
import sys

# Default values for preferences and consumption rate
DEFAULT_GUESTS = 100
DEFAULT_HOURS = 4
DEFAULT_BEER_PREFERENCE = 1.0
DEFAULT_WINE_PREFERENCE = 1.0
DEFAULT_COCKTAIL_PREFERENCE = 1.0
DEFAULT_CONSUMPTION_RATE = 1.0  # 1.0 is average, >1.0 for heavier drinking, <1.0 for lighter drinking

# Standard drink calculations
DRINKS_PER_PERSON_PER_HOUR = 1

def signal_handler(sig, frame):
    print("\n\nProcess interrupted. Exiting gracefully.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_input(prompt, default, input_type=float):
    user_input = input(f"{prompt} (default {default}): ")
    return input_type(user_input) if user_input else default

def calculate_drinks(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate):
    total_drinks = math.ceil(guests * hours * DRINKS_PER_PERSON_PER_HOUR * consumption_rate)
    
    # Calculate preference weights
    total_preference = beer_pref + wine_pref + cocktail_pref
    beer_weight = beer_pref / total_preference
    wine_weight = wine_pref / total_preference
    cocktail_weight = cocktail_pref / total_preference
    
    # Calculate drinks by type
    beers = math.ceil(total_drinks * beer_weight)
    wines = math.ceil(total_drinks * wine_weight)
    cocktails = math.ceil(total_drinks * cocktail_weight)
    
    # Recalculate total drinks as sum of individual drink types
    actual_total = beers + wines + cocktails
    
    return beers, wines, cocktails, actual_total

def print_decorated_output(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate, beers, wines, cocktails, total_drinks):
    line_length = 40
    print("\n" + "=" * line_length)
    print("🎉 Open Bar Drink Calculator 🎉".center(line_length))
    print("=" * line_length)
    print(f"\nEvent Details:".center(line_length))
    print(f"Number of guests: {guests}".center(line_length))
    print(f"Hours of service: {hours}".center(line_length))
    print(f"\nPreference Settings:".center(line_length))
    print(f"Beer preference: {beer_pref}".center(line_length))
    print(f"Wine preference: {wine_pref}".center(line_length))
    print(f"Cocktail preference: {cocktail_pref}".center(line_length))
    print(f"Consumption rate: {consumption_rate}x average".center(line_length))
    print(f"\nRecommended Drinks:".center(line_length))
    print(f"🍺 Beers: {beers}".center(line_length))
    print(f"🍷 Wines: {wines}".center(line_length))
    print(f"🍸 Cocktails: {cocktails}".center(line_length))
    print(f"\nTotal Drinks: {total_drinks}".center(line_length))
    print("=" * line_length)
    print("Cheers! 🥂".center(line_length))
    print("=" * line_length)

def main():
    parser = argparse.ArgumentParser(description="Calculate drinks for an open bar event.")
    parser.add_argument("guests", nargs="?", type=int, help="Number of guests")
    parser.add_argument("hours", nargs="?", type=int, help="Hours of service")
    parser.add_argument("-g", "--guests", type=int, dest="guests_switch", help="Number of guests")
    parser.add_argument("-H", "--hours", type=int, dest="hours_switch", help="Hours of service")
    args = parser.parse_args()

    print("Welcome to the Open Bar Calculator!")

    guests = args.guests or args.guests_switch or get_input("Number of guests", DEFAULT_GUESTS, int)
    hours = args.hours or args.hours_switch or get_input("Hours of service", DEFAULT_HOURS, int)
    beer_pref = get_input("Beer preference", DEFAULT_BEER_PREFERENCE)
    wine_pref = get_input("Wine preference", DEFAULT_WINE_PREFERENCE)
    cocktail_pref = get_input("Cocktail preference", DEFAULT_COCKTAIL_PREFERENCE)
    consumption_rate = get_input("Consumption rate", DEFAULT_CONSUMPTION_RATE)

    beers, wines, cocktails, total_drinks = calculate_drinks(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate)

    print_decorated_output(guests, hours, beer_pref, wine_pref, cocktail_pref, consumption_rate, beers, wines, cocktails, total_drinks)

if __name__ == "__main__":
    main()
