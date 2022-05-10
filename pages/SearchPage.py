from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage


class SearchPage(BasePage):
    URL = TestData.BASE_URL + "search/"

    # Локатор для лого "Лабиринт", возвращающий на главную страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # Локатор кнопки "Принять" файлы cookie
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # Локатор для поля "Поиск по Лабиринту"
    SEARCH_FIELD = (By.ID, "search-field")
    # Локатор для отправки поиска
    SEARCH_SUBMIT = (By.XPATH, '//button[@class="b-header-b-search-e-btn"]')

    # Локатор имени автора
    AUTHOR_NAME = (By.XPATH, '//div[@class="product-author"]/a')
    # Локатор описания книги
    BOOK_DESCRIPTION = (By.XPATH, '//a[@class="product-title-link"]')

    # Локаторы подменю "ВСЕ ФИЛЬТРЫ"
    # Локатор кнопки "ВСЕ ФИЛЬТРЫ", открывающей подменю
    ALL_FILTERS = (By.XPATH, '//span[@class="navisort-item__content" and contains(text(), "ВСЕ ФИЛЬТРЫ")]')
    # Локатор кнопки "Бумажные книги" в подменю "ВСЕ ФИЛЬТРЫ"
    PAPER_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Бумажные книги")]')
    # Локатор кнопки "Электронные книги" в подменю "ВСЕ ФИЛЬТРЫ" 
    DIGITAL_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Электронные книги")]')
    # Локатор кнопки "Показать" в подменю "ВСЕ ФИЛЬТРЫ" 
    SHOW_RESULTS = (By.XPATH, '//input[@class="show-goods__button" and @value="Показать"]')
    # Локатор кнопки "ЦЕНА"
    PRICE_MENU_BUTTON = (By.XPATH, '//div[@class="bl-name" and contains(text(), "ЦЕНА")]')
    # Локатор поля устновки минимальной цены
    SET_MIN_PRICE = (By.ID, "section-search-form-price_min")
    # Локатор поля установки максимальной цены
    SET_MAX_PRICE = (By.ID, "section-search-form-price_max")

    # Локатор кнопки установок под кнопкой "ВСЕ ФИЛЬТРЫ"
    # Локатор включения "Бумажные книги" 
    ENABLED_PAPER_BOOKS = (By.XPATH, '//div[contains(text(), "Бумажные книги")]')
    # Локатор включения "В наличии" 
    BOOKS_AVAILABLE_CURRENTLY = (By.XPATH, '//div[@class="filter-reset__content" and contains(text(), "В наличии")]')
    ALL_CURRENT_SETTINGS = (By.XPATH, '//div[@class="filter-reset__content"]')

    # Локаторы элементов под обложкой книги
    # Локатор "ЭЛЕКТРОННАЯ КНИГА"
    DIGITAL_BOOKS_LABEL = (By.XPATH, '//span[@class="card-label__text card-label__text_inversed" and contains(text(), '
                                     '"Электронная книга")]')
    # Локатор кнопки "КУПИТЬ" 
    BUY_NOW_BUTTON = (By.XPATH, '//a[@class="btn buy-link js-ebooks-buy-btn btn-primary" and contains(text(), '
                                '"КУПИТЬ")]')

    # Локатор цены книги
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]/span')
    # Локатор пагинации
    PAGINATION_PAGE_BUTTON = (By.XPATH, '//a[@class="pagination-next__text" and contains(text(), "Следующая")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchPage.URL)

    """Проверяем совпадение результата поиска"""

    def search_match_fully(self, element, search_name):
        element_text = element.get_attribute(TestData.ATTRIBUTE_TITLE)
        element_in_list = element_text.lower().split()
        name_list = search_name.lower().split()
        result = list(set(element_in_list) & set(name_list))
        return len(name_list) == len(result)

    """Получаем цену книги"""

    @staticmethod
    def price_by_int(element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)
