import os , time
import subprocess

import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Set the path to your web driver executable (e.g., chromedriver, geckodriver)
# driver_path = '/path/to/your/driver/executable'
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

cwd = os.getcwd()
print("Current working directory:", cwd)
print("Terminal open sample programe")
time.sleep(2)
command = 'mkdir sample'

subprocess.run(['gnome-terminal', '--', 'bash', '-c', command])

# os.system("gnome-terminal -e 'sudo apt-get update'")
