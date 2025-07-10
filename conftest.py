import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def driver():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }

    options.set_capability("selenoid:options", selenoid_capabilities["selenoid:options"])

    remote_driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    yield remote_driver

    attach.add_html(remote_driver)
    attach.add_screenshot(remote_driver)
    attach.add_logs(remote_driver)
    attach.add_video(remote_driver)

    remote_driver.quit()
