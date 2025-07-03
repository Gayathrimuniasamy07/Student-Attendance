# attendance_backend.py

# A simple list to store student names
attendance_list = []

# Function to mark attendance
def mark_attendance(name):
    attendance_list.append(name)
    print(f"{name} is marked present.")

# Example call
mark_attendance("Gayathri")
