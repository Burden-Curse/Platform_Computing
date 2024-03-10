from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #Using Firefox cause Chrome sucks and i don't have Chrome installed

driver.get("https://www.selenium.dev/selenium/web/web-form.html") #Gets link to website

title = driver.title #Get's website's title

driver.implicitly_wait(0.5) #adds buffer time for Selenium to get the information

text_box = driver.find_element(by=By.NAME, value="my-text") #looks for text box named "my-text" which is equal to Text input top right
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") #This finds the button in the middle of the page called "Submit"

text_box.send_keys("Selenium") #inserts the word "Selenium" into text input
submit_button.click() #clicks the Submit button

message = driver.find_element(by=By.ID, value="message") #gets the message from the webpage
text = message.text #inserts the message into this variable

# Added this in for my understanding
print(text) #print out the variable


driver.quit() #Disconnects