import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService  # Changed import
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Changed import
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())  # Changed service and manager
    driver = webdriver.Edge(service=service)  # Changed webdriver
    yield driver
    driver.quit()

def test_edge_google_title(driver):  # Checks if the title of the page is correct
    driver.get("https://www.atinitysol.com/")
    assert "Atinity" in driver.title

def test_edge_navbar_links(driver):  # Checks if the Navbar links are working
    driver.get("https://www.atinitysol.com/")
    driver.find_element(By.LINK_TEXT, "About").click()
    WebDriverWait(driver, 10).until(EC.url_contains("about"))
    driver.find_element(By.LINK_TEXT, "Services").click()
    WebDriverWait(driver, 10).until(EC.url_contains("services"))
    driver.find_element(By.LINK_TEXT, "Blog").click()
    WebDriverWait(driver, 10).until(EC.url_contains("blog"))
    driver.find_element(By.LINK_TEXT, "Projects").click()
    WebDriverWait(driver, 10).until(EC.url_contains("projects"))
    driver.find_element(By.LINK_TEXT, "Contact").click()
    WebDriverWait(driver, 10).until(EC.url_contains("contact"))