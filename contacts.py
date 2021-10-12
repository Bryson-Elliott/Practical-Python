contacts = {
    "number":4,
    "students":[
        {"name":"Bryson Elliott", "email":"bryson@example.com"},
        {"name":"Andrew Bean", "email":"AB@exapmle.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])
