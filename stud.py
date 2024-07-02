def main():
    # Take input from user for number of students
    num_students = int(input("Enter the number of students: "))

    # Initialize an empty list to store tuples of (marks, student_name)
    students = []

    # Take input for each student's name and marks
    for i in range(num_students):
        student_name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks of student {i+1}: "))
        students.append((marks, student_name))

    # Calculate average marks
    total_marks = sum(marks for marks, _ in students)
    average_marks = total_marks / num_students

    # Print average marks
    print(f"Average marks of all students: {average_marks:.2f}")

    # Sort students based on marks in descending order
    students.sort(reverse=True, key=lambda x: x[0])

    # Print students in descending order of marks
    print("\nStudents sorted by marks (descending):")
    for rank, (marks, student_name) in enumerate(students, start=1):
        print(f"{rank}. {student_name}: {marks}")

if __name__ == "__main__":
    main()
