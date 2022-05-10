import pytest
from config.config import TestData
from pages.SearchPage import SearchPage
from tests.test_base import BaseTest


class TestSearchPage(BaseTest):

    # Проверяем соответствие поиска по имени автора нашим ожиданиям
    def test_search_by_author(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.accept_cookies_policy()
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_NAME_FOR_SEARCH)
        self.search_result_list = self.searchPage.find_several_element(SearchPage.AUTHOR_NAME)
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_NAME_FOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # Проверяем поиск по имени автора в описании книги
    @pytest.mark.xfail
    def test_that_search_by_author_made_in_book_description(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_NAME_FOR_SEARCH)
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_NAME_FOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # Проверяем поиск по имени автора в кириллической раскладке
    @pytest.mark.xfail
    def test_that_search_by_book_name_works(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.BOOK_NAME_FOR_SEARCH)
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.BOOK_NAME_FOR_SEARCH):
                counter += 1
            else:
                pass
        assert counter > 0

    # Проверяем поиск по названию книги в неправильной раскладке
    def test_that_search_by_book_name_works_if_russian_word_is_typed_in_latin(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.clear_text_and_send_text(SearchPage.SEARCH_FIELD,
                                                 TestData.BOOK_NAME_FOR_SEARCH_WITH_WRONG_LAYOUT)
        self.searchPage.do_click(SearchPage.SEARCH_SUBMIT)
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.EXPECTED_RESULT_OF_WRONG_LAYOUT):
                counter += 1
            else:
                pass
        assert counter > 0

    # Проверяем, что кнопка "ВСЕ ФИЛЬТРЫ" открывает подменю "ВСЕ ФИЛЬТРЫ", а электронные книги исчезают после нажатия на
    # кнопку "Электронные книги"
    def test_that_submenu_search_opens_and_disabling_digital_books_works(self):
        self.searchPage = SearchPage(self.driver)
        self.list_of_digital_books = self.searchPage.find_several_element(SearchPage.DIGITAL_BOOKS_LABEL)
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        button_to_open_all_filters[0].click()
        self.searchPage.do_click(SearchPage.DIGITAL_BOOKS_IN_ALL_FILTERS)
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        for book in self.list_of_digital_books:
            assert self.searchPage.element_is_not_visible(book)

    # Проверяем, что кнопка "Бумажные книги" работает, а при клике на нее исчезает быстра кнопка "Бумажные книги"
    def test_that_paper_book_button_in_hidden_submenu_remove_quick_button_from_page(self):
        self.searchPage = SearchPage(self.driver)
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        button_to_open_all_filters[0].click()
        self.searchPage.do_click(SearchPage.PAPER_BOOKS_IN_ALL_FILTERS)
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        assert self.searchPage.is_not_visible(SearchPage.ENABLED_PAPER_BOOKS)

    # Проверяем работоспособность кнопки "В наличии"
    def test_that_quick_button_books_available_works(self):
        self.searchPage = SearchPage(self.driver)
        # находим все книги с кнопкой "В КОРЗИНУ"
        self.list_of_currently_available = self.searchPage.find_several_element(SearchPage.BUY_NOW_BUTTON)
        # находим кнопку "В наличии"
        self.searchPage.do_click(SearchPage.BOOKS_AVAILABLE_CURRENTLY)
        # проверяем, что исчезли все книги с кнопкой "В КОРЗИНУ"
        for book in self.list_of_currently_available:
            assert self.searchPage.element_is_not_visible(book)
