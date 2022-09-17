import os
import time
import requests
import subprocess
import argparse
import colorama
from colorama import Fore

parse = argparse.ArgumentParser()
parse.add_argument("-u", '--user', help="Name User")
args = parse.parse_args()


def funtion_banner():
	try:
		subprocess.run(["cat", "./banner/banner.txt"])
	except OSError:
		print("Error al obtener banner")
pinter = "https://www.pinterest.com/"
face = "https://es-la.facebook.com/public/"
inst = "https://www.instagram.com/"
tw = "https://twitter.com/"
linkedin = "https://cr.linkedin.com/in/"
tik = "https://www.tiktok.com/@"
chtu = "https://chaturbate.com/"
coil = "https://coil.com/u/"
grav = "http://en.gravatar.com/"
ph = "https://pornhub.com/users/"
mine = "https://api.mojang.com/users/profiles/minecraft/"
red = "https://www.reddit.com/user/"
roblox = "https://www.roblox.com/user.aspx?username="
reob = "https://robertsspaceindustries.com/citizens/"
ll = "https://www.tradingview.com/u/"
rw = "https://www.twitch.tv/"
xxx = "https://xvideos.com/profiles/"
forums = "https://forums.whonix.org/u/"
you = "https://youporn.com/uservids/"
hamster = "https://xhamster.com/users/"
fiv = "https://www.fiverr.com/"
fornite = "https://fortnitetracker.com/profile/all/"
guru = "https://gurushots.com/"
isu = "https://issuu.com/"
anime = "https://myanimelist.net/profile/"
trad = "https://www.tradingview.com/u/"
wat = "https://www.wattpad.com/user/"
webs = [pinter, face, inst, tw, linkedin, tik, chtu,
coil, grav, ph, mine, red, roblox, reob, ll, rw, forums,
xxx, you, fiv, fornite, guru, isu, anime, trad, wat]
funtion_banner()
print("Version 1.0.0 | search your profiles")
print("The quieter you are, the more you can hear")
if(args.user):
	for x in webs:
		user = args.user
		res = requests.get(x+user)
		if res.status_code != 404:
			print(f"Found {res.status_code} {x+user}")
		else:
			pass
	print("\nBusqueda finalizada")
else:
	print("Debes especificar el nombre de usuario\nUsa --help para obtener ayuda")
