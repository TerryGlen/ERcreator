
import pytest
import os
from context import isp, constants


billName = "test.pdf"


def test_download_maxxsouth_bill():
    billPath = isp.get_maxxsouth_bill(billName)
    assert len(billPath) != 0, "Bill path should not be empty"


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    yield
    os.remove(os.path.join(constants.download_dir, billName))
    
    

