import argparse
import os, sys
import logging
from crontab import CronTab


class CronManager:


	def __init__(self):
		self.cron = CronTab(user=True)


	def daily(self, name, user, command, environment=None):
		cron_job = self.cron.new(command=command, user=user)
		cron_job.minute.on(0)
		cron_job.hour.on(0)
		cron_job.enable.on(0)
		cron_job.write.on(0)
		if self.cron.render():
			return True