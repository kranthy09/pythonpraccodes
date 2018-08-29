students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
first = secnd = 0
for name, grade in students:
    if grade > first:
        secnd = first
        first = grade
    elif grade > secnd and grade < first:
        secnd = grade
        print(name)