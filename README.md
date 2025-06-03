# Selenium Test Automation Script

## Overview

This script automates interactions with various web elements on a test automation practice page using Selenium WebDriver with Python.

## Prerequisites

- Python 3.x
- Chrome browser
- ChromeDriver (matching Chrome version)
- Required packages:
  ```bash
  pip install selenium requests
  ```

## Features Implemented

### 1. Form Filling

- Input fields (name, email, phone, address)

- Radio button selection (gender)

- Checkbox selection (days of week)

### 2. Dropdown Selections

- Country selection

- Color selection

- Animal selection

### 3. Date Pickers

- Calendar iteration method

- Dropdown selection method

- Date range selection

- Direct date input

### 4. File Uploads

- Single file upload

- Multiple files upload

### 5. Table Data Extraction

- Static table data extraction

- Dynamic table data extraction

- Pagination handling

### 6. Alert Handling

- Simple alert

- Confirmation alert

- Prompt alert

### 7. Mouse Actions

- Hover actions

- Double click

- Drag and drop

- Slider manipulation

### 8. Other Features

- Wikipedia search

- Broken link detection

- Shadow DOM interaction

- Form submission

## How to Run

Ensure ChromeDriver is in the specified path or update the path in the code

Run the script:

```
python your_script_name.py
```


## Notes

- The script includes extensive waits and error handling for robust execution

- Multiple approaches are shown for similar tasks (e.g., date picking)

- The script outputs extracted data to console

- All actions are performed on a test automation practice page

## Outputs

- The script will:

- Fill out forms

- Upload files

- Print table data to console

- Handle alerts

- Perform various mouse interactions

- Output status of operations

## Dependencies

- Chrome browser

- ChromeDriver matching your Chrome version

- Python packages: selenium, requests