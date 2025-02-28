import logging

from src.main import address

def test_address():
    address = "20, zz street, Los Angeles"
    logging.info("Address...")
    assert address