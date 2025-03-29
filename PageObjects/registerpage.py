from PageObjects.homepage import HomePage


class RegisterPage(HomePage):
    _rad_gender_male = ("id", "gender-male")
    _rad_gender_female = ("id", "gender-female")
    _txt_firstname = ("id", "FirstName")
    _txt_lastname = ("id", "LastName")
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _txt_confirm_password = ("id", "ConfirmPassword")
    _btn_register = ("id", "register-button")

    def click_on_male_radio_button(self):
        self.click_on(self._rad_gender_male)

    def click_on_female_radio_button(self):
        self.click_on(self._rad_gender_female)

    def enter_firstname(self, firstname):
        self.enter_text_to(self._txt_firstname, firstname)

    def enter_lastname(self, lastname):
        self.enter_text_to(self._txt_lastname, lastname)

    def enter_email(self, email):
        self.enter_text_to(self._txt_email, email)

    def enter_password(self, password):
        self.enter_text_to(self._txt_password, password)

    def enter_confirm_password(self, cpassword):
        self.enter_text_to(self._txt_confirm_password, cpassword)

    def click_on_register_button(self):
        self.click_on(self._btn_register)