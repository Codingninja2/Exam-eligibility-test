# Take input for the student to check if they can attend the exam or not
medical_cause = input("Did you have a medical cause (Y or N): ")

# Take input for attendance
atten = int(input("Enter the attendance of the student: "))

# Checking the user input and predicting the output accordingly
if medical_cause == 'Y':  # Checking condition 1
    print("You are allowed")
else:
    if atten >= 75:  # Checking condition 2
        print("Allowed")
    else:
        print("Not allowed")
