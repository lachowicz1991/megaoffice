from dataclasses import dataclass, field
from employee import Employee
import json
import re
# from custom_exception import Input_Exception

@dataclass()
class ResourceManager:
	employee_list: dict = field(default_factory=dict)

	def menu(self):
		print('Menu:')
		print('1 : Show data about employee')
		print('2 : Add new employee')
		print('3 : Remove employee')
		print('4 : Add or remove employee hours')
		print('5 : Save changes into the file')
		print('6 : Load data from the file')
		print('7 : Check employee salary')
		print('0 : Exit program')

	def controls(self):
		switch = {
			"1": self.search_employee,
			"2": self.add_employee,
			"3": self.remove_employee,
			"4": self.change_hours,
			"5": self.save_data,
			"6": self.load_data,
			"7": self.check_salary,
			"x": self.quit,
		}

		choice = input("Wybierz jedną opcję:\n=> ")
		if choice in switch.keys():
			switch[choice]()
		else:
			print("Niepoprawny wybór!")


	def load_data(self):
		file_name = input('Please enter the name of the file that you would like to load:')
		file_name_formated = f'{file_name}.json'
		with open(file_name_formated, 'r') as f:
			loaded_data = json.load(f)
			for keys, values in loaded_data.items():
				import_user = []
				for data in values.values():
					import_user.append(data)
				loaded_employee = Employee(import_user[0], import_user[1], import_user[2], import_user[3],
										   import_user[4])
				self.employee_list[keys] = loaded_employee


	def save_data(self):
		file_name = input('Please enter the save name for a file:')
		file_name_formated = f'{file_name}.json'
		kuma={}
		for x, y in self.employee_list.items():
			kuma[x] = y.__dict__
		with open(file_name_formated, 'w') as f:
			json.dump(kuma, f)

	def change_hours(self):
		for e in self.employee_list:
			print(f'Employee id:{e}')

		employee_id = input("Enter employee's ID before adding or removing worked hours:")
		if employee_id in self.employee_list.keys():
			choice = input(f'Employee {employee_id} found in database. Would you like to add or remove its hours(remove/add)?')
			if choice == 'add':
				hours = int(input("Enter how many hours you want to add:"))
				self.employee_list[employee_id].add_hours(hours)
			elif choice == 'remove':
				hours = int(input("Enter how many hours you want to remove:"))
				self.employee_list[employee_id].remove_hours(hours)
		else:
			print('Employee not found')

	def check_salary(self):
		for e in self.employee_list:
			print(f'Employee id:{e}')

		employee_id = input("Enter employee's ID to check salary:")
		self.employee_list[employee_id].calculate_salary()

	def search_employee(self):
		print(self.employee_list)
		for e in self.employee_list:
			print(f'Employee id:{e}')

		employee_id = input("Enter employee's ID before adding or removing worked hours:")
		if employee_id in self.employee_list.keys():
			print(employee_id)
			print(self.employee_list[employee_id])
		else:
			print('Employee not found')


	def add_employee(self):
		try:
			name = input("Please enter employee's first name:")
			check = r"^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
			if re.match(check, name):
				pass
			else:
				print('Wrong format or incorrect input, try again!')
				raise ValueError
			surname = input("Please enter employee's second name:")
			check = r"^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
			if re.match(check, surname):
				pass
			else:
				print('Wrong format or incorrect input, try again!')
				raise ValueError
			number = input("Please enter employee's contact number(xxx-xxx-xxxx):")
			check = r'\w{3}-\w{3}-\w{4}'
			if re.match(check, number):
				pass
			else:
				print('Wrong format or incorrect input, try again!')
				raise ValueError
			email = input("Please enter employee's email:")
			check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
			if re.fullmatch(check, email):
				pass
			else:
				print('Wrong format or incorrect input, try again!')
				raise ValueError
			dob = input("Please enter date of birth(dd-mm-yyyy):")
			check = r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$'
			if re.fullmatch(check, dob):
				pass
			else:
				print('Wrong format or incorrect input, try again!')
				raise ValueError
			personal_details = {'Name': name, 'Surname': surname, 'Number': number, 'Email': email, 'Date of birth': dob}
			contracted_hours = float(input('Set monthly contracted hours for the employee:'))
			hourly_rate = float(input('Please set the rate for the employee ($):'))
			employee_data = Employee(contracted_hours, hourly_rate, personal_details=personal_details)
			employee_id = f'{name} {surname}'
			self.employee_list[employee_id] = employee_data
		except ValueError:
			print('Incorrect input please try again!')


	def remove_employee(self):
		try:
			print('Which employee would you like to remove?')
			for e in self.employee_list:
				print(f'Employee id:{e}')
			remove = input('Enter id of employee to be removed:')
			del self.employee_list[remove]
			print(f'{remove} was removed from the database, below remaining employees:')
			for e in self.employee_list:
				print(f'Employee id:{e}')
		except:
			print('')

	def quit(self):
		x = False

#
# testing = ResourceManager()
# testing.add_employee()
# testing.add_employee()
#
# testing.remove_employee()