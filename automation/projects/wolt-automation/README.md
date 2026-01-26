# Wolt Automation Project – Case Study (Playwright + Python)

## 🎯 Goal
Automate critical user flows on the Wolt website with a focus on navigation, content availability, and negative scenarios related to city selection.

## 🧠 Approach
- Focus on realistic end-user scenarios (positive + negative)
- Use stable locators and clear assertions
- Maintainable design using **Page Object Model (POM)**
- Keep tests readable, focused, and scalable

## 🧪 Test Scenarios (High-Level)

The following scenarios were selected to validate core user journeys and common risk areas:

- Verify that main service tabs (Restaurants, Groceries, Alcohol) are displayed after selecting a valid city
- Verify that clicking the Wolt logo redirects the user back to the homepage
- Navigate to a specific category (e.g. Restaurants) and verify that at least one result is displayed
- Verify successful navigation to the Jobs page
- Select an invalid city and verify that an appropriate error or “No addresses found” message is displayed

## 🧠 Test Design Considerations

The scenarios focus on high-impact user journeys while avoiding over-testing static content.
Priority was given to flows that are likely to break due to data, navigation, or configuration changes.


## 🛠 Tech Stack
- Python
- Playwright
- Pytest
- Page Object Model (POM)

## 🔗 Source Code
Full project repository: https://github.com/ygutmann/pom_project_wolt
