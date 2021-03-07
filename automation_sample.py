import selenium
import time

from selenium.webdriver import Chrome


def test_chek_placeholder():
    with Chrome() as driver:
        driver.get("https://a25.ru/about/vakansii/")
        driver.maximize_window()
        time.sleep(3)
        button1 = driver.find_element_by_xpath('//a[text()="Тестировщик"]')
        button1.click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, window.scrollY + 1200)")
        time.sleep(3)
        button2 = driver.find_element_by_xpath('//a[contains(text(), "Хочу быть тестировщиком в А25")]')
        button2.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        time.sleep(3)


if __name__ == '__main__':
    test_chek_placeholder()
