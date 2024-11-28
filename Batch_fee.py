# def add_fee(page, batch_name):

#     page.goto("https://aceexam-node-front.qa.mpower-social.com/batches?batchName=")

#     ## Navigate to the specific batch
#     try:
#         page.locator(f"//a[normalize-space()='{batch_name}']").click()
#         print(f"Navigate to batch: {batch_name}")

#     except Exception as e:
#         print(f"Failed to locate Batch {batch_name}. Error{e}")

#     ##--------------------Add New Fee-------------------------    

    
#     ## Click Billing tab
#     page.locator("#simple-tab-5").click()

#     ## Click "Add new Fee"
#     page.locator("//button[normalize-space()='Add New Fee']").click()

#     ## Give fee title as "Enrollment Fee"
#     page.locator("input[name='feeTitle']").fill("Lab Fee 1")

#     ## Click is recurring
#     page.locator("input[value='true']").click()

#     ## Fill Amount
#     page.locator("input[name='amount']").fill("2000")

#     ## Click payment frequency
#     locator = page.locator("div.MuiFormControl-root:has(label:has-text('Payment Frequency')) input[role='combobox']")
#     locator.click()

#     ## Wait for list to appear
#     page.wait_for_selector("li[role='option']", timeout= 5000)

#     ## Click monthly
#     page.locator("//li[normalize-space()= 'Monthly']").click()

#     ## Click charge Event
#     page.locator("div.MuiFormControl-root:has(label:has-text('Charge Event')) input[role='combobox']").click()

#     ## Wait for list to appear
#     page.wait_for_selector("li[role='option']", timeout= 5000)

#     ## Click "Enrollment"
#     page.locator("//li[normalize-space()= 'Enrollment']").click()

#     ## Click Add
#     page.locator("button[type='submit']").click()

#     ## Get the text
#     Text = page.text_content("div[role='status']")

#     assert "New Fee created successfully" in Text

#     print("Confirmation message validated successfully!")

#     ##----------------Charge Fees---------------------------
    
#     page.pause()
#     page.wait_for_timeout(3000)

#     ## Click charge fees
#     page.locator("//button[normalize-space()='Charge Fees']").click()

#     ## Click Fees
#     locator = page.locator("div.MuiFormControl-root:has(label:has-text('Fees')) input[role = 'combobox']")
#     locator.click()

#     ## wait for list to appear
#     page.wait_for_selector("li[role='option']", timeout=3000)
   
#     ## Click Enrollement fee
#     page.locator("li[data-option-index='0']").click()

#     ## Click Students
#     student_tab_locator = page.locator("div.MuiFormControl-root:has(label:has-text('Students')) input[aria-autocomplete='list']")
#     student_tab_locator.click()

#     # Wait for the student list container to appear after clicking the button
#     ##page.locator("div.MuiAutocomplete-root").wait_for(state="visible")

#     ## Click first element
#     ##page.locator("div:has(h6.MuiTypography-root:has-text('mozilla52')) input[type='checkbox']").click()
#     page.locator("div.MuiTypography-root.MuiTypography-subtitle1:has-text('Accea man')").click()

#     ## Click 2nd element
#     page.locator("div.MuiTypography-root.MuiTypography-subtitle1:has-text('Acvvc man')").click()

#     ## Click 3rd Element
#     page.locator("div.MuiTypography-root.MuiTypography-subtitle1:has-text('Bedzm man')").click()

#     ## Click 4th element
#     page.locator("div.MuiTypography-root.MuiTypography-subtitle1:has-text('Bhaym man')").click()

#     ## Click 5th element
#     page.locator("div.MuiTypography-root.MuiTypography-subtitle1:has-text('Cbccs man')").click()

#     student_tab_locator.click()

#     ## Click Charge
#     page.locator("button[type='submit']").click()


def add_fee(page, batch_name):
    page.goto("https://aceexam-node-front.qa.mpower-social.com/batches?batchName=")
    page.pause()
    # Navigate to the batch page
    page.locator(f"//a[normalize-space()='{batch_name}']").click()
    print(f"Navigated to batch: {batch_name}")

    # Add a new fee
    page.locator("#simple-tab-5").click()
    page.locator("//button[normalize-space()='Add New Fee']").click()
    page.locator("input[name='feeTitle']").fill("Lab Fee 1")
    page.locator("input[name='amount']").fill("2000")

    # Set payment frequency and event
    page.locator("div.MuiFormControl-root:has(label:has-text('Payment Frequency')) input[role='combobox']").click()
    page.locator("//li[normalize-space()='Monthly']").click()
    page.locator("div.MuiFormControl-root:has(label:has-text('Charge Event')) input[role='combobox']").click()
    page.locator("//li[normalize-space()='Enrollment']").click()
    page.locator("button[type='submit']").click()
    print("Fee created successfully!")

    # Charge the fee to enrolled students
    page.locator("//button[normalize-space()='Charge Fees']").click()
    page.locator("div.MuiFormControl-root:has(label:has-text('Fees')) input[role='combobox']").click()
    page.locator("li[data-option-index='0']").click()

    # Select students to charge fees
    student_list_locator = page.locator("div.MuiTypography-root.MuiTypography-subtitle1")
    student_count = student_list_locator.count()

    for i in range(student_count):
        student_list_locator.nth(i).click()

    # Click Charge
    page.locator("button[type='submit']").click()
    print("Fees charged successfully!")


    
    