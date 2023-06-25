class Student:
    pass

class Marks:
    pass

# Create instances
student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()

# Check if instances are of the classes
print(type(student1) is Student)  # True
print(type(student2) is Student)  # True
print(type(marks1) is Marks)      # True
print(type(marks2) is Marks)      # True

# Check if classes are subclasses of object
print(issubclass(Student, object))  # True
print(issubclass(Marks, object))    # True
