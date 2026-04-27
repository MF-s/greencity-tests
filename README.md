GreenCity Tests

📌 Description

This project contains automated UI tests for the GreenCity Events page.
Tests are implemented using Python, Selenium WebDriver, and unittest framework.

🔗 Tested page

https://www.greencity.cx.ua/#/greenCity/events

🧪 Test Coverage

Events list is displayed

Event details can be opened

Search input works coreclty

Open invalid URL

⚙️ How to run tests

1. Install dependencies:

pip install -r requirements.txt

▶️ Running Tests

Run all tests:

pytest

Run with Allure results:

pytest --alluredir=allure-results

📊 Allure Report

Generate and open report:

allure serve allure-results

📌 Report includes:

- test steps
- statuses (passed/failed)
- execution timeline
- error details

✅ Test Coverage

✔ TC1: Events list is displayed
- Verify events page loads
- Check at least one event exists
✔ TC2: Open event details
- Click "More"
- Verify event details page opens
❌ TC3: Search functionality (BUG)
- Search works for 1 letter
- Fails for full word ("Eco")
✔ TC4: Invalid URL handling
- Open invalid page
- Verify error message

⚠️ Notes

- Uses explicit waits only (no time.sleep())
- Some tests may be flaky due to UI loading delays
- Search test intentionally detects a bug

🧹 .gitignore

Ignored:

__pycache__/

.pytest_cache/

venv/

.venv/

allure-results/

📌 Requirements

Google Chrome installed

Compatible ChromeDriver (or Selenium Manager)

🧑‍💻 Author

Maksymilian Finohenov (SoftServe course)