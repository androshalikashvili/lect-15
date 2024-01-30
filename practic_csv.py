import csv
import os


head = ["Name", "Age", "Department", "Salary"]

csv_data = [
    # ["Name", "Age", "Department", "Salary"],
    ["John Doe", 28, "IT", 60000],
    ["Jane Smith", 35, "Marketing", 55000],
    ["Bob Johnson", 22, "HR", 50000],
    ["Alice Brown", 40, "Finance", 65000],
    ["Charlie Davis", 32, "IT", 62000],
    ["Eva Martinez", 28, "Sales", 58000],
]


path = "files"


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
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(head)
        writer.writerows(data_csv)
        # writer.writerow(['jane', '35', '599662244'])


def reader_csv(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        # print(reader)
        w1 = 20
        w2 = 10
        w3 = 15
        count = 0
        for row in reader:
            if count == 0:
                print(f"  {row[0]:<{w1}}{row[1]:<{w2}}{row[2]:<{w3}}{row[3]}")
                print("=" * 54)
                count += 1
            else:
                print(f"  {row[0]:<{w1}}{row[1]:<{w2}}{row[2]:<{w3}}{row[3]}")
                print("-" * 54)


def append_data(file_path):
    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=head)

        # writer.writerow({"Name": "Andro Shalikashvili", "Age": 43, "Department": "IT dep", "Salary": 2500})
        writer.writerow(
            {
                "Name": st_name,
                "Age": st_age,
                "Department": st_place,
                "Salary": st_salary,
            }
        )


# ===============> RUN MAIN <===================#

# file = input('create new file name: ')
make_new_csv(path, "file_11")

# write_csv_data(path, csv_data)

# # მონაცემების დასამატებლად:
# st_name = input('Please input Student Name: ')
# st_age = int(input('Please enter Student Age(only number): '))
# st_place = input('Please enter Student working Departament: ')
# st_salary = int(input('Please enter Student Salary(only number): '))
# append_data(path)


reader_csv(path)
