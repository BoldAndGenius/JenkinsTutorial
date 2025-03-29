from Library.library import Base


class HomePage(Base):
    _lnk_register = ("link text", "Register")
    _link_login = ("link text", "Log in")
    _lnk_shopping_cart = ("xpath", "//span[.='Shopping cart']")
    _lnk_wishlist = ("xpath", "//span[.='Wishlist']")
    _lnk_logout = ("link text", "Log out")
    _txt_newsletter = ("id", "newsletter-email")
    _btn_subscribe = ("id", "newsletter-subscribe-button")
    _txt_search_store = ("id", "small-searchterms")
    _btn_search = ("css selector", "input[value='Search']")

    def click_on_register_link(self):
        self.click_on(self._lnk_register)

    def click_on_login_link(self):
        self.click_on(self._link_login)

    def click_on_shopping_cart_link(self):
        self.click_on(self._lnk_shopping_cart)

    def click_on_wishlist_link(self):
        self.click_on(self._lnk_wishlist)

    def click_on_logout_link(self):
        self.click_on(self._lnk_logout)

    def enter_email_to_newsletter(self, email):
        self.enter_text_to(self._txt_newsletter, email)

    def click_on_subscribe_button(self):
        self.click_on(self._btn_subscribe)

    def search_for(self, product):
        self.enter_text_to(self._txt_search_store, product)
        self.click_on(self._btn_search)

