from PageObjects.homepage import HomePage


class SearchPage(HomePage):
    _txt_search_keyword = ("id", "Q")
    _chk_advance_search = ("id", "As")
    _lst_sort_by = ("id", "products-orderby")
    _lst_display = ("id", "products-pagesize")
    _lst_view_as = ("id", "products-viewmode")

    def get_search_keyword(self):
        return self.get_text_from(self._txt_search_keyword)

    def click_on_advance_search_checkbox(self):
        self.click_on(self._chk_advance_search)

    def sort_search_results_by(self, text):
        self.select_option_with_text(self._lst_sort_by, text)

    def display_no_of_items(self, text):
        self.select_option_with_text(self._lst_display, text)

    def view_search_results_as(self, text):
        self.select_option_with_text(self._lst_view_as, text)

    def check_search_for(self, key):
        if self.get_search_keyword( ) == key:
            assert True
        else:
            assert False
