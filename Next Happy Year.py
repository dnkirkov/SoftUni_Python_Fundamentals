# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct
# digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.

year = int(input())
while 1:
    year += 1
    year_str = str(year)
    set_year = set(year_str)
    if len(set_year) == len(year_str):
        print(year)
        break
