def dayOfProgrammer(year: int):
    daysInMonth = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    isLeapYear = False
    # Julian
    # check for leap year
    if year <= 1918:
        if year % 4 == 0:
            isLeapYear = True
    # Gregorian
    # check for leap year
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            isLeapYear = True

    # if leap year
    if isLeapYear:
        daysInMonth[2] = 29
    else:
        daysInMonth[2] = 28

    programmerDay = 0
    currentMonth = 1
    for month in daysInMonth.keys():
        if programmerDay + daysInMonth[month] < 256:
            currentMonth += 1
            programmerDay += daysInMonth[month]
        else:
            break

    programmerDay = 256 - programmerDay
    month = "0" + str(currentMonth) if currentMonth <= 9 else str(currentMonth)

    return f"{programmerDay}.{month}.{year}"


year = 2017
print(dayOfProgrammer(year))
