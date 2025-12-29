import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from app import app

@pytest.fixture(scope="session", autouse=True)
def setup_chromedriver():
    driver_path = ChromeDriverManager().install()
    driver_dir = os.path.dirname(driver_path)
    os.environ["PATH"] += os.pathsep + driver_dir

def pytest_setup_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    return options


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Pink Morsel Sales Analysis"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)
    region_picker = dash_duo.find_element("#region-picker")
    assert region_picker is not None