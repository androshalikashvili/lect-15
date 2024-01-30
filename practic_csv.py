import csv
import os


head = ["id", "name", "age", "grade", "subject_name", "marks"]

csv_data = [
    {'id': '1', 'name': 'Alice', 'age': '18', 'grade': 'A', 'subject_name': 'Math', 'marks': '100'},
    {'id': '2', 'name': 'Bob', 'age': '19', 'grade': 'A', 'subject_name': 'History', 'marks': '85'},
    {'id': '1', 'name': 'Alice', 'age': '18', 'grade': 'A', 'subject_name': 'History', 'marks': '95'},
    {'id': '2', 'name': 'Bob', 'age': '19', 'grade': 'A', 'subject_name': 'Science', 'marks': '90'},
    {'id': '1', 'name': 'Alice', 'age': '18', 'grade': 'A', 'subject_name': 'Science', 'marks': '88'},
    {'id': '2', 'name': 'Bob', 'age': '19', 'grade': 'A', 'subject_name': 'Biology', 'marks': '85'},
    {'id': '1', 'name': ' Alice', 'age': ' 18', 'grade': ' A', 'subject_name': ' Biology', 'marks': ' 90'},
    {'id': '2', 'name': ' Bob', 'age': ' 17', 'grade': ' B', 'subject_name': ' English', 'marks': ' 85'},
    {'id': '3', 'name': ' Charlie', 'age': ' 19', 'grade': ' A', 'subject_name': ' Science', 'marks': ' 92'},
    {'id': '4', 'name': ' David', 'age': ' 16', 'grade': ' C', 'subject_name': ' History', 'marks': ' 78'},
    {'id': '5', 'name': ' Eva', 'age': ' 18', 'grade': ' B', 'subject_name': ' Art', 'marks': ' 88'},
    {'id': '6', 'name': ' Frank', 'age': ' 17', 'grade': ' A', 'subject_name': ' Physics', 'marks': ' 95'},
    {'id': '7', 'name': ' Grace', 'age': ' 16', 'grade': ' B', 'subject_name': ' Chemistry', 'marks': ' 87'},
    {'id': '8', 'name': ' Henry', 'age': '19', 'grade': ' C', 'subject_name': ' Biology', 'marks': ' 75'},
    {'id': '9', 'name': ' Ivy', 'age': ' 18', 'grade': ' A', 'subject_name': ' Geography', 'marks': ' 93'},
    {'id': '10', 'name': ' Jack', 'age': ' 17', 'grade': ' B', 'subject_name': ' Computer Science', 'marks': ' 89'}
    ]


path = "files"
file_name = "csv_data"


def make_new_csv(path, file_name):
    try:
        os.mkdir(path)
    except FileExistsError:
        ...

    file_path = f"{path}/{file_name}.csv"

    try:
        with open(file_path, mode="x", encoding="utf-8"):
            print("CSV File created!\n")
    except FileExistsError:
        print("File with this name Exists")
        print("Continiue writing CODE!...\n")

    return file_path


def write_csv_data(path, data_csv):
    with open(f'{path}/{file_name}.csv', "w", encoding="utf-8", newline="") as file:
        # writer = csv.writer(file)
        # writer.writerow(head)
        # writer.writerows(data_csv)
        writer = csv.DictWriter(file, fieldnames=head)

        writer.writeheader()
        writer.writerows(data_csv)



def reader_csv(path):
    with open(f'{path}/{file_name}.csv', "r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        # reader = list(csv.DictReader(file))
        # print(reader)
        w0 = 5
        w1 = 10
        w2 = 5
        w3 = 10
        w4 = 15
        count = 0
        for row in reader:
            if count == 0:
                print(f"  {row[0]:<{w0}}{row[1]:<{w1}}{row[2]:<{w2}}{row[3]:<{w3}}{row[4]:<{w4}}{row[5]}")
                print("=" * 54)
                count += 1
            else:
                print(f"  {row[0]:<{w0}}{row[1]:<{w1}}{row[2]:<{w2}}{row[3]:<{w3}}{row[4]:<{w4}}{row[5]}")
                print("-" * 54)


# def is_duplicate_id(path, new_id):
#     with open(f'{path}/{file_name}.csv', "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         existing_ids = set(int(row["id"]) for row in reader)
#         return new_id in existing_ids


def append_data(path):
    # while True:
    #     new_id = int(input('Please enter Student ID (only number): '))
    #     if not is_duplicate_id(path, new_id):
    #         break
    #     print("ID already exists. Please choose a different ID.")

    with open(f'{path}/{file_name}.csv', "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=head)

        writer.writerow(
            {
                "id":int(input('Please enter Student ID (only number): ')),
                "name": input('Please input Student Name: '),
                "age": int(input('Please enter Student Age(only number): ')),
                "grade": input('Please enter Student Grade(A, B, C): '),
                "subject_name": input('Please enter Student Subject_Name: '),
                "marks": int(input('Please enter Student Marks(only number): ')),
            }
        )


def choose_student(path):
    filt_id = int(input('Please enter Student ID (only number): '))
    with open(f'{path}/{file_name}.csv', "r", encoding="utf-8") as file:
        # reader = list(csv.reader(file))
        reader = list(csv.DictReader(file))

        w0 = 5
        w1 = 10
        w2 = 5
        w3 = 10
        w4 = 15
        count = 0

        for row in reader:
            if count == 0:
                head = list(row.keys())
                print(f"  {head[0]:<{w0}}{head[1]:<{w1}}{head[2]:<{w2}}{head[3]:<{w3}}{head[4]:<{w4}}{head[5]}")
                print("=" * 54)
                count += 1

            if int(row.get('id')) == filt_id:
                print(f"  {row['id']:<{w0}}{row['name']:<{w1}}{row['age']:<{w2}}{row['grade']:<{w3}}{row['subject_name']:<{w4}}{row['marks']}")
                print("-" * 54)


def edit_marks(path):
    id_edit = int(input('Enter students ID: '))
    sb_name_edit = input('Enter subject_name for edit marks: ')
    new_marks = int(input('Enter new marks: '))

    with open(f'{path}/{file_name}.csv', "r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))

        for row in reader:
            if int(row["id"]) == id_edit and row["subject_name"] == sb_name_edit:
                row["marks"] = new_marks

    with open(f'{path}/{file_name}.csv', "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=head)
        writer.writeheader()
        # writer.writerow(head)
        writer.writerows(reader)

    print(f"Marks for student with ID {id_edit} and subject_name {sb_name_edit} updated to {new_marks}")


# ===============> RUN MAIN <===================#

# make_new_csv(path, file_name)

# write_csv_data(path, csv_data)

# append_data(path)
    
# choose_student(path)

# edit_marks(path)

# reader_csv(path)
