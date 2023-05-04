from seleniumwire import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

URL = "8306_bobokhonov_ax-app-1:5000"


class TestSelenium:
    def setup_method(self):
        binary = FirefoxBinary("/firefox/firefox")
        self.driver = webdriver.Firefox(firefox_binary=binary)

    def test_file_redirect(self):
        self.driver.get(f"http://{URL}/to_files")
        for request in self.driver.requests:
            if URL in request.url and "/to_file" in request.url:
                assert request.response.status_code == 302
            if URL in request.url and "/file" in request.url:
                assert request.response.status_code == 200

    def test_increment_redirect_loop(self):
        redirect_loop = False
        try:
            self.driver.get(f"http://{URL}/increment/0")
        except WebDriverException as e:
            redirect_loop = "redirectLoop" in e.msg
        assert redirect_loop

    def teardown_method(self):
        self.driver.close()
