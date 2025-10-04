def can_enroll(age):
    """
    Returns True if a student of given age can enroll in class (i.e. age between 10 and 20 inclusive),
    otherwise returns False.
    """
    if age < 10:
        return False
    elif age > 20:
        return False
    else:
        return True

def enroll_student(name, age, roster):
    """
    Try to enroll student with name and age into roster (a list of (name, age)).
    Prints whether enrollment succeeded or failed.
    """
    if can_enroll(age):
        roster.append((name, age))
        print(f"{name} (age {age}) has been enrolled.")
    else:
        print(f"Enrollment failed for {name} (age {age}): age must be between 10 and 20 years.")

# Example usage
roster = []
enroll_student("Alice", 12, roster)
enroll_student("Bob", 9, roster)
enroll_student("Charlie", 21, roster)

print("Final roster:", roster)
