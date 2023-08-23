import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import apen




def write_to_file(f,content):
    with open(f, "a") as file:
        file.write(content)


def start_browser():
    driver.get('https://www.google.com')    

def quit_browser():
    driver.quit()

def typethis(message , number, name ,op1):
    driver.get('https://messages.google.com/web/conversations')
    filename="data/"+number+"m.txt"
    filename2="data/"+number+"d.txt"
    filename3="data/"+number+"e.txt"
    with open(filename3, 'w') as f:
        f.write('0')
    with open(filename2, 'w') as f:
        f.write('')





    time.sleep(7)
    button = driver.find_element(By.CSS_SELECTOR,'div.fab-label')
    button.click()

    time.sleep(5)
    input_box = driver.find_element(By.CSS_SELECTOR, "input.input[data-e2e-contact-input]")
    input_box.click()





    for character in number:
        input_box.send_keys(character)
        time.sleep(0.25)  # pause for 200 milliseconds
    input_box.send_keys(Keys.RETURN)
    
    
    # Using CSS Selector
    time.sleep(5)
    
 
    text_area = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Text message"]')))
    text_area.click()
 

   
    


    #messages = apen.openinstial(message)
    time.sleep(5)
    clean_text = remove_nonbmp_chars(message)

    for line in clean_text:
    # Iterate through characters in each line
        for character in line:
            text_area.send_keys(character)
            time.sleep(0.10)  # pause for 200 milliseconds
    # After sending all characters in a line, send an "Enter" command
    text_area.send_keys(Keys.RETURN)

    write_to_file(filename,"Nav:"+message+"\n")
    
    

    while True:
        m89=get_message()
        if m89!=message:
            write_to_file(filename,name+":"+m89+"\n")
            break

    while True:

        m=get_message()

        checkq=apen.is_question(m)
        print(checkq)

        if checkq==1 and op1==1:
            datacomb="Please respond to:"+m
            write_to_file(filename2,datacomb)
            
            while True:
                fileData=read_file(filename2)
                print(fileData)
                if fileData!=datacomb:
                    fileData=read_and_clear_file(filename2)
                    print(fileData)
                    break
                time.sleep(12)
            
            op=apen.openinstial(m+"\nNav:"+fileData)
        else:
            op=apen.openinstial(m)
        ct = remove_nonbmp_chars(op)
        write_to_file(filename,"Nav:"+ct+"\n")

        a = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Text message"]')))
        a.click()
        for line in ct:
            for character in line:
                a.send_keys(character)
                time.sleep(0.10)  
        a.send_keys(Keys.RETURN)
        
        time.sleep(5)
        m=get_message()

        while True:

    
            m2=get_message()
            if m2!=m:
                write_to_file(filename,name+":"+m2+"\n")
                break
            #make a way to check a file and if there is number one then end the file 

        #make the break function
        if read_file(filename3)=="1":
            break
        


        
def remove_nonbmp_chars(text):
    return ''.join(c for c in text if c <= '\uffff')

   
def read_and_clear_file(filename):
    # Open the file and read all the data
    with open(filename, 'r') as file:
        data = file.read()
    with open(filename, 'w') as file:
        file.write('')
    return data


def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data    



def get_message():
#we need to wait for a message back 

    time.sleep(10)   
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the message id
# Find all message wrappers
    message_wrappers = soup.find_all('mws-message-wrapper')

    # Get the last message wrapper
    last_message_wrapper = message_wrappers[-1]

    # Extract the message ID
    message_id = last_message_wrapper['msg-id']

    # Extract all text messages from the last message wrapper
    message_text_parts = last_message_wrapper.find_all('div', {'class': 'text-msg'})

    # Get the last text message part
    last_message_text_part = message_text_parts[-1]

    # Extract the message text
    message_text = last_message_text_part.text

    print("Message ID:", message_id)
    print("Message text:", message_text)
    return message_text




# Initialize driver
options = Options()
options.add_argument("--user-data-dir=C:/Users/bnavv/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Profile 6")
driver = webdriver.Chrome(service=Service(r"C:\Users\bnavv\Downloads\chromedriver.exe"), options=options)   


