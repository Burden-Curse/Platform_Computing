import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def WritetoCSV(filename : str, metrics : dict):
    with open(file=filename, mode='w', newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=metrics[0].keys())
        writer.writeheader()

        for i in metrics:
            writer.writerow(i)

def main():
    # Initialize browser
    driver = webdriver.Firefox() #I don't have Chrome, change this to preferred browser

    #Trying to get my href button
    #button = driver.find_element(By.CSS_SELECTOR, value="a")

    #Trying to get number of paragraphs in my webpage
    Number_of_p = driver.find_elements(By.CSS_SELECTOR, "#everything .p")

    # Navigate to your website 
    Title = driver.get("http://localhost:3000/")

    driver.implicitly_wait(0.5) #probably helps for a buffer

    metrics = []
    # Track presence time
    count = 0
    SAMPLE_SIZE = 10
    start_time = time.time()
    presence_time = start_time
    while count < SAMPLE_SIZE:#presence_time < 50: # seconds
        current_time = time.time()
        presence_time = current_time - start_time
        
        # Track scrolling
        #scroll_height = driver.execute_script("return document.body.scrollHeight")
        Title_name = driver.execute_script('return document.title;')
        current_scroll = driver.execute_script("return window.pageYOffset;")

        #########
        #Optional
        #########
        # for button in buttons:
        #     button.click()
        #     num_clicks += 1
        Number = 0
        for i in Number_of_p:
            Number += i
        #Working, don't touch
        #Might make it into a Dict later on
        metrics.append({"TimeStamp (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
                        "Presense Time (Seconds)" : presence_time,
                        "Scrolling (current Pixel)" : current_scroll,
                        "Title Name" : Title_name})
        
        time.sleep(2)
        count += 1
        
    driver.quit()
    WritetoCSV("Measurements.csv", metrics)

    

if __name__ == "__main__":
    main()


###############################################
#Leaving in all my fail attempts for referrence
###############################################
        #for i in metrics:
        #    csv_writer.writerow(i)
    
    #time.sleep(2) 

    #print(f"Current Scroll pixel: {current_scroll}")
    #print(f"Current Presense Time: {metrics[1]}")
    #print(Title)
    
    #try:
        #selenium.common.exceptions.NoSuchWindowException == False
    #    driver.getTitle();
    #except:
        #break

    # Track clicks   
    # buttons = driver.find_elements_by_tag_name("button")
    # num_clicks = 0

    
        
    # print(f"Number of clicks: {num_clicks}")
#print(presence_time)
#print(f"Scrolled {current_scroll}/{scroll_height} pixels")
