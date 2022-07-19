from selene import command
from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_day(self, option: int):
        self.element.element(f'.react-datepicker__day--0{option}').click()

    def select_month(self, option: int):
        self.element.element(f'[value="{option.value}"]').click()
        return self

    def select_year(self, option: int):
        self.element.element(f'[value="{option}"]').click()
        return self





    def set_date(self, calendar: Element, option: str):
        browser.execute_script()
        browser.element(calendar).set_value(option).click()