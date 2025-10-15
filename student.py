# grade_evaluation.py

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "Fail"

def main():
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be greater than 0.")
            return

        marks = []
        for i in range(num_subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print("Marks should be between 0 and 100.")
                return


        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
