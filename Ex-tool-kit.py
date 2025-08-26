#!/usr/bin/env python3
# -- coding: utf-8 --

import os
import sys
import time
import socket
import requests
import argparse
import json
import random
from termcolor import colored


class ExToolKit:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64)"
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})

        # 🔑 Store API keys here
        self.api_keys = {
            "numverify": "84a23c87af2e09a3e1bb3a2fc05a10ab",
            "whoisxmlapi": "at_9KhEUQcdxfIiJuh2rIrwlEKiKgb0d",
            "whatcms": "d82adb49f92df5078ea646f71f333537",
            "useragentapi": "d82adb49f92df5078ea646f71f333537"
        }

    def typing_print(self, text, delay=0.002, color="green"):
        """Smooth typing effect"""
        for char in text:
            sys.stdout.write(colored(char, color))
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def glitch_print(self, text, color="red", glitch_chance=0.1):
        """Print text with glitch effect"""
        glitched = ""
        for char in text:
            if random.random() < glitch_chance:
                glitched += random.choice("#$%@*&")
            else:
                glitched += char
        print(colored(glitched, color))

    def hacker_intro(self):
        os.system("cls" if os.name == "nt" else "clear")
        intro_lines = [
            "[*] Initializing Ex Tool Kit...",
            "[*] Loading modules...",
            "[*] Establishing secure connection to darknet...",
            "[*] Deploying exploits...",
            "[*] Access Granted ✔"
        ]
        for line in intro_lines:
            self.typing_print(line, delay=0.03, color="green")
            time.sleep(0.3)
        print("\n" + colored("="*60, "green") + "\n")
        time.sleep(0.5)

    def banner(self):
        logo = """
                            ..............
                     ......',;:cccclllllllllccc;,'......
                ....,;coxOKKKKKKKKKKKKKKKKKKKKKKKKKKOxoc:,....
             ...':oOKKKKKKKK00KKKdlco0KlcKOldKOkK0KKKKKKKK0dc,...
          .'.,ckKKKKKKKKKKl'c,,kx.,::kK'.Ko..o;,Kc.,:0KKKKKKKK0o;.'.
        .'.;xO00KKKKKKKKKK..0k.;Oc::.,K''K;;d..lKd.oKKKKKKKKKKKK0kc.''
        ; kxlcl0KKKKKKKKKKx;,;;kKxlld0KddKoxKo;kK;'0KKKKKKKKKKKdcloK.;.
        ;.xOxdk0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0KKKKKKKKKKKK0xdOK.;
        '.c00000KKKKKKKKKKKOxdddxxxkkkkkkkkkxxxdddkKKKKKKKKKKKKKKKKk.,
        .,.00000KKKKKKkoddxOXWMMMMMMMMMMMMMMMMMMWX0xxdoxKKKKKKKKKKKc..
         ; x00000KOoodOWMMMWMWMMMMX;.',,'.,0MMMMMMWMWMW0dolkKKKKKKK.;.
         .';0000o:dNMMMMMMMMMMMMMN.         0MMMMMMMMMMMMMWxclKKKKx.,
          ;.O00x.WMMMMMMMMMMMMMMMO;,......';dMMMMMMMMMMMMMMMM:oKKK.,.
          .':000'KMMMMMMMMMMMM0c;:codxxxxdol:;:xMMMMMMMMMMMMN.KKKd.,
           ,.k00x,WMMMMMMMMMMMWKccd   ,:   lo,KWMMMMWMWMMMMMMcoKK0.;.
           .,.000:dMWMMMMMMWMWMMNckNKXWMNXXK:KMMMMWMWMMMMMM0,KKK;'.
            ..:000'KMMMMMMMMMMMMWk.xMMMMMM0.dNMMMMMMMMMMMMN'0KKd.,
             '.l00O'XMMMMMMMMMMo    oxO0kd.   cWMMMMMMMMMW;kKKk.,
              ,.o00k,NMMMMMMWKN;    lWocXk    'KXNMMMMMMW;xKKO.,
               ,.o00k,XMMMMd  .:kx   0. X.  oOl.  cMMMMW;xKKk.,.
                '.c00O;OMMN     oc   .. ,   ;k     OWMK;kKKd.,
                 .',O00clWMo.    ...      ...     cWWx:000:.' 
                  .,.d00x;OMWKxl:,..........';ld0WMK:o00k''.
                    '.;k00oc0WMMMMMMMMMMMMMMMMMMMKlcO0O:.,.
                     .,.:O00ockWMMMMMMMMMMMMMMMOclO00l.'.
                       .'.cO00dcl0WMMMMMMMMWKlco000l''.
                         .'.:k00OoclkNMMWOoclO00Oc.'' 
                           .'.,lO000xccccdO00Oo,.'.
                             ..'.,ck0dlcl0Ol,.''.
                                .''.',;:,,.''.
                                   ..''''..

              v3.0 - By cyber23-priyanshu
        """
        self.typing_print(logo, delay=0.0008, color="green")
        print("\n" + colored("="*60, "green") + "\n")

    def help_menu(self):
        self.glitch_print("Usage Examples:", color="yellow")
        print(colored("""
python3 Ex_tool_kit.py -i example.com       # Website Info
python3 Ex_tool_kit.py -n +1234567890       # Phone Info
python3 Ex_tool_kit.py -mx example.com      # MX Records
python3 Ex_tool_kit.py -w example.com       # WHOIS
python3 Ex_tool_kit.py -l example.com       # Location Info
python3 Ex_tool_kit.py -c example.com       # Cloudflare Bypass
python3 Ex_tool_kit.py -a example.com       # Domain Age
python3 Ex_tool_kit.py -ua "Mozilla/5.0"    # User Agent Info
python3 Ex_tool_kit.py -p 127.0.0.1         # Port Scan
python3 Ex_tool_kit.py -b 123456            # BIN Checker
python3 Ex_tool_kit.py -s example.com       # Subdomain Scan
python3 Ex_tool_kit.py -e email@test.com    # Email Check
python3 Ex_tool_kit.py -cms example.com     # CMS Detector
python3 Ex_tool_kit.py -u                   # Update
""", "cyan"))
        print(colored("="*60, "green"))

    # --- keep your original functions (website_info, phone_info, etc) ---


