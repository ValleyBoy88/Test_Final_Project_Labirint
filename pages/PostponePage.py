from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage


class PostponePage(BasePage):
    URL = TestData.BASE_URL

    # Локатор для лого "Лабиринт", возвращающий на главную страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # Кнопка "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # for symbol "heart" - "отложить" for books at Home Page in chapter "Что почитать: выбор редакции"
    HEART_SYMBOL_AT_THE_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')
    # Локатор для попап клика иконки "Сердце"
    POPUP_BOOK_POSTPONED = (By.XPATH, '//div[contains(text(), "Вы добавили  в отложенные книгу ")]')
    # Локатор для кнопки закрытия попап
    CLOSE_POPUP_BOOK_POSTPONED = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')
    # Локатор для количества отложенных книг
    QUANTITY_OF_POSTPONED_BOOKS = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-putorder '
                                             'basket-in-dreambox-a"]')
    # Локатор для удаления из отложенного
    DELETE_POSTPONED_BOOK = (By.XPATH, '//span[@class="b-list-item-hover pointer"]')
    # Описание книги в "Что почитать: выбор редакции" на главной странице
    BOOKS_DESCRIPTION_COVER = (By.XPATH, '//a[@class="cover"]')
    # Локатор для кнопки "Все отложенные товары" на попап сообщении
    BUTTON_IN_POSTPONE_ICON_POPUP = (By.XPATH, '//a[@class="btn btn-middle btn-clear font_size_s all-putorder-btn-js"]')

    # Локатор названия книги на странице Отложено
    BOOK_IN_POSTPONE_PAGE = (By.XPATH, '//span[@class="product-title"]')

    # Локатор кнопки "Очистить" на странице Отложено
    CLEAR_POSTPONE_BUTTON = (By.XPATH, '//a[@title="Удалить все отложенные товары"]')
    # окатор сообщения "Сообщение Выбранные товары удалены!"
    POSTPONED_BOOKS_DELETED_MESSAGE = (By.XPATH, '//p[contains(text(),"Выбранные товары удалены!")]')

    # Локатор кнопки "Выделить все" 
    SELECT_ALL_POSTPONED_BOOKS = (By.XPATH, '//a[@title="Выделить все отложенные товары"]')
    # Локаторы чекбоксов книг
    CHECKBOX_POSTPONED_BOOKS = (By.XPATH, '//label[@class="checkbox-ui checkbox-ui-m-bg checkbox-ui-m-multi '
                                          'checkbox-ui-m-big"]')
    # Локатор кнопки "Удалить" в попап меню
    DELETE_SELECTED_BOOKS = (By.XPATH, '//a[contains(text(),"Удалить")]')
    # Локатор расширенного описания отложенных книг
    ALL_SELECTED_BOOKS = (By.XPATH, '//div[@class="product-cover short-title"]')
    # Локатор кнопки "В КОРЗИНУ" под отложенными книгами
    MOVE_INTO_THE_BASKET_FROM_POSTPONE_BUTTON = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), '
                                                           '"В КОРЗИНУ")]')
    # Локатор кнопки "ОФОРМИТЬ" под отложенной книгой
    SWITCH_TO_CHECKOUT_BOOK_INTO_THE_BASKET_FROM_POSTPONE_PAGE = (By.XPATH, '//a[@class="btn buy-link btn-more" and '
                                                                            'contains( '
                                                                            'text(), "ОФОРМИТЬ")]')
    # Локатор кнопки закрытия попап
    CLOSE_POPUP_POSTPONED_BOOK_MOVED_INTO_THE_BASKET = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Получаем заголовок страницы"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    """Очищаем отложенные книги и возвращаемся на главную страницу"""

    def clear_postpone_reload_page(self):
        self.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        if self.is_visible(PostponePage.CLEAR_POSTPONE_BUTTON):
            self.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
            alert = self.driver.switch_to.alert
            alert.accept()
        self.do_click(PostponePage.LABIRINT_MAIN_LOGO)
