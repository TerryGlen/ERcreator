from enum import auto
from utils import autotask, config, isp


bill_path = isp.get_maxxsouth_bill()

reportID = autotask.create_expense_report(config.fullname, "Internet", config.userID)

itemID = autotask.create_expense_item(reportID, "Internet Bill" ,config.address, config.bill_amount)

autotask.create_expense_item_attachment(itemID, bill_path)
autotask.submit_expense_report(reportID)
