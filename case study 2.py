patient_name = input("Enter patient name: ")
requested = [x.strip() for x in input("Enter requested departments: ").split(",")]
available = [x.strip() for x in input("Enter available departments: ").split(",")]
visited = [x.strip() for x in input("Enter previously visited departments: ").split(",")]
preferred_doctors = [x.strip() for x in input("Enter preferred doctors: ").split(",")]
available_doctors = [x.strip() for x in input("Enter available doctors: ").split(",")]
emergency = [x.strip() for x in input("Enter emergency departments: ").split(",")]
req_set = set(requested)
avail_set = set(available)
visited_set = set(visited)
emergency_set = set(emergency)
available_depts = list(req_set & avail_set)
unavailable_depts = list(req_set - avail_set)
visited_before = list(req_set & visited_set)
urgent_depts = list(req_set & emergency_set)
duplicates = []
for dept in requested:
    if requested.count(dept) > 1 and dept not in duplicates:
        duplicates.append(dept)
doctor_match = list(set(preferred_doctors) & set(available_doctors))

first_department = requested[0] if requested else "None"
department_slice = requested[:2]
if urgent_depts:
    recommended = urgent_depts[0]
    status = "Immediate Attention Required"
elif available_depts:
    recommended = available_depts[0]
    if doctor_match:
        status = "Appointment Confirmed"
    else:
        status = "Department Available, Doctor Unavailable"
else:
    recommended = "None"
    status = "Appointment Not Available"
if recommended in avail_set:
    recommendation = "Recommended department is available"
else:
    recommendation = "Recommended department is unavailable"
all_departments = list(req_set | avail_set)
print("\n===== APPOINTMENT REPORT =====")
print("Patient Name          :", patient_name)
print("Requested Departments :", requested)
print("Available Departments :", available_depts)
print("Unavailable           :", unavailable_depts)
print("Previously Visited    :", visited_before)
print("Emergency Departments :", urgent_depts)
print("Duplicate Requests    :", duplicates)
print("Matching Doctors      :", doctor_match)
print("Recommended           :", recommended)
print("Status                :", status)
print("All Unique Departments:", all_departments)
