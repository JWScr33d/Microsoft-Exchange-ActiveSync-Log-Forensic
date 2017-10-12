#!/usr/bin/env python
# -*- coding: utf-8 -*

import urllib2, sys, time, os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

#AUTHOR JORGE CORONADO
#TWITTER @JORGEWEBSEC
#WEB BLOG.QUANTIKA14.COM

c = 0

def ip_location(ipo):
	try:
		print "[LOCATION]"
		html = urllib2.urlopen("https://geoiptool.com/es/?ip="+ipo+"+").read()
		soup = BeautifulSoup(html, "html.parser")
		soup = soup.find("div",{"class":"sidebar-data hidden-xs hidden-sm"})
		divs = soup.findAll("div",{"class":"data-item"})
		for div in divs:
			if "País" in div.text:
				print div.text.split(":")[1].strip()
				pais = div.text.split(":")[1].strip()
			if "Region" in div.text:
				print div.text.split(":")[1].strip()
				region = div.text.split(":")[1].strip()
			if "Ciudad" in div.text:
				print div.text.split(":")[1].strip()
				ciudad = div.text.split(":")[1].strip()
			if "Latitud" in div.text:
				print div.text.split(":")[1].strip()
				latitud = div.text.split(":")[1].strip()
			elif "Longitud" in div.text:
				print div.text.split(":")[1].strip()
				longitud = div.text.split(":")[1].strip()
	except:
		print "[LOCATION][>] Geo-ip ban ip"
		html = urllib2.urlopen("http://www.geoiptool.net/index.php?ip="+ipo).read()
		soup = BeautifulSoup(html, "html.parser")
		soup = soup.find("div",{"id":"ip-results"})
		tds = soup.findAll("td")
		for td in range(len(tds)):
			if "Country" in tds[td]:
				print tds[td+1].text
				pais = tds[td+1].text
			if "Region" in tds[td]:
				region = "Region nº "+tds[td+1].text
				print region
			if "City" in tds[td]:
				print tds[td+1].text
				ciudad = tds[td+1].text
			if "Longitude" in tds[td]:
				print tds[td+1].text
				longitud = tds[td+1].text
			if "Latitude" in tds[td]:
				print tds[td+1].text
				latitud = tds[td+1].text

		print "------------------------------------------"
		time.sleep(2)


def _filter_date_did(date, did, f):
	global c
	lineas = f.readlines()
	for linea in lineas:
		cas = linea.split(" ")
		if did in linea and date in linea:
			c += 1
			ip_address = cas[8]
			info = cas[0]
			id_device = cas[3]
			device = cas[9]
			hour = cas[1]
			to_print(info, hour, ip_address, device, id_device)

def _filter_date(date, f):
	global c
	lineas = f.readlines()
	for linea in lineas:
		cas = linea.split(" ")
		if date in cas[0]:
			c += 1
			ip_address = cas[8]
			info = cas[0]
			id_device = cas[3]
			device = cas[9]
			hour = cas[1]
			to_print(info, hour, ip_address, device, id_device)

def _filter_device(device, f):
	global c
	lineas = f.readlines()
	for linea in lineas:
		cas = linea.split(" ")
		if device in cas[9]:
			c += 1
			ip_address = cas[8]
			info = cas[0]
			id_device = cas[3]
			device = cas[9]
			hour = cas[1]
			to_print(info, hour, ip_address, device, id_device)

def _filter_deviceID(DID, f):
	global c
	lineas = f.readlines()
	for linea in lineas:
		cas = linea.split(" ")
		if DID in cas[3]:
			c += 1
			ip_address = cas[8]
			info = cas[0]
			id_device = cas[3]
			device = cas[9]
			hour = cas[1]
			to_print(info, hour, ip_address, device, id_device)

def to_print(date, hour, ip_address, device, id_device):
	print ""
	print "[INFO] Connect Nº: " + str(c)
	print "[DATE]" + date + "[HOUR] " + hour
	print "-----------------------------------------"
	print "[+][IP] " + ip_address
	print "[+][Device] " + device
	print "[+][Device_ID] " + id_device
	print ip_location(ip_address)

def main():
	menu()

def get_hash(arch):
	print "[HASH][SHA512] " + arch
	print os.system('sha512sum ' + arch)

def menu():
	print "***** Microsoft Exchange ActiveSync Log Forensic *****"
	print "*****                 MEALF.py                   *****"
	print "Author: Jorge Coronado | Twitter: @JorgeWebsec"
	print "Web: blog.quantika14.com | Twitter: @QuantiKa14"
	arch = str(raw_input("Insert file: "))
	get_hash(arch)
	f = open(arch, "r")
	print "-----------------------------------------"
	print "-- 1. Date + Device_ID.................--"
	print "-- 2. Only Date........................--"
	print "-- 3. Only Device......................--"
	print "-- 4. Only Device_ID...................--"
	print "-----------------------------------------"
	m = int(raw_input("Select: "))
	if m == 1:
		print "ejm: 2106-07-10"
		print "YYYY-MM-DD"
		date = str(raw_input("Insert date: "))
		DID = str(raw_input("Insert Device_ID: "))
		_filter_date_did(date, DID, f)
	elif m == 2:
		print "ejm: 2106-07-10"
		print "YYYY-MM-DD"
		date = str(raw_input("Insert date: "))
		_filter_date(date, f)
	elif m == 3:
		device = str(raw_input("Insert Device: "))
		_filter_device(device, f)
	elif m == 4:
		DID = str(raw_input("Insert Device_ID: "))
		_filter_deviceID(DID, f)
	elif m > 4 or m < 1:
		print "[WARNING] ERROR insert 1,2,3,4"
	else:
		print "[WARNING] ERROR insert 1,2,3,4"
	f.close()
	print "Total connection: " + str(c)

if __name__ == '__main__':
	main()
