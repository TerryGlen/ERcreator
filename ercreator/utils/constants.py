from dotenv import load_dotenv
import os
load_dotenv()

#AutoTask Configs

## ISP Configs
isp_username = os.getenv("ISP_USERNAME")
isp_password = os.getenv("ISP_PASSWORD")
isp_url = os.getenv("ISP_URL")

## AutoTask Configs
intergration_code = os.getenv("INTERGRATION_CODE")
at_username = os.getenv("AT_USERNAME")
at_secret = os.getenv("AT_SECRET")
at_userID = os.getenv("AT_USERID")


## Personal Information
fullname = os.getenv("fullname")
address = os.getenv("address")
bill_amount = os.getenv("bill_amount")


## Computer Configs
chrome_driver_path = '/usr/local/bin/chromedriver'
download_dir = os.path.join(os.path.expanduser('~'), "downloads/statements")
