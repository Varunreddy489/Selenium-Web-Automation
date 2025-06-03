import time
import requests
from selenium import webdriver
from click import confirmation_option
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

wait = WebDriverWait(driver, 10)

# name_input
first_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']")))
first_name.clear()
first_name.send_keys("Varunreddy")

# email_input
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
email_input.clear()
email_input.send_keys("ss9202@srmist.edu.in")

# Phone Number
phone = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='phone']")))
phone.clear()
phone.send_keys("1231231231")

# Address
address = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//textarea[@id='textarea']"))
)
address.clear()
address.send_keys("Chennai")

# Gender
label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='male']")))
label.click()

# Selecting Days
checkboxes = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='form-check form-check-inline']/input")
    )
)

for checkbox in checkboxes:
    value = checkbox.get_attribute("value")

    if value == "sunday":
        driver.execute_script("arguments[0].click();", checkbox)
        break

# Selecting Dropdown Countries

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='country']")))

options = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//select[@id='country']/option"))
)

for i in options:
    value = i.get_attribute("value")

    if value == "india":
        i.click()

# Selecting Color in dropdown

wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='colors']")))

options = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//select[@id='colors']/option"))
)

for i in options:
    value = i.get_attribute("value")

    if value == "red":
        i.click()

# selecting a sorted list
select = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))

select.select_by_value("cat")

# date picker
# 1. Iterate the calendar

date_year = "2026"
date_month = "February"
date_day = "28"

date_input1 = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date_input1.click()

while True:
    month = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-month']").text

    year = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-year']").text

    if month == date_month and year == date_year:
        break

    driver.find_element(By.XPATH, "//a[@title='Next' and @data-handler='next']").click()

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for ele in dates:
    if ele.text == date_day:
        ele.click()
        break

# 2. Using dropdowns

year = '2026'
month = 'Jan'
day = '02'

driver.find_element(By.XPATH, '//*[@id="txtDate"]').click()

month_drop = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month_drop.select_by_visible_text(month)

year_drop = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year_drop.select_by_visible_text(year)

dates = driver.find_elements(By.XPATH, '//tbody/tr/td/a')

for date in dates:
    if date.text == str(int(day)):
        date.click()
        time.sleep(2)
        break

# 3. Date Range
start_date = '2025-12-01'
end_date = '2025-12-31'

driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys(start_date)

driver.find_element(By.XPATH, "//input[@id='end-date']").send_keys(end_date)

driver.find_element(By.XPATH, "//button[@class='submit-btn']").click()

# Select the day
dates = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a"))
)
for d in dates:
    if d.text == day:
        d.click()
        break

# upload files
img1 = r"C:\Users\varun\OneDrive\Desktop\Screenshot 2024-12-15 224845.png"
img2 = r"C:\Users\varun\OneDrive\Desktop\Screenshot 2024-12-15 224903.png"

single_file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='singleFileInput']")))

# send single file
single_file_input.send_keys(img1)
driver.find_element(By.XPATH, "//form[@id='singleFileForm']/button").click()

# send multiple files
multiple_file_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='multipleFilesInput']"))
)

files = f"{img1}\n{img2}"  # newline-separated file paths
multiple_file_input.send_keys(files)

driver.find_element(By.XPATH, "//form[@id='multipleFilesForm']/button").click()

# Extracting data from Table
rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@name='BookTable']/tbody/tr")))

# Print header
headers = [th.text for th in rows[0].find_elements(By.TAG_NAME, "th")]
print("{:<25} {:<15} {:<15} {:<10}".format(*headers))
print("-" * 70)

# Print each row (skip header row)
for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    print("{:<25} {:<15} {:<15} {:<10}".format(*data))

print()

# Dynamic Table

headers = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//table[@id='taskTable']/thead/tr/th")))
header_text = [h.text for h in headers]
print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(*header_text))
print("-" * 80)

# Get all table rows (not just cells)
rows = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//table[@id='taskTable']/tbody/tr")))

# Loop through each row and print the columns
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(*data))

# Pagination

total_pages = len(driver.find_elements(By.XPATH, "//ul[@class='pagination']/li"))

for page in range(1, total_pages + 1):
    # Wait and get all checkboxes on current page
    checkboxes = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//table[@id='productTable']/tbody/tr/td/input[@type='checkbox']"))
    )

    # Click only if not already selected
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

    # Move to next page if not the last one
    if page < total_pages:
        next_page = driver.find_element(By.XPATH, f"//ul[@class='pagination']/li[{page + 1}]/a")
        next_page.click()
        time.sleep(1)

