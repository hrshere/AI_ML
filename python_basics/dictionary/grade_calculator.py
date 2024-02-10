'''program to create grade calculator'''
def main():
    jack = {
            "name": "Jack Frost",
            "assignment": [80,50,40,20],
            "test": [75, 75],
            "lab": [78.20, 77.20]
            }
    score = calculate_total_average(jack)
    print(score)
    print(assign_grade_letter(score))

def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])
    return (0.1 * assignment + 0.7 * test + 0.2 * lab)

def assign_grade_letter(score):
    if score >= 90:
        print("A")
    elif 90> score >= 80:
        print("B")
    elif 80>score >= 70:
        print("C")
    elif 70 > score >= 60:
        print("D")
    else:
        print("E")

if __name__ == "__main__":
    main()