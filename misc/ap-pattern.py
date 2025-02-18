
def getHours(start: str, end: str) -> int:
    startHour = int(start[0:2])
    endHour = int(end[0:2])

    if startHour < endHour:
        return endHour - startHour
    elif startHour > endHour:
        return 24 - startHour + endHour
    else:
        return 0

test = getHours("23:00", "05:00")
print("Pass" if test == 6 else "Fail")

test = getHours("23:00", "07:00")
print("Pass" if test == 8 else "Fail")

test = getHours("23:00", "24:00")
print("Pass" if test == 1 else "Fail")

test = getHours("03:00", "04:00")
print("Pass" if test == 1 else "Fail")

test = getHours("20:00", "20:00")
print("Pass" if test == 0 else "Fail")

test = getHours("00:00", "23:00")
print("Pass" if test == 23 else "Fail")
