from selene import command
from selene.core.entity import Element


class DatePicker:
    def __int__(self, element: Element):
        self.element = element

    def select_day(self, option: int):
        self.element.element(f".react-datepicker__day--0{option}").click()

    def select_month(self, option: int):
        self.element.element(f'[value="{option.value}"]').click()

    def select_year(self, option: int):
        self.element.element(f'[value="{option}"]')
