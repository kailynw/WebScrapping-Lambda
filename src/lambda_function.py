import sys
import time
import os
from src.driver.LambdaDriver import LambdaDriver
from src.driver.LocalDriver import LocalDriver

def is_local():
    is_windows= "win32" in sys.platform
    return is_windows

def lambda_handler(*args, **kwargs):
    # driver = LambdaDriver().get_driver()
    driver= LocalDriver().get_driver()
    driver.get("https://google.com")
    time.sleep(2)
    # xpath='(//div//h1)[1]'
    # elem_value = driver.find_element_by_xpath(xpath)
    # example_text=elem_value.get_attribute('innerHTML')
    driver.close()
    driver.quit()
    os.system('killall chrome')


    # return example_text

if __name__=="__main__":
    lambda_handler()