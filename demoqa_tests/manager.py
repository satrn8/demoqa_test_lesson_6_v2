from demoqa_tests.student_registration_form import StudentRegistrationForm
from demoqa_tests.controls.table import Table


class Application_manager:
    result_registered_user_dialog = Table
    registration_form = StudentRegistrationForm()


app = Application_manager