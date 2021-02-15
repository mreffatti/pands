student = {"name":"Mary", "modules":[{"coursename" : "Programing", "grade" : 45}, {"coursename" : "History", "grade" : 99}] }


print(f"Student: {student['name']}")

for module in student['modules']:
    print(f"\t {module['coursename']} \t: {module['grade']}")