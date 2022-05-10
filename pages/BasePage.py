from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Локатор для кнопки "Принять" файлы cookie
COOKIE_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """Поиск элемента"""

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """Посылаем ключ в поле ввода"""

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """Очищаем поле ввода, посылаем ключ"""

    def clear_text_and_send_text(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)

    """Очищаем поле ввода, посылаем ключ, нажимаем ENTER"""

    def clear_text_and_send_text_with_enter(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(u'\ue007')

    def clear_text_in_element_and_send_text_with_enter(self, element, text):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()
        element.send_keys(text)
        element.send_keys(u'\ue007')

    """Получаем текст элемента"""

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """Проверяем видимость элемента"""

    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def are_visible(self, by_locator) -> bool:
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(elements)

    """Проверяем, что элемент не виден"""

    def is_not_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def element_is_not_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(by_element))
        return bool(element)

    def element_is_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of(by_element))
        return bool(element)

    """ Получаем заголовок страницы"""

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    """ Поиск одного элемента"""

    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    """Поиск нескольких элементов"""

    def find_several_element(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    """Смотрим подменю"""

    def move_to_show_submenu(self, by_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()

    """Смотрим подменю и нажимаем на первый пункт"""

    def move_to_submenu_and_click_at_first_level(self, by_locator, submenu_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submenu_locator))
        submenu.click()

    """Смотрим подменю, переходим на первый пункт и нажимаем элемент второго уровня"""

    def move_to_submenu_and_click_at_second_level(self, by_locator, submenu_locator, second_level_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(submenu_locator))
        action.move_to_element(submenu).perform()
        second_level_submenu = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(second_level_locator))
        second_level_submenu.click()

    """Получаем атрибут элемента"""

    def get_attribute_value(self, by_locator, attr_name):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        value = element.get_attribute(attr_name)
        return value

    """Скроллим"""

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """Принимаем куки и закрываем попап"""

    def accept_cookies_policy(self, COOKIES_POLICY_BUTTON=None):
        if self.is_visible(COOKIES_POLICY_BUTTON):
            self.do_click(COOKIES_POLICY_BUTTON)
        else:
            pass

    """Обновляем страницу"""

    def refresh_current_url(self):
        self.driver.get(self.driver.current_url)
        self.driver.refresh()

    """Возвращаем URL"""

    def get_current_url(self):
        return self.driver.current_url
