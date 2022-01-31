
import pytest
import os
from context import autotask, constants



def test_get_expense_reports():
    report = autotask.get_expense_reports(constants.at_userID)
    assert len(report.items)!=0, "Reports list should not be empty"


""" # Warning: Expense Reports cannot be deleted through API
def test_create_expense_report():
    pytest.reportID = autotask.create_expense_report("Test User", "Internet", config.userID)
    assert pytest.reportID != 0, "ReportID should not be 0"       
        
        
# Warning: Expense Items cannot be deleted through API
def test_create_expense_item():
    pytest.itemID = autotask.create_expense_item(pytest.reportID, "Test Report", "123 Test Lane", 0.01)
    assert pytest.itemID != 0, "ItemID should not be 0"

def test_create_attachment():
    attachment_path = os.path.abspath("tests/sample.txt")
    attachmentID = autotask.create_expense_item_attachment(pytest.itemID, attachment_path)
    assert attachmentID != 0, "AttachmentID should not be 0"
 """



    

