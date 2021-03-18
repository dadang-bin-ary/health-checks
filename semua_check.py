#!/usr/bin/env python3

import os
import sys
import shutil

def check_reboot():
	"""Returns True if the computer has a pending reboot"""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	"""return True if there isn't enough space, False otherwise."""
	du = shutil.disk_usage(disk)
	# calculte the percentage of free space
	percent_free = 100 * du.free / du.total
	# calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or  gigabytes_free < min_gb:
		return True
	return False

def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if check_disk_full(disk='/', min_gb=2, min_percent=10):
		print('Disk Full.')
		print('ahihihihihihi')
		sys.exit(1)
	print('Everything is ok')
	sys.exit(0)
main()
