#MrNoobking
#Team : PlXwFreeTeamHyberN
import time
import requests, re , colorama
colorama.init()

print("[=====         ]    1%")
time.sleep(2)
print("[=========     ]    30%")
time.sleep(2)
print("[============= ]    90%")
time.sleep(3)
print("[==============]    100")
time.sleep(2)

print("""
\033[1;35m ▄████▄   ▄████▄  ▄▄▄█████▓ ██▒   █▓    ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
\033[1;31m ▒██▀ ▀█  ▒██▀ ▀█  ▓  ██▒ ▓▒▓██░   █▒   ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
\033[1;34m▒▓█    ▄ ▒▓█    ▄ ▒ ▓██░ ▒░ ▓██  █▒░   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
\033[1;33m▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒░ ▓██▓ ░   ▒██ █░░   ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
\033[1;35m▒ ▓███▀ ░▒ ▓███▀ ░  ▒██▒ ░    ▒▀█░     ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
\033[1;31m░ ░▒ ▒  ░░ ░▒ ▒  ░  ▒ ░░      ░ ▐░      ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
\033[1;32m░ ▒     ░  ▒       ░       ░ ░░      ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
\033[1;34m░        ░          ░           ░░      ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
\033[1;31m░ ░      ░ ░                     ░      ░  ░  ░      ░  ░░ ░      ░  ░   
\033[1;36m░        ░                      ░                        ░               

\033[1;32m1) \033[1;36mIndonesia 
\033[1;35m2) \033[1;35mUnited Kingdom
\033[1;36m3) \033[1;34mMalaysia
\033[1;31m4) \033[1;32mSingapore
\033[1;33m5) \033[1;32mUnited States
\033[1;35m6) \033[1;31mIsrael
\033[1;34m7) \033[1;33mJapan
\033[1;33m8) \033[1;36mCanada
""")


try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                  "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 91+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
             headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;34m", ip)
except:
    pass
finally:
    print("\033[1;34m")
    exit()