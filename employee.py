from dataclasses import dataclass, field


@dataclass()
class Employee:
	contracted_hours: float
	hourly_rate: float
	hours_worked: float = 0
	expected_salary: float = 0
	personal_details: dict = field(default_factory=list)

	def remove_hours(self, remove):
		self.hours_worked = self.hours_worked - remove
		return self.hours_worked


	def add_hours(self, add):
		self.hours_worked = self.hours_worked + add
		return self.hours_worked

	def calculate_salary(self):
		self.expected_salary = self.hours_worked * self.hourly_rate
		print(f'Employee salary = ${self.expected_salary}')
		return self.expected_salary
#
# test_emp = Employee(100,10,0,0)
#
# test_emp.add_hours(10)

