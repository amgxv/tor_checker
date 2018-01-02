import requests
from cowpy import cow

url_check_tor = "https://check.torproject.org/"

get_status = requests.get(url_check_tor)
text_status = get_status.text

cowsatan = cow.Satanic()
cowmutil = cow.Mutilated()
using_tor = cowsatan.milk("You're Using Tor")
not_using_tor = cowmutil.milk("You're Not Using Tor")

if "Congratulations. This browser is configured to use Tor." in text_status:
	print(using_tor)
else:
	print(not_using_tor)
