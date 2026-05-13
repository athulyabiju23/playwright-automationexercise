# Playwright E2E Test Automation

End-to-end test automation for [automationexercise.com](https://automationexercise.com) using Playwright with Python and Pytest. Built with the Page Object Model pattern and integrated with GitHub Actions CI.

## Tech Stack

- Playwright - browser automation
- Pytest - test framework
- Python 3.11
- GitHub Actions - CI/CD
- Pytest-HTML - test reports

## Test Coverage

| Flow | Tests |
|---|---|
| Smoke | 1 |
| Signup | 3 |
| Login | 4 |
| Search & Cart | 5 |
| Checkout | 4 |

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

```bash
pytest
```

HTML report is generated at `reports/report.html`.