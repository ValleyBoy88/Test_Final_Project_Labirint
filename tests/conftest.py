import pytest
from selenium import webdriver


# noinspection PyGlobalUndefined
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.set_window_size(1400, 1000)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
