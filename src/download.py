id = "takadahiroyuki0929"
pw = ""

import urllib3
import datetime as dt
http = urllib3.PoolManager()
# url = "https://csvex.com/kabu.plus/csv/japan-all-stock-prices/daily/japan-all-stock-prices.csv"
start = dt.date(2021,1,4)
yyyymmdd = '{0:%Y%m%d}'.format(start)
url = "https://csvex.com/kabu.plus/csv/japan-all-stock-prices/daily/japan-all-stock-prices_" + yyyymmdd + ".csv"
print(url)
headers = urllib3.util.make_headers(basic_auth="%s:%s" % (id, pw) )
response = http.request("GET", url, headers=headers)
if response.status == 200:
    f = open("../data/japan-all-stock-prices_" + yyyymmdd + ".csv", "wb")
    print("../data/japan-all-stock-prices_" + yyyymmdd + ".csv")
    f.write(response.data)
    f.close()
#
# url = "https://csvex.com/kabu.plus/json/japan-all-stock-prices/daily/japan-all-stock-prices.json"
# headers = urllib3.util.make_headers(basic_auth="%s:%s" % (id, pw) )
# response = http.request("GET", url, headers=headers)
# f = open("japan-all-stock-prices.json", "wb")
# f.write(response.data)
# f.close()
#
