from selene.support.shared import browser
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.resource import resource
from demoqa_tests.controls.tags_input import TagsInput


class StudentRegistrationForm:
    def set_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def set_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def set_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def set_gender(self):
        female = '[for="gender-radio-2"]'
        browser.element(female).click()
        return self

    def set_number(self, value):
        browser.element("userNumber").type(value)
        return self

    def set_date_birth(self, param):
        Date_Of_Birth = DatePicker(browser.element('#dateOfBirth'))
        Date_Of_Birth.explicit_inpit(option=param)
        return self

    def set_subjects(self, subjects: list[str]):
        for i in subjects:
            TagsInput(browser.element("#subjectsInput")).add(i)
        return self

    def set_hobbies(self):
        hobby = '[for="hobbies-checkbox-2"]'
        browser.element(hobby).click()
        return self

    def set_picture(self, value):
        browser.element("#uploadPicture").send_keys(resource(value))
        return self

    def set_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def set_states(self):
        state = Dropdown(browser.element("#state"))
        state.select(option="NCR")
        return self

    def set_cities(self):
        city = Dropdown(browser.element("#city"))
        city.select(option="Gurgaon")
        return self

    def set_submit(self):
        browser.element("#submit").click()
