from selene.support.shared import browser
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.resource import resource
from demoqa_tests.model.controls.tags_input import TagsInput


class StudentRegistrationForm:
    def first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def gender(self, value):
        female = '[for="gender-radio-2"]'
        browser.element(female).click()

    def number(self, value):
        browser.element("userNumber").type(value)
        return self

    def date_birth(self, param):
        date_of_birth = DatePicker(browser.element('#dateOfBirth'))
        date_of_birth.explicit_inpit(option=param)
        return self

    def subjects(self):
        pass

    def hobbies(self):
        hobby = '[for="hobbies-checkbox-2"]'
        browser.element(hobby).click()

    def picture(self, value):
        browser.element("#uploadPicture").send_keys(resource(value))
        return self

    def address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def states(self):
        state = Dropdown(browser.element("#state"))
        state.select(option="NCR")

    def cities(self):
        city = Dropdown(browser.element("#city"))
        city.select(option="Gurgaon")

    def submit(self):
        browser.element("#submit").click()
