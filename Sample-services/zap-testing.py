#!/usr/bin/env python
import time
import datetime
import os
import requests
from pprint import pprint
from pprint import pprint
from zapv2 import ZAPv2 
from zapv2 import ZAPv2 as ZAP
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# The URL of the application to be tested
target = 'http://localhost:5074/hello'
# Change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = '1irjjncg7itnjut55dfgd2bc33'

firefox_options = FirefoxOptions()
firefox_options.headless = True

# By default ZAP API client will connect to port 8080
# zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Spidering target {}'.format(target))
# The scan returns a scan id to support concurrent scanning
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

print('Spider has completed!')
# Prints the URLs the spider has crawled
print('\n'.join(map(str, zap.spider.results(scanID))))
# If required post process the spider results

# TODO: Explore the Application more with Ajax Spider or Start scanning the application for vulnerabilities

print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)
# If required perform additional operations with the Ajax Spider results

# TODO: Start scanning the application to find vulnerabilities
print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(25)

print('Active Scan completed')
# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))

###########
alerts = zap.core.alerts(baseurl=target)
print('Alerts: ')
pprint(alerts)

with open("zap-alerts.txt", "w") as f:
    f.write("Alerts:\n")
    for alert in alerts:
        f.write(str(alert) + "\n")


# Shut down ZAP
zap.core.shutdown()