#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)

# this file must do two things:
	# 1. it must set DJANGO_SETTINGS_MODULE environment variable.
	#2. it must call Django's execute_from_command_line function.

