import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LocalDriver:
    
    def get_driver(self):
        chrome_options= Options()
        download_location = os.path.abspath("tmp")
        
        prefs = {'download.default_directory': download_location,
                    'download.prompt_for_download': False,
                    'download.directory_upgrade': True,
                    'safebrowsing.enabled': False,
                    'safebrowsing.disable_download_protection': True,
                    'profile.default_content_setting_values.automatic_downloads': 1}

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_experimental_option("detach", True)

        return webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)



