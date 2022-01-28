import base64
import json
from urllib import response
import requests
from types import SimpleNamespace as Namespace
from datetime import datetime
from . import config




my_headers = {'ApiIntegrationcode' : config.intergration_code, 'UserName' : config.at_username, 'Secret' : config.at_secret, 'Content-Type': 'application/json'}

now = datetime.now()
timestamp = now.strftime("%Y-%m-%dT%H:%M:%S")

def get_expense_reports(userID):
    url = f"https://webservices5.autotask.net//atservicesrest/v1.0/ExpenseReports/query?search={{\"filter\":[{{\"op\":\"and\",\"items\":[{{\"op\":\"eq\",\"field\":\"submitterID\",\"value\":\"{userID}\"}}]}}]}}"
    response = requests.get( url, headers=my_headers)
    if response.status_code != 200 :
        raise Exception(f"Autotask Error: {response.reason}")
    reports = json.loads(response.content.decode('utf-8'), object_hook=lambda d : Namespace(**d))

    
    return reports


def create_expense_report(fullName, type, autotaskID):
    expense_report_url = "https://webservices5.autotask.net/atservicesrest/v1.0/ExpenseReports/"

    name = f"{fullName}-{now.strftime('%B')} {now.year} {type}"
    new_report = {"name" : name , "submitterID" : autotaskID, "weekEnding" : timestamp}

    
    response = requests.post(url = expense_report_url, json=new_report, headers=my_headers)
    if response.status_code != 200 :
        raise Exception(f"Autotask Error: {response.reason}")
 
    report = json.loads(response.content.decode('utf-8'), object_hook=lambda d : Namespace(**d))
    return report.itemId


def create_expense_item(expenseID, description, address, amount ):
    expense_items_url = f"https://webservices5.autotask.net/atservicesrest/v1.0/Expenses/{expenseID}/Items"
    address = address

    new_expense_item = {'description' : description, 'expenseCategory' : 3 , 'expenseDate' : timestamp, 'haveReceipt' : "true", "isBillableToCompany" : "false", "paymentType" : 14 , "expenseCurrencyExpenseAmount": amount, "expenseCategory" : 3 , "entertainmentLocation" : address }
    response = requests.post(url = expense_items_url, json=new_expense_item, headers=my_headers)
    if response.status_code != 200 :
        raise Exception(f"Autotask Error: {response.reason}")
    item = json.loads(response.content.decode('utf-8'), object_hook=lambda d : Namespace(**d))
    return item.itemId 


def create_expense_item_attachment(itemID, attachment_path):
    item_attachment_url = f"https://webservices5.autotask.net/atservicesrest/v1.0/ExpenseItems/{itemID}/Attachments/"
   
    
    
    file = open(attachment_path, "rb")
    encoded_string = base64.b64encode(file.read())
    encoded_string = encoded_string.decode("ascii")
    file.close()

  
    attachment= {"attachmentType" : "FILE_ATTACHMENT" , "publish" : 1 , "title" : "Internet Bill", "fullPath" : "Internet Bill.pdf",  "data" : encoded_string}
    response = requests.post(url = item_attachment_url, json=attachment, headers=my_headers)
    if response.status_code != 200 :
        raise Exception(f"Autotask Error: {response.reason}")

    print(response.status_code)
    print(response.content)
    attachment = json.loads(response.content.decode('utf-8'), object_hook=lambda d : Namespace(**d))
    return attachment.itemId


def submit_expense_report(reportID):
    expense_report_url = f"https://webservices5.autotask.net/atservicesrest/v1.0/ExpenseReports/"
    report = {"id": reportID, "submit" : 1}
    response = requests.patch(url = expense_report_url, json = report, headers=my_headers)
    print(response.status_code)
    print(response.content)




#TODO: Create Expense Item
#TODO: Handle Exceptions
#TODO: Don't DOX yourself
#TODO: Create Attachment

