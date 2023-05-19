# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
import math

centuries = float(input())
years = centuries * 100
days = years * 365.2422
hours = math.floor(days) * 24
minutes = hours * 60
print(f"{centuries:.0f} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
