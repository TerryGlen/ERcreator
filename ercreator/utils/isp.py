
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from . import config
import time
import os
import sys




def get_maxxsouth_bill(billName = ""):

   
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    prefs = {"download.default_directory" : config.download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    
    with webdriver.Chrome(options=chrome_options) as driver:
        # Set timeout time 
        wait = WebDriverWait(driver, 10)
        # retrive url in headless browser
        driver.get(config.isp_url)
        
        # find search box
        userField = driver.find_element(By.ID, "textfield-1041-inputEl")
        passField = driver.find_element(By.ID, "textfield-1042-inputEl")
        userField.send_keys(config.isp_username)
        passField.send_keys(config.isp_password)

        loginButton = driver.find_element(By.ID,"button-1044")

        print("Logging in...")
        loginButton.click()
        time.sleep(3)
        
        driver.get(config.isp_url)
        time.sleep(3)
        currentDate = driver.find_element(By.ID, "comboasselectfield-1128-inputEl").get_attribute('value')

        if not billName:
            billName= f"{currentDate}.pdf"

        print("Latest Statement: " + currentDate)
        if os.path.isdir(config.download_dir):
            if len(os.listdir(config.download_dir) ) != 0:  #Check if Directory is Empty
                if billName in latest_download_file():
                      raise Exception("We already have a statement for this date!")
                   

        
        viewPDFButton = driver.find_element(By.ID, "button-1129-btnInnerEl")
        viewPDFButton.click()

        print("Downloading PDF copy to" + config.download_dir)
        wait_file_download()
        pdf_current = latest_download_file()

        
        
        os.rename(pdf_current, billName)

        pdf_path = os.path.abspath(billName)

        driver.close()
        return pdf_path




def latest_download_file():
      path = config.download_dir
      os.chdir(path)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      newest = files[-1]
      return newest
    
def wait_file_download():
    fileends = "crdownload"
    while "crdownload" == fileends:
        time.sleep(1)
        newest_file = latest_download_file()
        if "crdownload" in newest_file:
            fileends = "crdownload"
        else:
            fileends = "none"




    #TODO: Replace all Time.Sleep
    #TODO: Check if current Statement is already donwloaded, if so stop program
    #TODO: Upload (Sans Important Information) to Github
    #TODO: Intergrate with AutoTask to create a Expense Report