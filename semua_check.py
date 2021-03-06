#!/usr/bin/env python3

import os
import sys
import shutil
import socket

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

def check_root_full():
	"""return True if the root partition is full, False otherwise."""
	return check_disk_full(disk='/', min_gb=2, min_percent=10)

def check_no_network():
	"""return True if it fails to sesolve google's URL, False otherwise"""
	try:
		socket.gethostbyname('www.google.com')
		return False
	except:
		return True

def main():
	checks=[
		(check_reboot, "pending reboot"),
		(check_root_full, "root partition full"),
		(check_no_network, "no working network"),
	]
	everything_ok=True
	for check,msg in checks:
		if check():
			print(msg)
			everything_ok=False
	if not everything_ok:
		sys.exit(1)
	
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if check_root_full():
		print('Disk partition full.')
		sys.exit(1)
	print('Everything is ok')
	sys.exit(0)
main()
