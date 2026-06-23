students = {}

def add_students():
    name = input("Enter Student Name: ")
    if name in students:
        print(f"{name} already added")
    else:
        students[name] = []
        print(f"{name} added!")


def add_grades():
    name = input("Enter Student Name: ")
    if name not in students:
        print("Not found")
        return
    grade = int(input("Enter grade: "))
    if grade < 0 or grade > 100:
        print("Wrong grade")
    else:
        students[name].append(grade)
        print(f"{name}'s grade added")


def get_average(grades):

    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)



def show_students():

    for name, grades in students.items():
        avg = get_average(grades)
        if avg == None:
            print(f"{name} → {grades} → Միջին: N/A")
        else:
            print(f"{name} → {grades} → Միջին: {round(avg,1)}")



def statistics():

    quantity = len(students)
    all_grades = []
    without_grades = 0
    best_grades = 0

    for name, grades in students.items():

        if len(grades) == 0:
            without_grades += 1
        else:
            avg = get_average(grades)
            if avg > 90:
                best_grades += 1

            all_grades += grades

    if len(all_grades) > 0:
        total_avg = sum(all_grades) / len(all_grades)
    else:
        total_avg = 0
    print("Students:", quantity)
    print("Total average grades:", round(total_avg,1))
    print("Students without grades:", without_grades)
    print("Best Students:", best_grades)


def best_students():

    max_avg = 0
    best = []

    for name, grades in students.items():
        avg = get_average(grades)

        if avg != None:
            if avg > max_avg:
                max_avg = avg
                best = [name]
            elif avg == max_avg:
                best.append(name)

    if len(best) == 0:
        print("Not found best students:")
    else:
        print("Best Students:")
        for student in best:
            print(student, "average", round(max_avg,1))


def delete_students():
    name = input("Enter student name: ")
    if name in students:
        del students[name]
        print(f"{name} deleted")
    else:
        print("Not found student name")


def delete_grade():
    name = input("Enter student name: ")

    if name not in students:
        print("Not found student name")
        return

    if len(students[name]) == 0:
        print(f"{name} doesn't have grades")
        return

    print(students[name])
    grade = int(input("Choose grade to delete: "))
    if grade in students[name]:
        students[name].remove(grade)
        print("Grade deleted")
    else:
        print("Not found grades")


def sort_students():

    result = []

    for name, grades in students.items():
        avg = get_average(grades)
        result.append((name, avg))

    result.sort(

        key=lambda x: x[1] if x[1] != None else -1,
        reverse=True

    )

    for index, item in enumerate(result, start=1):

        if item[1] == None:
            print(index, item[0], "→ Avg N/A")
        else:
            print(index, item[0], "→ Avg", round(item[1],1))

def search_low_average():
    value = float(input("Min avg: "))
    for name, grades in students.items():
        avg = get_average(grades)

        if avg == None or avg < value:
            print(
                name,
                "→ Avg",
                "N/A" if avg == None else round(avg,1)
            )


while True:

    print("""
1 — Ավելացնել ուսանող
2 — Ավելացնել գնահատական
3 — Ցույց տալ բոլոր ուսանողներին
4 — Ցույց տալ վիճակագրությունը
5 — Նշել լավագույն ուսանողին
6 — Ջնջել ուսանող
7 — Ջնջել գնահատական
8 — Սորտավորել ուսանողներին ըստ միջինի
9 — Փնտրել միջինը ցածր ուսանողներ
0 — Ելք
""")


    choice = input("Choose: ")

    if choice == "1":
        add_students()
    elif choice == "2":
        add_grades()
    elif choice == "3":
        show_students()
    elif choice == "4":
        statistics()
    elif choice == "5":
        best_students()
    elif choice == "6":
        delete_students()
    elif choice == "7":
        delete_grade()
    elif choice == "8":
        sort_students()
    elif choice == "9":
        search_low_average()
    elif choice == "0":
        print("Menu break")
        break
    else:
        print("Wrong choice")