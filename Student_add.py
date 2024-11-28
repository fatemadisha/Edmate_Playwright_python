from datetime import datetime


def add_student(page):
    page.goto("https://aceexam-node-front.qa.mpower-social.com/batches?batchName=")

    ## Navigate to students tab
    page.locator("(//button[@aria-label='theme-icon'])[7]").click()
    page.pause()
    
    ## Wait for list to visible
    page.wait_for_selector("//tr[@data-testid='MUIDataTableBodyRow-0']", state="visible", timeout=30000)

    ## WAit until add new student is visible
    page.wait_for_selector("//button[normalize-space()='Add New Student']", state="visible", timeout=10000)

    ## Click Add new student
    page.locator("//button[normalize-space()='Add New Student']").click()

    ## Send values at firstname field
    page.locator("//input[@name='firstName']").fill("Nikto")
 
    ## Send values at lastname field
    page.locator("//input[@name='lastName']").fill("Server Again")

    ## Send values for contact number
    page.locator("//input[@name='contactNo']").fill("012345675")

    ## Send value email field
    page.locator("//input[@name='email']").fill("nikto@gmail.com")

    ## Select date 
    page.locator("//button[@aria-label='Choose date']").click()
    today = datetime.now().strftime("%d")  # Get day as a two-digit number (e.g., '21')

    # Remove leading zero if your calendar uses single-digit days for the first 9 days
    if today.startswith("0"):
        today = today[1:]

    page.locator(f"//button[normalize-space()='{today}']").click()

    ## Select blood group dropdown
    page.locator("//div[.='Blood Group']").click()

    ## wait fpr list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select blood group 
    page.locator("//li[normalize-space()= 'O (+ve)']").click()

    ##Select Division
    page.locator("//div[.='Division']").click()

    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select division
    page.locator("//li[normalize-space()= 'CHITTAGONG']").click()

    ## Select district
    page.locator("//div[.='District']").click()

    ## Select district
    page.locator("//li[normalize-space()= 'BANDARBAN']").click()

    ## Give address
    page.locator("//textarea[@name='address']").fill("346/6, howra")

    ## Open school dropdown
    page.locator("//div[.='School']").click()
 
    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Give school
    page.locator("//li[normalize-space()= 'Aga Khan Academy']").click()

    ## Click gender
    page.locator("//input[@value='female']").click()

    ## Give username
    page.locator("//input[@name='userName']").fill("nikto5")

    ## Give password
    page.fill("//input[@name='password']", "12345678")

    ##Scroll down
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    ## Click Next button
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Next']").click()
    page.wait_for_timeout(10000)

    ##--------------Step 2 --------------------------

    ## Select guardian first Name
    page.locator("//input[@name='guardian[0].relationId.firstName']").fill("Rahim")

    ## Select guardian last name
    page.locator("//input[@name='guardian[0].relationId.lastName']").fill("Sheikh")

    ## Select guardian contact no
    page.locator("//input[@name='guardian[0].relationId.contactNo']").fill("015345678885")

    ##Select guardian email
    page.locator("//input[@name='guardian[0].relationId.email']").fill("guardian@gmail.com")

    ## Select relation with student
    page.locator("//div[.='Relation with student']").click()

    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select father
    page.locator("//li[normalize-space()= 'Father']").click()

    ## Select primary guardian
    page.locator("//input[@name='saveCard']").click()

    ## Select username
    page.locator("//input[@name='guardian[0].relationId.userName']").fill("sheikh")

    ## Select password
    page.locator("//input[@name='password']").fill("12345678")

    ## Scroll to last
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    ## Click next
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Next']").click()
    page.wait_for_timeout(10000)

    ##-------------Step 3---------------

    ## Click next from batch enrollment
    page.locator("//button[normalize-space()='Next']").click()

    ##--------------------Step 4 ---------------------

    ## Review and submit
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Submit']").click()
    page.wait_for_timeout(10000)

    ##Get the message
    message_text = page.text_content("//p[@id='alert-dialog-description']")

    # Validate the message
    assert "User with details created successfully" in message_text, "Confirmation message validation failed"

    print("Confirmation message validated successfully!")

    ##  Close the success message
    page.wait_for_timeout(5000)
    page.locator("//button[@aria-label='Close']").click()

    

    





