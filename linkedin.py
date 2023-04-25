from selenium import webdriver  # webdriver
from getpass import getpass     # getpass is used to receive password
from selenium.webdriver.chrome.options import Options # Chrome Options
from selenium.webdriver.common.by import By  # detect the elements of page
from selenium.webdriver.support.ui import WebDriverWait # Delay
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time # Delay in code

username = input("Please enter the Linkedin username:")
print (username + " is Entered")
# getpass will not display your password
password = getpass("Please enter the Linkedin password")    
print ("Password is... don't worry ;). Only you know your password")

try:
  linkedinpost = """ Enter the post of your choice. Remember that each time you press <Enter> here, it will reflect the structure of your post on Linkedin.
  So use the right indentations to make your post look nice.
  """
  chrome_options = webdriver.ChromeOptions()
# Colab does not support real time display outputs so use the following options to ensure Colab does not crash.
  # Remove chrome popup 
  chrome_options.add_argument('--headless')                                        
  # Disable sandbox to allow colab to talk with chrome                         
  chrome_options.add_argument('--no-sandbox')                                  
  # Prevents launch flags
  chrome_options.add_argument('--disable-dev-shm-usage')                        
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  # Chromium-chromedriver driver is used as webdriver. 
  driver = webdriver.Chrome('chromedriver',options=chrome_options)              
  time.sleep(5)                                                           
  # Linkedin Login page      
  print(driver.get("https://www.linkedin.com/login"))
  print("Entering username")
  # sending username by ID
  driver.find_element(By.ID,'username').send_keys(username)                     
  print("Entering password")
  # sending password by ID
  driver.find_element(By.ID,'password').send_keys(password)                   
  print("clicking signin")
  # locating signin button by ID
  signinlocation = '//*[@id="organic-div"]/form/div[3]/button'   
  # clicking signin button using EC           
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, signinlocation))).click()    
  print("Finding post element and typing the post")
  time.sleep(7)
  # Clicking start a post - Use class and contains to find it.
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger')]//*[contains(., 'Start a post')]"))).click()
  print("Writing post")
  # Write the post by using the linkedinpost from earlier and CSS_SELECTOR
  time.sleep(2)
  driver.find_element(By.CSS_SELECTOR,"div[class='ql-editor ql-blank'][role='textbox']").send_keys(linkedinpost)
  time.sleep(6)
  print("Clicking post")
  # Click post using the XPATH method
  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view')]//*[contains(., 'Post')]"))).click()
  driver.close()
except Exception as e:
  print(e)  
