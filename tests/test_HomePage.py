from config.config import TestData
from pages.HomePage import HomePage
from tests.test_base import BaseTest


class TestHomePageMainMenu(BaseTest):

    # Проверяем, что кнопка "Книги" отображается
    def test_books_button_presents(self):
        self.homePage = HomePage(self.driver)
        button = self.homePage.presents(HomePage.BOOKS)
        assert True == button

    # Проверяем, что кнопка "Книги" соответственно названа
    def test_books_button_has_proper_name(self):
        self.homePage = HomePage(self.driver)
        button_name = self.homePage.get_element_text(HomePage.BOOKS)
        assert button_name == TestData.BOOKS_BUTTON_DESCRIPTION

    # Проверяем, что кнопка "Книги" кликабельна и ведет на соответствующую страницу
    def test_books_button_clickable(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.BOOKS)
        book_page_header = self.homePage.get_element_text(HomePage.BOOKS_PAGE_HEADER)
        assert book_page_header == TestData.TITLE_OF_THE_BOOK_PAGE

    # Проверяем кликабельность и соответствие подменю "Главное 2022" кнопки "Книги"
    def test_submenu_books_of_year_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.MAIN_OF_THE_YEAR)
        books_main_of_the_year_title = self.homePage.get_element_text(HomePage.MAIN_OF_THE_YEAR_HEADER)
        assert books_main_of_the_year_title == TestData.TITLE_OF_THE_MAIN_YEAR_BOOK_PAGE

    # Проверяем кликабельность и соответствие подменю "Все книги" кнопки "Книги"
    def test_submenu_all_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.ALL_BOOKS)
        all_books_title = self.homePage.get_element_text(HomePage.ALL_BOOKS_HEADER)
        assert all_books_title == TestData.ALL_BOOKS_TITLES

    # Проверяем кликабельность и соответствие подменю "Молодежная литература" кнопки "Книги"
    def test_submenu_teens_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.TEENS_BOOKS)
        teens_books_title = self.homePage.get_element_text(HomePage.TEENS_BOOKS_HEADER)
        assert teens_books_title == TestData.TEENS_BOOKS_TITLE

    # Проверяем кликабельность и соответствие подменю "Периодические издания" кнопки "Книги"
    def test_periodicals_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.PERIODICAL_BOOKS)
        periodicals_title = self.homePage.get_element_text(HomePage.PERIODICAL_BOOKS_HEADER)
        assert periodicals_title == TestData.PERIODICALS_TITLE

    # Проверяем кликабельность и соответствие подменю "Билингвы и книги на иностранных языках" кнопки "Книги"
    def test_bilingual_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.BILINGUAL_FIRST_SUBMENU,
                                                                HomePage.BILINGUAL_BOOKS)
        bilingual_title = self.homePage.get_element_text(HomePage.BILINGUAL_BOOKS_HEADER)
        assert bilingual_title == TestData.BILINGUAL_TITLE

    # Проверяем кликабельность и соответствие подменю "Комиксы, Манга, Артбуки" кнопки "Книги"
    def test_manga_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.MANGA_FIRST_SUBMENU,
                                                                HomePage.MANGA_BOOKS)
        manga_books_title = self.homePage.get_element_text(HomePage.MANGA_BOOKS_HEADER)
        assert manga_books_title == TestData.MANGA_BOOKS_TITLE

    # Проверяем кликабельность и соответствие подменю "Религия" кнопки "Книги"
    def test_religion_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.RELIGION_FIRST_SUBMENU,
                                                                HomePage.RELIGION_BOOKS)
        religion_books_title = self.homePage.get_element_text(HomePage.RELIGION_BOOKS_HEADER)
        assert religion_books_title == TestData.RELIGION_BOOKS_TITLE

    # Проверяем локацию пользователя
    def test_to_set_current_region(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text_with_enter(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET)
        city_after_setting = self.homePage.get_element_text(HomePage.REGION_CURRENT_SETTING)
        assert city_after_setting == TestData.CURRENT_CITY

    # Проверяем ввод региона с неправильной раскладкой
    def test_auto_advice_to_set_current_region_in_wrong_layout(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET_THE_WRONG_LAYOUT)
        self.auto_advice_cities = self.homePage.find_several_element(HomePage.REGION_SUGGESTION)
        first_city_in_list = self.auto_advice_cities[0]
        assert TestData.FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC in first_city_in_list.text

    # Проверяем попап кнопки "Сообщение"
    def test_popup_window_message_button_appears(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MESSAGE_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MESSAGE_BUTTON)
        assert popup_window is True

    # Проверяем появление и исчезновение попап сообщения кнопки "Сообщение" 
    def test_popup_window_message_button_disappears(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MESSAGE_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MESSAGE_BUTTON)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert window_disappeared is True

    # Проверяем появление попап кнопки "Мой Лабиринт" 
    def test_popup_window_my_labirint_button_appear(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MY_LABIRINT_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert popup_window is True

    # Проверяем появление и исчезновение попап кнопки "Мой Лабиринт"
    def test_popup_window_my_labirint_button_disappears(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MY_LABIRINT_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert window_disappeared is True

    # Проверяем появление попап кнопки "Отложено" 
    def test_popup_window_postponed_button_appears(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.POSTPONED_BOOKS_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert popup_window is True

    # Проверяем появление и исчезновение попап кнопки "Отложено"
    def test_popup_window_my_postponed_button_disappears(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.POSTPONED_BOOKS_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert window_disappeared is True
