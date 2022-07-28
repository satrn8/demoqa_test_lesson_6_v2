from demoqa_tests.student_registration_form import StudentRegistrationForm
from demoqa_tests.controls.table import Table


class Manager:
    result_registered_user_dialog = Table
    registration_form = StudentRegistrationForm()


app = Manager