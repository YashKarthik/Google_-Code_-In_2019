import os
import sys
import urllib3
import getopt
import argparse
from time import strftime
from bs4 import BeautifulSoup
from sys import platform as _platform

print("\nDownload the NASA Pic of the day\n")

prefix = "http://apod.nasa.gov/apod/"
progress_bar_width = 100
obstacles = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"] # Windows filename problems. Unallowed symbols.
userhome = os.path.expanduser('~')
# username = os.path.split(userhome)[-1]

if _platform == "linux" or _platform == "linux2":
	default_path = userhome + "/Pictures/Nasa_pic_of_the_day/"
elif _platform == "darwin":
	default_path = userhome + "/Pictures/Nasa_pic_of_the_day/"
elif _platform == "win32":
	default_path = userhome + "\\Pictures\\NASA Pic of the day"

def getImage(url, file_name):
	marker = "-"
	try:
		u = urllib3.urlopen(url)
	except HTTPError: #urllib3 throws IOError on 404 Not Found
		sys.stderr.write("Either the webpage is not available or your internet connection doesn't seem to be established :( \n")
		sys.exit(0)
	f = open(file_name,'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print("Downloading: \"%s\" of size %3.2f KB to %s \n" % (file_name, file_size / 1024., os.getcwd()),)

	file_size_dl = 0
	block_sz = 8192 # Download 8KB for each iteration
	while True:
		percent_old = file_size_dl * 100 / file_size # Update progress bar using percent_old and percent_new
		buffer = u.read(block_sz)
		if not buffer:
			break
		file_size_dl += len(buffer)
		f.write(buffer)
		percent_new = file_size_dl * 100 / file_size
		marker = marker + ("-" * (percent_new - percent_old))
		status = r"%4d%% [%s%s]" % (percent_new, marker, " " * (progress_bar_width - len(marker) + 1))
		status = status + (chr(8) * (len(status) + 1)) # Overwrite the status using chr(8)
		print(status)
	print("\nOperations are now complete. :) \n")
	f.close()

def getSoup(url):
	try:
		page = urllib3.urlopen(url).read()
	except IOError: #urllib3 throws IOError on 404 Not Found
		sys.stderr.write("Either the webpage is not available or your internet connection doesn't seem to be established :( \n")
		sys.exit(0)
	soup = BeautifulSoup(page, "html.parser")
	return soup

def getFilename(soup, date=strftime("%d"), month=strftime("%m"), year=strftime("%Y")):
	image_name = soup.find('b').get_text()
	for letter in image_name: # Windows filename problems. Unallowed symbols.
		if letter in obstacles:
			image_name = image_name.replace(letter, "-")
	return date + "-" + month + "-" + year + "-" + image_name +".jpg"

def getArgs(print_help = False):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--path', required = False, default = default_path, help = "download the pic to this directory")
	parser.add_argument('-d', '--day', required = False, help = "download the pic of this day (format: ddmmyyyy)")
	args = parser.parse_args()
	if print_help == True:
		parser.print_help()
		parser.exit()
	return args

def main():
	args = getArgs()

	path = args.path
	try:
		os.chdir(path)
	except:
		sys.stderr.write("Folder not available :( \n")
		sys.exit(0)

	if args.day == None: # Default behaviour. Program running without the --day argument
		print("Downloading today's pic...")
		url = "http://apod.nasa.gov/apod/astropix.html"
		soup = getSoup(url)
		file_name = getFilename(soup)
	else:
		if len(args.day) < 8: # If the day is not in the correct format
			getArgs(True)
		date = args.day[:2]
		month = args.day[2:4]
		year = args.day[4:8]
		print("Downloading the pic of the day " + date + "/" + month + "/" + year + "...")
		url = "http://apod.nasa.gov/apod/ap" + year.replace(year, year[2:]) + month + date + ".html"
		soup = getSoup(url)
		file_name = getFilename(soup, date, month, year)

	# Setup web scraping
	links = soup.find_all("a")
	lobbying = {}
	for element in links:
		lobbying[element.get_text()] = prefix + element["href"]
	for key in lobbying:
		if key == "\n":
			getImage(lobbying[key], file_name)

if __name__ == "__main__":
	sys.exit(main())