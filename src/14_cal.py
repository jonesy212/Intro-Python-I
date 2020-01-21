"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# today = datetime.datetime.today() datem(today.year, today.month.1 )
# datem = datetime.today().strftimes("Y-%m")
# datem = datetime.strptime(datem, "Y-%m")


year = input("Current year: ")
month = input("Current month: ")

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

# currentCalendar = datetime.now().isocalendar

if currentDay == "" and currentMonth == "" and currentYear == "":
  print(int(datetime.now().day))
  print(int(datetime.now().month))
  print(int(datetime.now().year))
else:
  print(int(()))
 

 today str (datetime.date.today()):

 currentYear =int(today[:4])
 currentMonth =int(today[5:7])
