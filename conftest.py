import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    ## My system chromedriver version differs from this one, that's why I decided to put another chromedriver to the project folder
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    yield driver
    driver.quit()
