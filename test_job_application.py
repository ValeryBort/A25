from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Chrome


def test_job_application_is_available():
    """
    Анкета соискателя на должность тестировщика доступна
    """
    with Chrome() as driver:
        driver.get("https://a25.ru/about/vakansii/")
        driver.maximize_window()
        button1 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Тестировщик"]'))
        )
        button1.click()
        driver.execute_script("window.scrollTo(0, window.scrollY + 1200)")
        button2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Хочу быть тестировщиком в А25")]'))
        )
        button2.click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        header = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )

        assert header.text == "Работа в команде А25", "Job application page is not available"
