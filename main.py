from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def testings(self):
        search_request = 'iphone 13'
        url = 'https://allo.ua'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[class="search-form__input"]').send_keys(search_request)
        browser.find_element_by_css_selector('[class ="search-form__input"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="breadcrumbs__link breadcrumbs__link--without-hover"]').text

        expectedResult = "Результати пошуку для 'iphone 13'."

        assert expectedResult in actualResult
        url = 'https://allo.ua'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[class="search-form__input"]').send_keys("Xiaomi mi 9t")
        browser.find_element_by_css_selector('[class ="search-form__input"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="breadcrumbs__link breadcrumbs__link--without-hover"]').text

        expectedResult = "Xiaomi mi 9t"

        assert expectedResult in actualResult
        browser.close()