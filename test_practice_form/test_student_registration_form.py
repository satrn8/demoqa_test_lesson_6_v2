from selene import have
from selene.support.shared import browser
import os


def open_form():
    browser.open("/automation-practice-form")


def test_registration_form():
    open_form()


    browser.element("#firstName").type("Alyona")
    browser.element("#lastName").type("Tch")
    browser.element("#userEmail").type("verypyc@gmail.com")
    browser.element('[for="gender-radio-2"]').click()
    browser.element("#userNumber").type("9998889988")
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__year-select [value="1992"]').click()
    browser.element('.react-datepicker__month-select [value="6"]').click()
    browser.element(".react-datepicker__day--027").click()
    browser.element("#subjectsInput").type("math").press_tab()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('../resources/pepe.png'))
    browser.element("#currentAddress").type("Moscow")
    browser.element("#state").element("input").type("NCR").press_enter()
    browser.element("#city").element("input").type("Gurgaon").press_enter()
    browser.element("#submit").press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all(".modal-dialog").all("table tr")[1].all("td").should(have.exact_texts("Student Name", "Alyona Tch"))
    browser.all(".modal-dialog").all("table tr")[2].all("td").should(have.exact_texts("Student Email", "verypyc@gmail.com"))
    browser.all(".modal-dialog").all("table tr")[3].all("td").should(have.exact_texts("Gender", "Female"))
    browser.all(".modal-dialog").all("table tr")[4].all("td").should(have.exact_texts("Mobile", "9998889988"))
    browser.all(".modal-dialog").all("table tr")[5].all("td").should(have.exact_texts("Date of Birth", "27 July,1992"))
    browser.all(".modal-dialog").all("table tr")[6].all("td").should(have.exact_texts("Subjects", "Maths"))
    browser.all(".modal-dialog").all("table tr")[7].all("td").should(have.exact_texts("Hobbies", "Reading"))
    browser.all(".modal-dialog").all("table tr")[8].all("td").should(have.exact_texts("Picture", 'pepe.png'))
    browser.all(".modal-dialog").all("table tr")[9].all("td").should(have.exact_texts("Address", "Moscow"))
    browser.all(".modal-dialog").all("table tr")[10].all("td").should(have.exact_texts("State and City", "NCR Gurgaon"))
    browser.element("#closeLargeModal").press_enter()


if __name__ == '__main__':
    test_registration_form()




