from selene import have
from selene.support.shared import browser
from demoqa_tests.controls.resourse import resourse
from demoqa_tests.controls.datepicker import DatePicker
from enum import Enum
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table


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


class Student:
    first_name = "Alyona"
    last_name = "Tch"
    email = "verypyc@gmail.com"
    gender = "Female"
    mobile = "9998889988"
    date_of_birth = "27 July,1992"
    subjects = "Maths"
    hobbies = "Reading"
    picture = "pepe.png"
    address = "Moscow"
    state = "NCR"
    city = "Gurgaon"


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

    hobby = '[for="hobbies-checkbox-2"]'
    browser.element(hobby).click()

    browser.element("#uploadPicture").send_keys(resourse('pepe.png'))
    browser.element("#currentAddress").type("Moscow")

    state = Dropdown(browser.element("#state"))
    state.select(option="NCR")
    city = Dropdown(browser.element("#city"))
    city.select(option="Gurgaon")
    browser.element("#submit").press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    result = Table(browser.element('.modal-content .table'))
    result.cells_of_row(1).should(have.exact_texts("Student Name", "Alyona Tch"))
    result.cells_of_row(2).should(have.exact_texts("Student Email", "verypyc@gmail.com"))
    result.cells_of_row(3).should(have.exact_texts("Gender", "Female"))
    result.cells_of_row(4).should(have.exact_texts("Mobile", "9998889988"))
    result.cells_of_row(5).should(have.exact_texts("Date of Birth", "27 July,1992"))
    result.cells_of_row(6).should(have.exact_texts("Subjects", "Maths, English"))
    result.cells_of_row(7).should(have.exact_texts("Hobbies", "Reading"))
    result.cells_of_row(8).should(have.exact_texts("Picture", 'pepe.png'))
    result.cells_of_row(9).should(have.exact_texts("Address", "Moscow"))
    result.cells_of_row(10).should(have.exact_texts("State and City", "NCR Gurgaon"))

    browser.element("#closeLargeModal").press_enter()


if __name__ == '__main__':
    test_registration_form()



