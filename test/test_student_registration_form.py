from selene.support.shared import browser
from demoqa_tests.manager import app
from demoqa_tests.student_registration_form import StudentRegistrationForm


def test_registration_form():
    browser.open("/automation-practice-form")

    (app.registration_form
     .set_first_name("Alyona")
     .set_last_name("Tch")
     .set_email("verypyc@gmail.com")
     .set_gender("Female")
     .set_number("9998889988")
     .set_date_birth(1992, 7, 27)
     .set_subjects("Sports")
     .set_hobbies("Reading")
     .set_picture("pepe.png")
     .set_address("Moscow")
     .set_states("NCR")
     .set_cities("Gurgaon")
     .set_submit())




