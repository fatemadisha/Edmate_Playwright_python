import csv

def enroll_student(page, batch_name, student_csv_path):
    
    # Navigate to the batch page
    url_batch = "https://aceexam-node-front.qa.mpower-social.com/batches?batchName="
    page.goto(url_batch)
    page.pause()
    # Navigate to the specified batch
    try:
        page.locator(f"//a[normalize-space()='{batch_name}']").click()
        print(f"Navigated to batch: {batch_name}")
    except Exception as e:
        print(f"Failed to locate batch '{batch_name}'. Error: {e}")
        return

    # Open the student enrollment section
    try:
        page.locator("//button[normalize-space()='Enroll Student']").click()
        print("Opened student enrollment section.")
    except Exception as e:
        print("Failed to open student enrollment section. Error:", e)
        return

     # Read the student list from the CSV file
    with open(student_csv_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for student in csv_reader:
                student_name = student.get('Name', '').strip()
                student_email = student.get('Email', '').strip()
                ##page.pause()

                try:
                    # Search for the student by email
                    page.locator("(//label[normalize-space()='Email'])[1]").fill(student_email)
                    print(f"Searching for student: {student_name} ({student_email})")

                    # Wait for the search results to load
                    search_result = page.locator(f"tr:has(h6:has-text('{student_email}'))")

                    # Locate and click the "Enroll" button for the student
                    enroll_button = search_result.locator("button[aria-label='Enroll']")
                    enroll_button.click()

                    print(f"Enrolled student: {student_name} ({student_email})")
                    

                except Exception as e:
                    print(f"Failed to enroll student {student_name}. Error: {e}")
                    
                    ## Click close button
                    page.locator("//button[normalize-space()='Close']").click()