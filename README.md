# QA Automation Framework Using Python, Selenium & PyTest
![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![Selenium](https://img.shields.io/badge/Selenium-4.39.0-green) ![PyTest](https://img.shields.io/badge/PyTest-8.0.0-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview
**QA Automation Framework** is a robust, scalable Selenium-based test automation framework built with industry best practices. This framework leverages **Python, Selenium WebDriver, and PyTest** to provide automated testing capabilities for web applications. It implements the **Page Object Model (POM)** design pattern, ensuring maintainable and reusable test code.

The framework currently automates login functionality testing for **The Internet Demo Application**, demonstrating both successful and failed authentication scenarios.

## ✨ Key Highlights
- **Design Pattern**: Page Object Model (POM) for better code maintainability
- **PyTest Framework**: Powerful test framework with fixtures and detailed reporting
- **Automated Browser Management**: WebDriver Manager for seamless driver setup (no manual driver downloads needed)
- **Intelligent Waits**: WebDriverWait with expected conditions for reliable element interactions
- **Clean Architecture**: Well-organized project structure
- **Extensible Framework**: Easy to extend with additional test scenarios and pages

## 🛠️ Tech Stack
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.7+ | Core programming language |
| Selenium WebDriver | 4.39.0 | Browser automation |
| PyTest | 8.0.0 | Test framework and assertions |
| pytest-html | 4.1.1 | HTML report generation |
| webdriver-manager | 4.0.1 | Automatic browser driver management |

## 🚀 Features

### ✅ Automated Test Scenarios
- Valid and invalid login credential testing
- Success message verification after successful login
- Error message validation for failed login attempts

### ✅ Framework Capabilities
- Page Object Model (POM) architecture
- Explicit wait strategies with WebDriverWait
- Cross-browser ready (Chrome supported, extensible to others)
- PyTest fixtures for browser management
- Automatic screenshot capture on test failures
- Manual screenshot support during test execution
- HTML report generation with pytest-html
- WebDriver Manager for zero-configuration driver setup

## 📂 Project Structure

```
QA-Automation-Framework-Using-Python-Selenium-PyTest/
│
├── pages/                      # Page Object Model classes
│   └── login_page.py          # Login page object with locators and methods
│
├── tests/                      # Test cases
│   └── test_login.py          # Login functionality test cases
│
├── reports/                    # Generated test reports
│
├── screenshots/                # Screenshots captured during test execution
│   ├── valid_login.png        # Example: Valid login screenshot
│   ├── invalid_login.png      # Example: Invalid login screenshot
│   └── *_failed.png           # Auto-captured screenshots for failed tests
│
├── conftest.py                # PyTest configuration and fixtures
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

### Key Components
- **login_page.py**: Page Object for login page with element locators and action methods
- **test_login.py**: Contains test methods for valid and invalid login scenarios
- **conftest.py**: PyTest fixtures for browser setup/teardown and screenshot on failure hook

## 📋 Prerequisites
Before running this project, ensure you have the following installed:

- **Python**: Version 3.7 or higher
  ```bash
  python --version
  ```
- **pip**: Python package installer
- **Chrome Browser**: Latest stable version (for ChromeDriver compatibility)
- **IDE (Optional but recommended)**: PyCharm, VS Code, or any Python IDE

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sandeep12222300/QA-Automation-Framework-Using-Python-Selenium-PyTest.git
   cd QA-Automation-Framework-Using-Python-Selenium-PyTest
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Test Scenarios
The framework currently includes the following test scenarios:

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| test_valid_login | Verifies login with valid credentials (tomsmith/SuperSecretPassword!) | Success message is displayed |
| test_invalid_login | Verifies login failure with invalid credentials | Error message is displayed |

## ▶️ How to Run

### Run All Tests
```bash
pytest
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Specific Test Method
```bash
pytest tests/test_login.py::test_valid_login
```

### Generate HTML Report
```bash
pytest --html=reports/report.html
```

### Run Tests with Detailed Output and HTML Report
```bash
pytest -v --html=reports/report.html --self-contained-html
```

## 💡 Page Object Model (POM)

The framework uses the Page Object Model design pattern where:
- Each web page is represented by a class
- Page elements are defined as class attributes using locator tuples
- Page interactions are implemented as class methods
- Test logic is separated from page implementation
- Explicit waits are used for reliable element interactions

Example:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    username = (By.ID, "username")
    password = (By.ID, "password")
    
    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
    
    def wait_for_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.message)
        )
