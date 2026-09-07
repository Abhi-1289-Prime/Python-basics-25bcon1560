class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Create a student object and assign values as in the C code
s1 = Student(name="Rahul", roll=101, marks=87.5)

# Print the student's details
print(f"Name: {s1.name}")
print(f"Roll: {s1.roll}")
print(f"Marks: {s1.marks:.1f}")