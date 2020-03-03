import os
from datetime import datetime


class User:
	""" Class for User """

	def __init__(self, user_data, tasks):
		self.complete_tasks = []
		self.unfulfilled_tasks = []
		self.name_company = user_data['company']['name']
		self.user_id = user_data['id']
		self.username = user_data['username']
		self.email = user_data['email']
		self.filename = user_data['username'] + '.txt'

		for task in tasks:
			if task['userId'] == self.user_id:
				title_task = task['title']
				if len(task['title']) > 50:
					title_task = task['title'][0:50] + '...'
				if task['userId'] == self.user_id and task['completed']:
					self.complete_tasks.append(title_task + '\n')
				else:
					self.unfulfilled_tasks.append(title_task + '\n')

	def saveIndicator(self):
		if os.path.isfile('./tasks/' + self.filename):
			os.rename('./tasks/' + self.filename, './tasks/' + self.username + '_' + datetime.now().strftime("%d.%m.%Y %H:%M") + '.txt')

		with open('./tasks/' + self.filename, 'w') as file:
			file.write(self.username + ' <' + self.email + '> ' + datetime.now().strftime("%d.%m.%Y %H:%M") + '\n')
			file.write(self.name_company + '\n')
			file.write('\n')
			file.write('Завершённые задачи:\n')
			file.writelines(self.complete_tasks)
			file.write('\n')
			file.write('Оставшиеся задачи:\n')
			file.writelines(self.unfulfilled_tasks)