```

## ⚙️ Configuration

### Browser Configuration
The `conftest.py` file contains PyTest fixtures and configuration:
- **browser fixture**: Initializes and manages the WebDriver instance
- Automatically handles browser setup and teardown
- Maximizes browser window for test execution
- **pytest_runtest_makereport hook**: Automatically captures screenshots when tests fail

Currently configured for Chrome. To add support for other browsers, modify `conftest.py`:

```python
# For Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# For Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
```

### Test URL Configuration
The application URL is configured in `login_page.py`:

```python
def open(self):
    self.driver.get("https://the-internet.herokuapp.com/login")
```

### Timeout Configuration
Wait timeout is set to 10 seconds in page objects using WebDriverWait.

## 📸 Screenshots

The framework supports screenshot capture in two ways:

### 1. Automatic on Failure
Screenshots are automatically captured when a test fails (configured in `conftest.py`). Screenshots are saved in the `screenshots/` directory with the naming convention `{test_name}_failed.png`.

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}_failed.png")
```

### 2. Manual Capture
Tests can manually capture screenshots at any point during execution:

```python
import os

def test_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("username", "password")
    
    # Capture screenshot manually
    os.makedirs("screenshots", exist_ok=True)
    browser.save_screenshot("screenshots/login_success.png")
    
    assert "success" in page.get_message_text()
```

All screenshots are stored in the `screenshots/` directory.

### Example Screenshots

#### Valid Login Test
![Valid Login Screenshot](screenshots/valid_login.png)
*Screenshot captured during a successful login test*

#### Invalid Login Test
![Invalid Login Screenshot](screenshots/invalid_login.png)
*Screenshot captured during an invalid login attempt test*

## 📊 Test Reporting
Test execution results are generated in the following locations:

- **Console Output**: Real-time test execution results with pass/fail status
- **HTML Reports**: `reports/report.html`
  - Detailed test execution report with screenshots
  - Summary of passed/failed tests
  - Test duration and timestamps
- **Screenshots**: `screenshots/` directory
  - Manual screenshots from test execution
  - Automatic screenshots for failed tests

## 🐛 Troubleshooting

### Common Issues and Solutions

**Issue**: ChromeDriver version mismatch
```
Solution: WebDriver Manager automatically handles driver versions. 
Ensure you have the latest Chrome browser installed.
If issues persist, clear the driver cache:
- Windows: C:\Users\{username}\.wdm\
- macOS/Linux: ~/.wdm/
```

**Issue**: Tests failing due to timeouts
```
Solution: Increase wait times in page objects (currently set to 10 seconds).
Check your internet connection and application availability.
```

**Issue**: Import errors or module not found
```bash
# Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

**Issue**: Port already in use
```
Solution: Close any existing browser instances or ChromeDriver processes.
Use Task Manager (Windows) or Activity Monitor (macOS) to kill chromedriver processes.
```

## 📈 Future Enhancements
- [ ] **Enhanced Reporting**: Integrate Allure or Extent Reports for detailed HTML reports
- [ ] **Parallel Execution**: Configure PyTest for concurrent test execution with pytest-xdist
- [ ] **CI/CD Integration**: Add GitHub Actions/Jenkins pipeline configuration
- [ ] **Data-Driven Testing**: Implement test data management using Excel/CSV/JSON
- [ ] **Cross-Browser Testing**: Add support for Firefox, Edge, and Safari
- [ ] **Logging Framework**: Integrate logging module for comprehensive logging
- [ ] **API Testing**: Extend framework to include REST API testing capabilities with requests library
- [ ] **Docker Support**: Containerize tests for consistent execution environments
- [ ] **Video Recording**: Add video recording for test execution
- [ ] **Page Object Generator**: Tool to auto-generate page objects from web pages

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author
**B Sandeep**
- GitHub: [@sandeep12222300](https://github.com/sandeep12222300)

## 🙏 Acknowledgments
- **The Internet** (Herokuapp) for providing a demo application for testing
- **Selenium WebDriver** for browser automation capabilities
- **PyTest** for the testing framework
- **WebDriver Manager** for simplified driver management

---

**If you find this project helpful, please consider giving it a ⭐!**
