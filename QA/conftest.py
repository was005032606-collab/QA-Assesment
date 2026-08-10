import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://qae-assignment-tau.vercel.app"
USER_ID = "candidate-tXygdphSqf"

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get(f"{BASE_URL}/?user-id={USER_ID}")
    yield driver
    driver.quit()

@pytest.fixture
def api_headers():
    return {"x-user-id": USER_ID, "Content-Type": "application/json"}

@pytest.fixture
def api_base_url():
    return f"{BASE_URL}/api"