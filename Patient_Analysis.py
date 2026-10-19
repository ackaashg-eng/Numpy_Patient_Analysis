import numpy as np

# Hospital Patient Record Explorer

# 1. Column names (the order matches the values in each row)
columns = [
    "Patient ID",
    "Age",
    "Blood Pressure",
    "Sugar Level",
    "Heart Rate",
    "BMI",
]

# 2. Create a 2D NumPy array.
# Each row represents one patient.
# Each column represents one measurement or identifier.
patients = np.array([
    [1001, 45, 120,  95, 72, 23],
    [1002, 67, 145, 160, 85, 28],
    [1003, 32, 118,  88, 68, 22],
    [1004, 72, 155, 180, 90, 31],
    [1005, 58, 135, 110, 76, 26],
    [1006, 25, 110,  90, 65, 21],
    [1007, 63, 142, 150, 82, 29],
    [1008, 50, 128, 105, 74, 24],
    [1009, 70, 160, 190, 95, 33],
    [1010, 39, 122,  98, 70, 25],
    [1011, 61, 140, 145, 80, 27],
    [1012, 29, 115,  85, 66, 20],
    [1013, 55, 132, 125, 78, 26],
    [1014, 66, 150, 170, 88, 30],
    [1015, 41, 125, 100, 73, 24],
], dtype=int)


def display_records(title, data, headings=columns):
    """Print a title, column headings, and the selected records."""
    print(f"\n--- {title} ---")
    print(headings)
    print(data)


def main():
    # Display the full dataset
    display_records("HOSPITAL PATIENT RECORDS", patients)
    print("\nDataset shape (rows, columns):", patients.shape)
    print("Number of patients:", patients.shape[0])
    print("Number of columns:", patients.shape[1])

    # 3. Positive and negative indexing
    print("\n--- INDEXING ---")
    print("First patient (index 0):", patients[0])
    print("Last patient (index -1):", patients[-1])
    print("Age of the first patient:", patients[0, 1])
    print("BMI of the last patient:", patients[-1, -1])
    print("Blood pressure of the third patient:", patients[2, 2])

    # 4. Display the first and last patient
    display_records("FIRST PATIENT", patients[0])
    display_records("LAST PATIENT", patients[-1])

    # 5. Display every blood pressure value.
    blood_pressure = patients[:, 2]
    print("\n--- ALL BLOOD PRESSURE VALUES ---")
    print(blood_pressure)

    # 6. Select Age (column 1) and BMI (column 5) for every patient.
    age_and_bmi = patients[:, [1, 5]]
    display_records("AGE AND BMI", age_and_bmi, ["Age", "BMI"])

    # 7. Retrieve patient positions 5 through 15.
    selected_patients = patients[4:15]
    display_records("PATIENTS 5 TO 15", selected_patients)

    # 8. Find patients whose blood pressure is at least 140.
    high_bp = patients[patients[:, 2] >= 140]
    display_records("PATIENTS WITH BLOOD PRESSURE >= 140", high_bp)

    # 9. Extract senior citizens whose age is greater than 60.
    seniors = patients[patients[:, 1] > 60]
    display_records("SENIOR CITIZENS (AGE > 60)", seniors)

    # 10. Bonus: blood pressure >= 140 AND sugar level >= 140.
    high_bp_and_sugar = patients[
        (patients[:, 2] >= 140) & (patients[:, 3] >= 140)
    ]
    display_records("HIGH BLOOD PRESSURE AND HIGH SUGAR", high_bp_and_sugar)


if __name__ == "__main__":
    main()
