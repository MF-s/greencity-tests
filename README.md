🧪 GreenCity UI Test Automation

Automation framework for testing the GreenCity Events page using Selenium, Pytest, and Allure.

🚀 Tech Stack

- Python 3.10+
- Selenium WebDriver
- Pytest
- Allure Report
- Page Object Model (POM)
- Component-based architecture

📁 Project Structure

greencity-tests/
├── src/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   └── events_page.py
│   ├── components/
│   │   ├── base_component.py
│   │   └── event_card.py
├── tests/
│   └── test_events_page.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

🧩 Architecture

🔹 Page Objects

Located in src/pages/

Contain logic for full pages:

- HomePage — navigation
- EventsPage — events functionality

🔹 Components

Located in src/components/

Reusable UI elements:

- BaseComponent — base class
- EventCard — single event card

🔹 Tests

Located in tests/

Contain test scenarios using Pytest + Allure.

⚙️ Setup

1. Clone repository

git clone <your-repo-url>

cd greencity-tests

2. Create virtual environment

python -m venv .venv

3. Activate venv

Windows (PowerShell):

.\.venv\Scripts\activate

Windows (CMD):

.venv\Scripts\activate

4. Install dependencies

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

