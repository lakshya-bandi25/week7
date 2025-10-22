import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver 
    driver.quit()

def test_google_title(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.instagram.com")
    print("Page title:", driver.title)
    assert "Instagram" in driver.title, "Test Failed: Title mismatch"