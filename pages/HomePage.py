from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage


class HomePage(BasePage):
    URL = TestData.BASE_URL

    # Локатор для лого "Лабиринт", возвращающий на главную страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # Локатор для кнопки "Принять" файлы cookie
    COOKIE_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # Локаторы меню кнопки "Книги" и кнопок подменю
    BOOKS = (By.XPATH, '//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]')
    BOOKS_PAGE_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    MAIN_OF_THE_YEAR = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                                  '"Главное 2022")]')
    MAIN_OF_THE_YEAR_HEADER = (By.XPATH, '//h1[contains(text(), "Главные книги 2022")]')
    ALL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Все книги")]')
    ALL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    TEENS_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Молодежная '
                             'литература")]')
    TEENS_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Молодежная литература")]')
    PERIODICAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                                  '"Периодические издания")]')
    PERIODICAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Периодические издания")]')

    # Локаторы второго подменю типов книг главного меню кнопки "Книги"
    BILINGUAL_FIRST_SUBMENU = (By.XPATH,
                               '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                               '"Билингвы и книги на иностранных языках")]')
    BILINGUAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Билингвы")]')
    BILINGUAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Билингвы")]')

    CHILD_BOOKS_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains('
                                           'text(), "Книги для детей")]')
    CHILD_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Детский досуг")]')
    CHILD_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Детский досуг")]')

    MANGA_FIRST_SUBMENU = (By.XPATH,
                           '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Комиксы, '
                           'Манга, Артбуки")]')
    MANGA_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Манга для детей")]')
    MANGA_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Манга для детей")]')

    RELIGION_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text('
                                        '), "Религия")]')
    RELIGION_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Религии мира")]')
    RELIGION_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Религии мира")]')

    # Локаторы локации пользователя
    REGION_ICON_BUTTON = (By.XPATH, '//span[@class="js-header-menu-region-name"]')
    REGION_CURRENT_SETTING = (By.XPATH, '//span[@class="region-location-icon-txt "]')
    REGION_SEARCH_FIELD = (By.ID, "region-post")
    # Локатор авто подстановки региона
    REGION_SUGGESTION = (By.XPATH, '//a[@class="a-item"]')

    # Локаторы верхней панели
    # Для кнопки "Сообщения"
    MESSAGE_BUTTON = (By.XPATH, '//span[@class="b-header-b-personal-e-text" and contains(text(), "Сообщения")]')
    # Для попап "Сообщения" 
    POPUP_MESSAGE_BUTTON = (By.XPATH, '//div[@class="b-menu-list-title font_regular"]')

    # Для кнопки "Мой Лабиринт"
    MY_LABIRINT_BUTTON = (By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown '
                                    'b-header-b-personal-e-list-item_cabinet"]')
    POPUP_MY_LABIRINT_BUTTON_WINDOW = (By.XPATH, '//div[@class="b-header-login-action-logo-e-wrap"]')

    # Для кнопки "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH,
                              '//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder '
                              'b-header-e-sprite-background"]')
    POPUP_POSTPONED_BOOKS_WINDOW = (
    By.XPATH, '//div[contains(text(), "Здесь будут храниться ваши отложенные товары.")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Получаем заголовок страницы"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    """Перемещаем курсор с одного элемента на другой"""

    def move_away_from_element(self, by_locator):
        element_to_move = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_move).perform()

    def presents(self, BOOKS):
        pass
