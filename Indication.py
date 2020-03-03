import requests

from User import User


class Indication:
	"""Class for Indication"""

	USER_URL = 'https://json.medrating.org/users'
	TASKS_URL = 'https://json.medrating.org/todos'

	def __init__(self):
		self.response_users = requests.get(self.USER_URL).json()
		self.response_tasks = requests.get(self.TASKS_URL).json()
		self.users = []

	def creatUsers(self):
		for user in self.response_users:
			self.users.append(User(user, self.response_tasks))

	def CreateIndicators(self):
		for user in self.users:
			user.saveIndicator()


