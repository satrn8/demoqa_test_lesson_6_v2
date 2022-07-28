from selene.support.shared import browser
from demoqa_tests.manager import app


def test_registration_form():
    browser.open("/automation-practice-form")

    (app.registration_form
     .set_first_name("Alyona")
     .set_last_name("Tch")
     .set_email("verypyc@gmail.com")
     .set_gender("Female")
     .set_number("9998889988")
     .set_date_birth(1992, 7, 27)
     .set_subjects("Maths")
     .set_hobbies("Reading")
     .set_picture("pepe.png")
     .set_address("Moscow")
     .set_states("NCR")
     .set_cities("Gurgaon")
     .set_submit())

    app.result_registered_user_dialog.table_row(1, value="Alyona Tch")
    app.result_registered_user_dialog.table_row(2, value="verypyc@gmail.com")
    app.result_registered_user_dialog.table_row(3, value="Female")
    app.result_registered_user_dialog.table_row(4, value="9998889988")
    app.result_registered_user_dialog.table_row(5, value="27 July,1992")
    app.result_registered_user_dialog.table_row(6, value="Maths")
    app.result_registered_user_dialog.table_row(7, value="Reading")
    app.result_registered_user_dialog.table_row(8, value="pepe.png")
    app.result_registered_user_dialog.table_row(9, value="Moscow")
    app.result_registered_user_dialog.table_row(10, value="NCR Gurgaon")




