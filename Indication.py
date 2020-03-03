import requests

from User import User

import sys
import logging
class Indication:
	"""Class for Indication"""

	USER_URL = 'https://json.medrating.org/users'
	TASKS_URL = 'https://json.medrating.org/todos'

	def __init__(self):
		"""
			Можно было перехватить все исключения указав Exception, но
			тут показано из-за чего возможны проблемы
		"""
		try:
			self.response_users = requests.get(self.USER_URL).json()
			self.response_tasks = requests.get(self.TASKS_URL).json()
		except requests.ConnectionError:
			logging.debug("Connection Error:отсутствует соединение")
			sys.exit(1)
		except requests.Timeout:
			logging.debug("Oops. Connection timeout")
			sys.exit(1)
		except requests.HTTPError as httpErrors:
			logging.debug("Timeout Error: {content}").format(content=httpErrors)
			sys.exit(1)

		self.users = []

	def creatUsers(self):
		for user in self.response_users:
			self.users.append(User(user, self.response_tasks))

	def CreateIndicators(self):
		for user in self.users:
			user.saveIndicator()


