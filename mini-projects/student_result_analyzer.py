print("Student Result Analyzer\n")

# ---------- Functions ----------

def total_marks(marks):
    return sum(marks.values())


def average_marks(marks):
    return total_marks(marks) / len(marks)


def pass_fail(marks):
    for score in marks.values():
        if score < 40:
            return "FAIL"
    return "PASS"


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


# ---------- Student Data ----------

students = [
    {
        "roll_no": 1,
        "name": "Aman Sharma",
        "marks": {"Maths": 78, "English": 65, "Science": 82}
    },
    {
        "roll_no": 2,
        "name": "Riya Verma",
        "marks": {"Maths": 92, "English": 88, "Science": 91}
    },
    {
        "roll_no": 3,
        "name": "Kunal Singh",
        "marks": {"Maths": 56, "English": 60, "Science": 58}
    },
    {
        "roll_no": 4,
        "name": "Neha Gupta",
        "marks": {"Maths": 45, "English": 52, "Science": 49}
    },
    {
        "roll_no": 5,
        "name": "Rohit Mehta",
        "marks": {"Maths": 34, "English": 48, "Science": 40}
    },
    {
        "roll_no": 6,
        "name": "Pooja Yadav",
        "marks": {"Maths": 81, "English": 74, "Science": 79}
    },
    {
        "roll_no": 7,
        "name": "Arjun Patel",
        "marks": {"Maths": 67, "English": 72, "Science": 69}
    },
    {
        "roll_no": 8,
        "name": "Simran Kaur",
        "marks": {"Maths": 90, "English": 85, "Science": 88}
    },
    {
        "roll_no": 9,
        "name": "Mohit Jain",
        "marks": {"Maths": 59, "English": 61, "Science": 63}
    },
    {
        "roll_no": 10,
        "name": "Anjali Mishra",
        "marks": {"Maths": 76, "English": 80, "Science": 73}
    },
    {
        "roll_no": 11,
        "name": "Vikas Kumar",
        "marks": {"Maths": 41, "English": 39, "Science": 45}
    },
    {
        "roll_no": 12,
        "name": "Sneha Roy",
        "marks": {"Maths": 88, "English": 90, "Science": 92}
    }
]


# ---------- Result Analysis ----------

for student in students:
    total = total_marks(student["marks"])
    avg = average_marks(student["marks"])
    result = pass_fail(student["marks"])
    grade = calculate_grade(avg)

    print(f"Name       : {student['name']}")
    print(f"Roll No    : {student['roll_no']}")
    print(f"Total      : {total}")
    print(f"Average    : {avg:.2f}")
    print(f"Result     : {result}")
    print(f"Grade      : {grade}")
    