def main():
    parser = argparse.ArgumentParser(description="Ex Tool Kit", add_help=False)
    parser.add_argument("-H", "--help", action="store_true", help="Show help menu")
    parser.add_argument("-i", "--info", help="Website Information")
    parser.add_argument("-n", "--number", help="Phone Number Information")
    parser.add_argument("-mx", "--mx", help="MX Records")
    parser.add_argument("-w", "--whois", help="WHOIS Lookup")
    parser.add_argument("-l", "--location", help="IP/Domain Location")
    parser.add_argument("-c", "--cloudflare", help="Bypass Cloudflare")
    parser.add_argument("-a", "--age", help="Domain Age")
    parser.add_argument("-ua", "--useragent", help="User Agent Info")
    parser.add_argument("-p", "--port", help="Port Scanner")
    parser.add_argument("-b", "--bin", help="BIN Checker")
    parser.add_argument("-s", "--subdomain", help="Subdomain Scanner")
    parser.add_argument("-e", "--email", help="Email Checker")
    parser.add_argument("-cms", "--cms", help="CMS Detector")
    parser.add_argument("-u", "--update", action="store_true", help="Update Tool")

    args = parser.parse_args()
    tool = ExToolKit()

    tool.hacker_intro()
    tool.banner()

    if args.help:
        tool.help_menu()
    elif args.info:
        tool.website_info(args.info)
    elif args.number:
        tool.phone_info(args.number)
    elif args.mx:
        tool.mx_records(args.mx)
    elif args.whois:
        tool.whois_lookup(args.whois)
    elif args.location:
        tool.location_info(args.location)
    elif args.cloudflare:
        tool.cloudflare_bypass(args.cloudflare)
    elif args.age:
        tool.domain_age(args.age)
    elif args.useragent:
        tool.user_agent_info(args.useragent)
    elif args.port:
        tool.port_scanner(args.port)
    elif args.bin:
        tool.bin_checker(args.bin)
    elif args.subdomain:
        tool.subdomain_scanner(args.subdomain)
    elif args.email:
        tool.email_check(args.email)
    elif args.cms:
        tool.cms_check(args.cms)
    elif args.update:
        tool.update()
    else:
        tool.help_menu()


if __name__ == "__main__":
    main()
