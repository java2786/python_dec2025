""" 
name, subject-score, sub-score, avg

3 std

topper
"""


# std1 = {"name":"Ramesh", "subjects":{"Math":87,"Eng":72,"Phy":89}, "avg": 0, "total": 0}
# std2 = {"name":"Mahesh", "subjects":{"math":83,"eng":76,"Phy":78}, "avg": 0, "total": 0}


students = [
    {"name":"Ramesh", "subjects":{"Math":87,"Eng":72,"Phy":89}, "avg": 0, "total": 0},
    {"name":"Mahesh", "subjects":{"Math":83,"Eng":76,"Phy":78, "Hindi": 92}, "avg": 0, "total": 0}
]

print("=========== Class Report Card ===========")
for i in range(len(students)):
    print(f'{i+1}\tName\t{students[i]["name"]}')
    print("\tSubjects")
    for key in students[i]["subjects"].keys():
        print(f'\t\t{key} -> {students[i]["subjects"][key]}')
        students[i]["total"] = students[i]["total"] + students[i]["subjects"][key]
    print(f"Total\t{students[i]['total']}")
    print("===================")