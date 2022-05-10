from selenium.webdriver.common.by import By


class TestData:

    BASE_URL = "https://www.labirint.ru/"
    USER_NAME = "technique_88@mail.ru"
    PASSWORD = "98A7-4AD7-88D2"

    # Главная страница. Кнопка верхнего меню "Книги"
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_THE_BOOK_PAGE = "Книги"
    TITLE_OF_THE_MAIN_YEAR_BOOK_PAGE = "Главное 2022"
    ALL_BOOKS_TITLES = "Книги"
    TEENS_BOOKS_TITLE = "Молодежная литература"
    PERIODICALS_TITLE = "Периодические издания"
    BILINGUAL_TITLE = "Билингвы и книги на иностранных языках"
    CHILD_BOOKS_TITLE = "Детский досуг"
    MANGA_BOOKS_TITLE = "Манга для детей"
    RELIGION_BOOKS_TITLE = "Религии мира"

    # Настройки региона
    CITY_TO_SET = "Санкт-Петербург"
    CURRENT_CITY = "Санкт-Петербург"

    CITY_TO_SET_THE_WRONG_LAYOUT = "Abcruhmz"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Москва"

    # Количество отложенных книг
    NUMBER_OF_THE_POSTPONED_BOOKS = 3

    # Сообщение об успешном удалении товаров из Отложенных
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Сообщение об успешном удалении товаров из Корзины
    MESSAGE_OF_THE_EMPTY_BASKET = "Ваша корзина пуста. Почему?"

    # Атрибуты
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Данные для Поиска
    AUTHOR_NAME_FOR_SEARCH = "Лев Шестов"
    BOOK_NAME_FOR_SEARCH = "Достоевский и Ницше. Философия трагедии"
    BOOK_NAME_FOR_SEARCH_WITH_WRONG_LAYOUT = "abkjcjabz nhfutlbb"  
    EXPECTED_RESULT_OF_WRONG_LAYOUT = "философия трагедии"

    # Данные для фильтра Поиска
    MIN_PRICE = "500"
    MAX_PRICE = "1000"

    """Межстраничные локаторы"""
    # Локатор кнопки, закрывающий попап любого действия
    CLOSE_THE_POPUP = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """Корзина"""
    # Локатор кнопки "Корзина" в хэдере
    BASKET_BUTTON_AT_THE_HEADER = (
        By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]')
    # Локатор счетчика кнопки "Корзина"
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')


