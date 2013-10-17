#! /usr/bin/env python
#python version of the ls command using subprocess system calls

import subprocess

function hd_func ():
	subprocess.call(["df"])

function loc_func ():
	subprocess.call(["pwd"])

function main ():
	print("determining hard drive space......")
	hd_func()
	print("determining your location in the computer.......")
	print("your location is:")
	loc_func()

if __name__ == "__main__":
	main()
