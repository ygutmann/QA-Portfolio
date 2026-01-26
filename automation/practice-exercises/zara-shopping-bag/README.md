# Zara – Shopping Bag Smoke Tests

## Overview
This project contains basic smoke tests for the Zara website,
focusing on the shopping bag functionality for a new user session.

## Test Scenarios Covered
1. Verify that the Shopping Bag link is visible in the header
2. Verify that the shopping bag counter is initialized to zero

## Technologies
- Python
- Pytest
- Playwright

## Testing Approach
- Tests are separated to isolate failures
- Stable locators are preferred (data-qa-id where available)
- Assertions focus on expected UI behavior

## Known Limitations
- No login flow is covered
- Tests assume an empty cart on first load
- UI changes may affect locators

## Possible Improvements
- Add API-based cart reset
- Add mobile viewport coverage
- Move configuration to environment variables

## How to Run Locally

1. Create and activate a virtual environment
2. Install dependencies:
   `pip install -r requirements.txt`
3. Install Playwright browsers:
   `playwright install`
4. Run tests:
   `pytest -q`

