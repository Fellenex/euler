"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeapYear(n):
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0: return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)

#December occurs at the beginning.
daysPerMonth = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
daysPerMonthLeapYear = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

#0-index Sundays, meaning Monday is 1
startingDay = 1

#First figure out what the first day of the week of 1901 is,
#   by calculating from 1900 (which is not a leap year)
for monthDays in daysPerMonth[1:]:
    startingDay = (startingDay + monthDays) % 7
#    print(startingDay)

#Now startingDay is the first day of 1901
print("First day of Dec 1900 is: "+str(startingDay))

#Calculate the first day of each month for years 1901-2000, taking into account leap years.
firstOfMonthSundays = 0
for i in range(1901,2001):
    if isLeapYear(i):
        for monthDays in daysPerMonthLeapYear:
            startingDay = (startingDay + monthDays) % 7
            if startingDay == 0:
                firstOfMonthSundays += 1

    else:
        for monthDays in daysPerMonth:
            startingDay = (startingDay + monthDays) % 7
            print(startingDay)
            if startingDay == 0:
                firstOfMonthSundays += 1

print(firstOfMonthSundays)