# Search Wikipedia
search_input = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
search_but = driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']")
search_but.submit()
time.sleep(2)


# alerts and  pop-ups

# 1.Alert Button
alert = driver.find_element(By.XPATH, "//button[@id='alertBtn']")
alert.click()

simple_alert = driver.switch_to.alert  # Switch to alert and accept
print("Alert Text:", simple_alert.text)
simple_alert.accept()

# 2.Confirmation Button
driver.find_element(By.XPATH, "//button[@id='confirmBtn']").click()

conf_alert = driver.switch_to.alert  # Switch to confirmation alert and accept
print("Confirmation Alert Text:", conf_alert.text)
conf_alert.accept()

# 3. Prompt Button
driver.find_element(By.XPATH, "//button[@id='promptBtn']").click()

prompt_alert = driver.switch_to.alert  # Switch to prompt alert
print("Prompt Alert Text:", prompt_alert.text)
prompt_alert.send_keys("Hello, this is a prompt alert!")
prompt_alert.accept()

# 4. Opens New tab

driver.find_element(By.XPATH, "//button[text()='New Tab']").click()



# Mouse Actions
act = ActionChains(driver)

hover_ele = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='dropbtn']")))  # Hover over the button

act.move_to_element(hover_ele).perform()

# double click element
double_click_ele = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")

act.double_click(double_click_ele).perform()
print("Double click action performed on the button.")
time.sleep(4)
# drag and drop
drag = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='draggable']")))
drop = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='droppable']")))

act.drag_and_drop(drag, drop).perform()
print("Drag and drop action performed.")

# Slider

min_val = wait.until(EC.presence_of_element_located(
    (By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")))

max_val = wait.until(EC.presence_of_element_located(
    (By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")))

act.drag_and_drop_by_offset(min_val, 150, 0).perform()
act.drag_and_drop_by_offset(max_val, -150, 0).perform()

# refetch the slider elements to get their new positions
min_val = driver.find_element(By.XPATH, " //*[@id='slider-range']/span[1]")
max_val = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of sliders after dragging:")
print("Min slider location:", min_val.location)
print("Max slider location:", max_val.location)

# scrolling dropdown

combo = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='comboBox']")))
driver.execute_script("arguments[0].scrollIntoView(true);", combo)
time.sleep(1)  # optional pause to ensure visibility
combo.click()

options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='dropdown']/div")))

item = driver.find_element(By.XPATH, "//div[@id='dropdown']/div[text()='Item 78']")
item.click()
driver.execute_script("arguments[0].scrollIntoView();", item)
value = driver.execute_script("return window.pageYOffset")
print("Current Y Offset after scrolling to Item 78:", value)

# handling links

links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='laptops']/a")))

for link in links:
    link_text = link.text
    print("Link Text:", link_text)
    href = link.get_attribute("href")
    print("Link Href:", href)

# Broken links

links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='broken-links']/a")))

count = 0

for link in links:
    url = link.get_attribute("href")

    try:
        res = requests.head(url)
    except requests.exceptions.RequestException as e:
        None

    if res.status_code > 400:
        print(url, "is a broken link")
        count += 1
    else:
        print(url, "is a valid link")

print(f"Total broken links: {count}")

# form submission

# section-1
driver.find_element(By.XPATH, "//input[@id='input1']").send_keys("Varun")

driver.find_element(By.XPATH, "//button[@id='btn1']").click()

# section-2
driver.find_element(By.XPATH, "//input[@id='input2']").send_keys("Varun")

driver.find_element(By.XPATH, "//button[@id='btn2']").click()

# section-3
driver.find_element(By.XPATH, "//input[@id='input3']").send_keys("Varun")

driver.find_element(By.XPATH, "//button[@id='btn3']").click()

# shadow DOM

shadow_host = driver.find_element(By.ID, "shadow_host")
shadow_root = shadow_host.shadow_root

input1 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Varunreddy")
input2 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
input2.click()
input3 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(
    r"C:\Users\varun\OneDrive\Desktop\Screenshot 2024-12-15 224903.png"
)

blog_link = shadow_root.find_element(By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
driver.execute_script("arguments[0].click();", blog_link)

driver.back()

time.sleep(5)
driver.quit()
