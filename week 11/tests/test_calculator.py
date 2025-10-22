import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time
@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
def test_google_title(setup_teardown):
    driver = setup_teardown

    driver.get("http://localhost:8000/index.html")

    driver.find_element(By.ID,"num1").send_keys("30")
    driver.find_element(By.ID,"num2").send_keys("40")

    driver.find_element(By.TAG_NAME,"button").click()

    time.sleep(1)

    result=driver.find_element(By.ID,"result").text

    assert "70" in result, f"Expected 70, but got : {result}"
    print("Tests passed")


