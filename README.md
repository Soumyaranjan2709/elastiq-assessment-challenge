**Overview**

This repository contains a Selenium-based test script to validate the search functionality on the Selenium Playground Table Search Demo. The script uses the pytest framework for structuring the test cases, ensuring modularity, readability, and maintainability.

**Approach**

1.	Objective:
  
    a.	Navigates to the Selenium Playground Table Search Demo.
  
    b.	Locates and interacts with the search box to search for "New York".
  
    c.	Ensure that the number of visible rows matches the count displayed in the information text.

2.	Test Flow:

    a.	Open the Selenium playground page in a browser.

    b.	Locate the search input field and type “New York”.

    c.	Capture the filtered rows that are visible in the table.

    d.	Extract the result information text displayed below the table.

    e.	Assert the number of visible rows matched the result information.

3.	Tools and Framework:

    a.	Python

    b.	Selenium

    c.	Pytest

**Prerequisites**

    Install python
    Install Google Chrome Browser or Firefox.
    Install selenium and pytest
    Command: pip install selenium pytest

**Running the test**

    Save the test script in a file named **qa_selenium_test.py**.
    Run the test using pytest: **pytest qa_selenium_test.py**

**Code Structure**

  qa_selenium_test.py: contains the test case structured using pytest.

    Fixture: Used for setting up and tearing down the WebDriver.
    Test Case: Execute the search, captures the results, and performs assertions.

**Example Output**

When searching for “New York”, the table should filter to 5 rows. The test verifies by comparing:

•	visible_rowCount: Count the rows in the table.

•	example_info: extract the “Showing 1 to 5 of 5 entries (filtered from 24 total entries)”.

•	Check for the “Showing 1 to visible_rowCount of visible_rowCount entries” in example_info, 

If the text contains in example_info, the test passes.


