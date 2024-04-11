import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def CountElements(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # Initialize browser
    driver = webdriver.Firefox() #I don't have Chrome, change this to preferred browser

    
    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    tags = ["img"]
    for tag in tags:
        num_images = CountElements(driver, tag)
        total_reward_time += reward_time * num_images
        #time.sleep(reward_time)

    
    
    driver.quit()

    print("Presence Time:", total_reward_time)



if __name__ == "__main__":
    main()