def goto_users_page(page):
    """Navigate to the users page."""
    users_url = "https://aceexam-node-front.qa.mpower-social.com/batches?batchName="
    page.goto(users_url)
    
    # Optional: Wait for navigation or a specific element to confirm login
    page.wait_for_url("**/batches?batchName=")  # Adjust the URL pattern if needed
    
    # Wait for the page to reach a stable state with no ongoing network requests
    #page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")  # Waits until the DOM is fully loaded

    # or wait for a specific element that indicates the page is ready
    # page.wait_for_selector("//div[@id='uniqueElementId']")
    # or wait for a specific API call to complete
    #page.wait_for_response("**/api/endpoint/path")

    # Check if the "Users" link is available
    if page.locator("//p[normalize-space()='Users']").count() > 0:
        # Click the "Users" link directly if available
        page.click("//p[normalize-space()='Users']")
    else:
        # Otherwise, toggle the sidebar
        page.click("//div[@class='MuiAvatar-root MuiAvatar-rounded MuiAvatar-colorDefault css-1sq9373']//*[name()='svg']")

        # Wait for the "Users" link to become available
        page.wait_for_selector("//p[normalize-space()='Users']")

        # Click the "Users" link
        page.click("//p[normalize-space()='Users']")

    # Click the Teacher tab
    page.click("//a[@id='simple-tab-1']")

    # Wait for the 'Add New User' button to be available
    page.wait_for_selector("//button[normalize-space()='Add New User']")

    # Click the 'Add New User' button to open the form
    page.click("//button[normalize-space()='Add New User']")

    # Click the input field with name 'roles' to open the dropdown
    page.click("input[name='roles']")

    # Wait for the dropdown options to appear
    page.wait_for_selector("//ul[contains(@class, 'MuiAutocomplete-listbox')]")

    # Select the desired option by visible text
    page.click("//li[normalize-space()='Teacher']") 
    # Enter other inputs
    page.fill("input[name='firstName']", "Teacher")
    page.fill("input[name='lastName']", "Rumman1")
    page.fill("input[name='contactNo']", "01122223333")
    page.fill("input[name='email']", "duce@bigolo.com")
    # Select the female radio button
    page.check("input[name='gender'][value='female']")
    page.fill("input[name='userName']", "rumman1")
    page.fill("input[name='password']", "12345678")

    # Click the button with type="submit"
    #page.click("button[type='submit']")
    # Click the button with visible text "Next"
    page.click("//button[normalize-space()='Next']")

    # Wait for the "Submit" button in the confirmation popup to appear
    page.wait_for_selector("//button[normalize-space()='Submit']")

    # Click the "Submit" button
    page.click("//button[normalize-space()='Submit']")

    # Wait for the confirmation dialog to appear
    page.wait_for_selector("//p[@id='alert-dialog-description']")

    # Get the message text
    message_text = page.text_content("//p[@id='alert-dialog-description']")

    # Validate the message
    assert "User with details created successfully" in message_text, "Confirmation message validation failed"

    print("Confirmation message validated successfully!")

    ##  Close the success message
    page.locator("//button[@aria-label='Close']").click()

    # click search to verify it's added
    page.locator("//input[@type='text']").click()

    ## sendKeys to thhe search field
    page.locator("//input[@type='text']").fill("rumman1")

    # Wait for the search results to appear
    page.wait_for_selector("//h6[normalize-space()='Teacher Rumman1']", timeout=10000)

    # Validate that the teacher appears in the search results
    search_result = page.locator("//h6[normalize-space()='Teacher Rumman1']").count()
    assert search_result > 0, "Teacher not found in the search results"
    print("Teacher validated in the list successfully!")