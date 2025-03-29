from PageObjects.homepage import HomePage


class LoginPage(HomePage):
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _btn_login = ("css selector", "input[value='Log in']")
    _chk_remember_me = ("id", "RememberMe")
    _lnk_forgot_password = ("link text", "Forgot password?")

    def enter_email(self, email):
        self.enter_text_to(self._txt_email, email)

    def enter_password(self, password):
        self.enter_text_to(self._txt_password, password)

    def check_remember_me(self):
        self.click_on(self._chk_remember_me)

    def click_on_forgot_password(self):
        self.click_on(self._lnk_forgot_password)

    def click_on_login_button(self):
        self.click_on(self._btn_login)

    def check_login_success(self):
        ...