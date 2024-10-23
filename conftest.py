from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest



@pytest.fixture(params={"edge"})
def driver(request):
    browser = request.config.getoption("--browser")
    #browser = request.param
    print(f"Creating {browser} driver")
    if browser == "edge":
        my_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install())) 
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'edge' or 'firefox', but got{browser}")

    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="Browser to execute tests(edge or firefox)"
    )