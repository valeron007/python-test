#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import Indication as indi

# for user in users:
# 	print(user)

def createDirectoyTasks():
	if not os.path.isdir('./tasks'):
		os.mkdir('./tasks')


if __name__ == "__main__":
	createDirectoyTasks()
	indicator = indi.Indication()
	indicator.creatUsers()
	indicator.CreateIndicators()


