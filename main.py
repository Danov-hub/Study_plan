from data import zagruzka_discipline
from sort import binary_sort

def report(disciplines, title):
    print(f"\n{title}")
    print("-" * 100)
    for d in disciplines:
        print(f"{d['name']:<20} | {d['semester']} | {d['time']} | "
              f"{d['hours']} | {d['assessment']:<7} | {d['department']}")
    print()

def report_1(disciplines):
    sort_list = binary_sort(disciplines, key_func=lambda d: (
        d['semester'], d['department'], -d['hours']
    ))
    report(sort_list, "Отчёт 1: Полный список (семестр ↑, кафедра ↑, часы ↓)")

def report_2(disciplines):
    assessment = input("Введите вид отчётности (зачёт/экзамен): ").strip()
    if assessment not in ('зачёт', 'экзамен'):
        print("Допустимы только: зачёт, экзамен \n")
        return

    filtr = [d for d in disciplines if d['assessment'] == assessment]
    if not filtr:
        print("Нет дисциплин с такой отчётностью \n")
        return

    sort_list = binary_sort(filtr, key_func=lambda d: (
        d['time'], -d['hours']
    ))
    report(sort_list, f"Отчёт 2: {assessment} (длительность ↑, часы ↓)")

def report_3(disciplines):
    n1_str = input("Введите N1 (мин. часов): ").strip()
    n2_str = input("Введите N2 (макс. часов): ").strip()
    if not (n1_str.isdigit() and n2_str.isdigit()):
        print("Введите целые неотрицательные числа \n")
        return

    n1, n2 = int(n1_str), int(n2_str)
    if n1 > n2:
        print("N1 должно быть ≤ N2 \n")
        return

    filtr = [d for d in disciplines if n1 <= d['hours'] <= n2]
    if not filtr:
        print("Нет дисциплин в этом диапазоне часов \n")
        return

    sort_list = binary_sort(filtr, key_func=lambda d: (
        d['department'], -d['hours']
    ))
    report(sort_list, f"Отчёт 3: часы от {n1} до {n2} (кафедра ↑, часы ↓)")

def main():
    filename = "disciplines.txt"
    disciplines = zagruzka_discipline(filename)

    if not disciplines:
        print("Данные не загружены")
        return

    print(f"Учебный план загружен. Дисциплин: {len(disciplines)}")
    while True:
        print("\n" + "="*50)
        print("МЕНЮ")
        print("1. Полный список дисциплин")
        print("2. Дисциплины по виду отчётности")
        print("3. Дисциплины по диапазону часов")
        print("4. Выход")
        choice = input("Выберите пункт (1–4): ").strip()
        if choice == '1':
            report_1(disciplines)
        elif choice == '2':
            report_2(disciplines)
        elif choice == '3':
            report_3(disciplines)
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("\nВведите число от 1 до 4!")

if __name__ == "__main__":
    main()
