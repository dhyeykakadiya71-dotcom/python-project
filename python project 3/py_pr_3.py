print("=========================================")
print("  Welcome to the Student Data Organizer! ")
print("=========================================")

students_list = []
all_subjects_set = set()

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("\nEnter student details:")
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects_input = input("Subjects (comma-separated): ")
        subjects_list = [s.strip() for s in subjects_input.split(",") if s.strip()]
        immutable_info = (student_id, dob)
        for sub in subjects_list:
            all_subjects_set.add(sub)
        student_dict = {
            "id_dob": immutable_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects_list
        }
        students_list.append(student_dict)
        print("\nStudent added successfully!")

    elif choice == "2":
        print("\n--- Display All Students ---")
        if not students_list:
            print("No student records found.")
        else:
            for student in students_list:
                sid, dob = student["id_dob"]
                sub_str = ", ".join(student["subjects"])
                print(f"Student ID: {sid} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {sub_str}")

    elif choice == "3":
        print("\n--- Update Student Information ---")
        if not students_list:
            print("No records available to update.")
            continue
            
        search_id = int(input("Enter Student ID to update: "))
        found = False
        
        for student in students_list:
            if student["id_dob"][0] == search_id:
                found = True
                print(f"Updating record for {student['name']}.")
                print("Leave field blank to keep current value.")
                
                new_age = input(f"New Age (current: {student['age']}): ").strip()
                if new_age:
                    student["age"] = int(new_age)
                    
                new_grade = input(f"New Grade (current: {student['grade']}): ").strip()
                if new_grade:
                    student["grade"] = new_grade
                    
                new_subs = input("New Subjects (comma-separated, leave blank to keep current): ").strip()
                if new_subs:
                    student["subjects"] = [s.strip() for s in new_subs.split(",") if s.strip()]
                    for sub in student["subjects"]:
                        all_subjects_set.add(sub)
                        
                print("Student records updated successfully.")
                break
        
        if not found:
            print("Student ID not found.")

    elif choice == "4":
        print("\n--- Delete Student ---")
        if not students_list:
            print("No records available to delete.")
            continue
            
        search_id = int(input("Enter Student ID to delete: "))
        found_index = -1
        
        for i, student in enumerate(students_list):
            if student["id_dob"][0] == search_id:
                found_index = i
                break
        
        if found_index != -1:
            target_name = students_list[found_index]["name"]
            del students_list[found_index]
            print(f"Student '{target_name}' has been successfully removed.")
            all_subjects_set.clear()
            for s in students_list:
                for sub in s["subjects"]:
                    all_subjects_set.add(sub)
        else:
            print("Student ID not found.")

    elif choice == "5":
        print("\n--- Display Subjects Offered ---")
        if not all_subjects_set:
            print("No subjects are currently being offered.")
        else:
            print("Unique subjects offered to students (No Duplicates):")
            for idx, subject in enumerate(all_subjects_set, start=1):
                print(f"{idx}. {subject}")

    elif choice == "6":
        print("\n=========================================")
        print("Thank you for using Student Data Organizer!")
        print("Exiting application... Goodbye!")
        print("=========================================")
        break
        
    else:
        print("Invalid option chosen. Please select between 1 and 6.")
