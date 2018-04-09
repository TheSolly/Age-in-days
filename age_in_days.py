# Given your birthday and the current date, this function
# calculate your age in days. Account for leap days.


notleap = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def yearis(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def isleap(year):
    if yearis(year):
        return leap
    else:
        return notleap


# determining the days from your birthday to the end of the year you were born on.
def daysoldbirthday(year1, month1, day1, year2, month2, day2):
    if year1 == year2:
        return 0
    elif month1 == 12:
        daysoldbirthday = day1
    else:
        if isleap(year1) == notleap:
            daysoldbirthday = sum(notleap[month1 + 1:]) + (notleap[month1] - day1)
        else:
            daysoldbirthday = sum(leap[month1 + 1:]) + (leap[month1] - day1)
    return daysoldbirthday


# determining the days of the current year till your birthday.
def daysoldthisyear(year1, month1, day1, year2, month2, day2):
    if year1 == year2:
        daysoldthisyear = (leap[month1] - day1) + sum(leap[month1 + 1:month2]) + day2
    else:
        if isleap(year2) == notleap:
            daysoldthisyear = (sum(notleap[:month2]) + day2)
        else:
            daysoldthisyear = (sum(leap[:month2]) + day2)
    return daysoldthisyear


def daysofyears(year1, year2):
    counter = year1 + 1
    daysofyears = 0
    while counter < year2:
        if isleap(counter) == leap:
            daysofyears = daysofyears + sum(leap)
            counter += 1
        elif isleap(counter) == notleap:
            daysofyears = daysofyears + sum(notleap)
            counter += 1
    return daysofyears


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days1 = daysoldbirthday(year1, month1, day1, year2, month2, day2)
    days2 = daysoldthisyear(year1, month1, day1, year2, month2, day2)
    days3 = daysofyears(year1, year2)
    daysBetweenDates = days1 + days2 + days3
    return daysBetweenDates

    # Test routine


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
