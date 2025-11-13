# gradebook.py
# Author: [Hitarth Kumar Srivastava]
# Roll Number : [2501730430]
# Date: [11-11-2025]
# Project: GradeBook Analyzer CLI
# Course: Programming for Problem Solving Using Python (ETCCPP102)
# Faculty: Ms. Neha Kaushik
# College: K.R. Mangalam University

import csv

def calculate_average(marks_dict):
    total = 0
    count = 0
    for v in marks_dict.values():
        total += v
        count += 1
    return total / count if count > 0 else 0

def calculate_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2

def find_max_score(marks_dict):
    it = iter(marks_dict.values())
    try:
        current_max = next(it)
    except StopIteration:
        return None
    for v in it:
        if v > current_max:
            current_max = v
    return current_max

def find_min_score(marks_dict):
    it = iter(marks_dict.values())
    try:
        current_min = next(it)
    except StopIteration:
        return None
    for v in it:
        if v < current_min:
            current_min = v
    return current_min

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    dist = {'A':0,'B':0,'C':0,'D':0,'F':0}
    for g in grades.values():
        if g in dist:
            dist[g] += 1
    return dist

def input_marks():
    marks = {}
    try:
        n = int(input("Enter number of students: ").strip())
    except ValueError:
        print("Invalid number. Returning to menu.")
        return marks
    for _ in range(n):
        name = input("Enter student name: ").strip()
        try:
            mark = float(input(f"Enter marks for {name}: ").strip())
        except ValueError:
            print("Invalid mark. Setting mark to 0 for this student.")
            mark = 0.0
        marks[name] = mark
    return marks

def load_from_csv(filename):
    marks = {}
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if len(row) < 2:
                    continue
                name = row[0].strip()
                try:
                    mark = float(row[1])
                except ValueError:
                    mark = 0.0
                marks[name] = mark
        print("CSV file loaded successfully.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print("Error loading CSV:", e)
    return marks

def print_summary(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name in marks:
        print(f"{name:<12}\t{marks[name]:<7}\t{grades[name]}")
    print("---------------------------------")
    avg = calculate_average(marks)
    med = calculate_median(marks)
    hi = find_max_score(marks)
    lo = find_min_score(marks)
    print(f"Average: {avg:.2f}")
    print(f"Median: {med:.2f}")
    if hi is not None:
        print(f"Highest: {hi:.2f}")
    if lo is not None:
        print(f"Lowest: {lo:.2f}")

def export_to_csv(marks, grades):
    filename = "grades_report.csv"
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Marks", "Grade"])
            for name in marks:
                writer.writerow([name, f"{marks[name]:.2f}", grades[name]])
        print(f"Grades exported successfully to {filename}")
    except Exception as e:
        print("Error exporting CSV:", e)

def main():
    print("===================================")
    print("       GradeBook Analyzer CLI      ")
    print("===================================")
    print("Author: Vaibhav Kumar    Roll No.: 2501730427    Date: 12-11-2025")

    while True:
        print("\nMenu:")
        print("1. Manual Input")
        print("2. Import from CSV")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            marks = input_marks()
        elif choice == "2":
            filename = input("Enter CSV file name (e.g., marks.csv): ").strip()
            marks = load_from_csv(filename)
        elif choice == "3":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid option. Try again.")
            continue

        if not marks:
            print("No data found.")
            continue

        grades = assign_grades(marks)
        print_summary(marks, grades)

        passed_students = [n for n, m in marks.items() if m >= 40]
        failed_students = [n for n, m in marks.items() if m < 40]

        print("\nPassed Students:", passed_students)
        print("Failed Students:", failed_students)

        dist = grade_distribution(grades)
        print("\nGrade Distribution:", dist)

        export = input("\nDo you want to export grade report to CSV? (yes/no): ").strip().lower()
        if export == "yes":
            export_to_csv(marks, grades)

        again = input("\nRun analysis again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using GradeBook Analyzer.")
            break

if __name__ == "__main__":
    main()
