# Hospital Patient Record Explorer

A beginner-friendly Python project that uses NumPy indexing, slicing, and conditional selection to explore a small hospital patient dataset.

> Note: All records are fictional and created for programming practice only. The thresholds in this project are simplified examples, not medical advice or diagnostic rules.

## Learning objectives

By completing this project, you will practise how to:

- Access individual elements in a NumPy array.
- Use positive and negative indexing.
- Retrieve rows and columns.
- Slice a range of rows.
- Select multiple columns.
- Filter rows using conditions.
- Combine conditions to find records that match more than one requirement.

## Dataset

The NumPy array contains 15 fictional patient records and six columns:

| Column index | Column | Description |
| ---: | --- | --- |
| 0 | Patient ID | Unique sample identifier |
| 1 | Age | Patient age |
| 2 | Blood Pressure | Sample blood pressure value |
| 3 | Sugar Level | Sample sugar level |
| 4 | Heart Rate | Sample heart rate |
| 5 | BMI | Sample body mass index |

Each row represents one patient. Each column represents one field.

## Requirements

- Python 3
- NumPy

## Installation and setup

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install NumPy:

   ```bash
   pip install numpy
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## Project structure

```text
hospital-patient-explorer/
├── main.py
└── README.md
```

## Concepts demonstrated

### 1. Positive indexing

```python
patients[0]
```

Returns the first patient row. Python indexing starts at `0`.

### 2. Negative indexing

```python
patients[-1]
```

Returns the last patient row. The index `-1` means the last item.

### 3. Access one value

```python
patients[0, 1]
```

Returns the value in the first row and second column: the first patient's age.

The general pattern is:

```python
array[row_index, column_index]
```

### 4. Select a column

```python
patients[:, 2]
```

The colon `:` means all rows. Column index `2` is Blood Pressure, so this expression returns every patient's blood pressure value.

### 5. Select multiple columns

```python
patients[:, [1, 5]]
```

Returns the Age and BMI columns for all patients.

### 6. Slice rows

```python
patients[4:15]
```

Selects row indices `4` through `14`. Because the stop index is excluded, this returns patient positions 5 through 15.

### 7. Filter by a condition

```python
patients[patients[:, 1] > 60]
```

Returns complete rows for patients whose age is greater than 60.

### 8. Combine two conditions

```python
patients[
    (patients[:, 2] >= 140) &
    (patients[:, 3] >= 140)
]
```

Returns rows where both the blood pressure value is at least 140 and the sugar level is at least 140. Parentheses around each condition are important when using `&`.

## Tasks covered

- Display the first and last patient.
- Display all blood pressure values.
- Display only Age and BMI.
- Retrieve patients 5 to 15.
- Find patients with blood pressure values at least 140.
- Extract senior citizens (Age > 60).
- **Bonus:** Find patients with both blood pressure and sugar values at least 140.

## Important NumPy reminder

The most important pattern in this project is:

```python
patients[rows, columns]
```

- `:` selects all rows or columns.
- A number selects one index.
- `start:stop` selects a slice; `stop` is excluded.
- A list such as `[1, 5]` selects multiple indices.
- A Boolean condition selects rows that match the condition.

## Future improvements

- Allow users to enter patient values from the keyboard.
- Add a menu so users can choose which analysis to run.
- Load records from a CSV file using NumPy.
- Add input validation and more descriptive output.

## Disclaimer

This is an educational NumPy exercise using fictional data. It is not intended for real patient records, clinical decisions, or medical diagnosis.
