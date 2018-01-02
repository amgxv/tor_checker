import requests

url_check_tor = "https://check.torproject.org/"

get_status = requests.get(url_check_tor)
text_status = get_status.text

if "Congratulations. This browser is configured to use Tor." in text_status:
	print("Using Tor")
else:
	print("Not Using Tor")
