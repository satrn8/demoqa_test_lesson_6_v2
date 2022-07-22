from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls.resource import resource
from demoqa_tests.model.controls.datepicker import DatePicker
from enum import Enum
from demoqa_tests.model.controls.tags_input import TagsInput
from demoqa_tests.model.controls.dropdown import Dropdown


class Months(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October = 9
    November = 10
    December = 11


def open_form():
    browser.open("/automation-practice-form")


def test_registration_form():
    open_form()

    browser.element("#firstName").type("Alyona")
    browser.element("#lastName").type("Tch")
    browser.element("#userEmail").type("verypyc@gmail.com")

    gender = '[for="gender-radio-2"]'
    browser.element(gender).click()

    browser.element("#userNumber").type("9998889988")

    calendar = '#dateOfBirthInput'
    browser.element(calendar).click()
    date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    date_of_birth.select_year(1992).select_month(Months.July).select_day(27)

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Math', autocomplete='Maths')
    subjects.add('English')
    # browser.element("#subjectsInput").type("math").press_tab()

    hobby = '[for="hobbies-checkbox-2"]'
    browser.element(hobby).click()

    browser.element("#uploadPicture").send_keys(resource('pepe.png'))
    browser.element("#currentAddress").type("Moscow")

    state = Dropdown(browser.element("#state"))
    state.select(option="NCR")
    city = Dropdown(browser.element("#city"))
    city.select(option="Gurgaon")

    browser.element("#submit").press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all(".modal-dialog").all("table tr")[1].all("td").should(have.exact_texts("Student Name", "Alyona Tch"))
    browser.all(".modal-dialog").all("table tr")[2].all("td").should(have.exact_texts("Student Email", "verypyc@gmail.com"))
    browser.all(".modal-dialog").all("table tr")[3].all("td").should(have.exact_texts("Gender", "Female"))
    browser.all(".modal-dialog").all("table tr")[4].all("td").should(have.exact_texts("Mobile", "9998889988"))
    browser.all(".modal-dialog").all("table tr")[5].all("td").should(have.exact_texts("Date of Birth", "27 July,1992"))
    browser.all(".modal-dialog").all("table tr")[6].all("td").should(have.exact_texts("Subjects", "Maths, English"))
    browser.all(".modal-dialog").all("table tr")[7].all("td").should(have.exact_texts("Hobbies", "Reading"))
    browser.all(".modal-dialog").all("table tr")[8].all("td").should(have.exact_texts("Picture", 'pepe.png'))
    browser.all(".modal-dialog").all("table tr")[9].all("td").should(have.exact_texts("Address", "Moscow"))
    browser.all(".modal-dialog").all("table tr")[10].all("td").should(have.exact_texts("State and City", "NCR Gurgaon"))
    browser.element("#closeLargeModal").press_enter()


if __name__ == '__main__':
    test_registration_form()




