if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
    grades = sorted(set(students.values()))
    second_lowest = grades[1]
    second_lowest_students = []
    for name, grade in students.items():
        if grade == second_lowest:
            second_lowest_students.append(name)
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
