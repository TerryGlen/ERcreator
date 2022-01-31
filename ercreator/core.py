from enum import auto
from ercreator.utils import constants
from utils import autotask, isp


bill_path = isp.get_maxxsouth_bill()

reportID = autotask.create_expense_report(constants.fullname, "Internet", constants.userID)

itemID = autotask.create_expense_item(reportID, "Internet Bill" ,constants.address, constants.bill_amount)

autotask.create_expense_item_attachment(itemID, bill_path)
autotask.submit_expense_report(reportID)
