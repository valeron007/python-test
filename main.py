#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import Indication as indi
import logging
# for user in users:
# 	print(user)

def createDirectoyTasks():
	if not os.path.isdir('./tasks'):
		os.mkdir('./tasks')


if __name__ == "__main__":
	logging.basicConfig(filename='medrating.log', level=logging.INFO)
	createDirectoyTasks()
	indicator = indi.Indication()
	indicator.creatUsers()
	indicator.CreateIndicators()


