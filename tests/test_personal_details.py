import logging

from src.personal_details import PersonalDetails

def test_address():
    logging.info("Address...")
    return PersonalDetails.address()