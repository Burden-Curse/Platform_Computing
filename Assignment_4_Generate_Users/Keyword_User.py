import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def Keyword(driver, keyword)->bool:
    return keyword.lower() in driver.page_source.lower()

def main():
    # Initialize browser
    driver = webdriver.Firefox() #I don't have Chrome, change this to preferred browser

    
    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    keyword = ["Student", "Grade"]
    for key in keyword:
        if Keyword(driver, key):
            total_reward_time += reward_time
            time.sleep(reward_time)

    
    
    driver.quit()

    print("Presence Time:", total_reward_time)



if __name__ == "__main__":
    main()