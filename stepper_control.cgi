#!/usr/bin/python37all
import cgi
import json
from urllib.request import urlopen
from urllib.parse import urlencode

# parse the data into json format
data = cgi.FieldStorage()
output = {}
submitType = data.getvalue('action')
if submitType == "Change Stepper Motor Angle":
  inputAngle = data.getvalue('slider')
  output['action'] = "change angle"
  output['angle'] = int(inputAngle)
else:
  output['action'] = "zero"

with open('lab5.txt', 'w') as f:
  json.dump(output,f)

# output data to thingspeak
"""
api = "JQIJM76POJAMNCL1"
params = {1:output["angle"],
          "api_key":api}
params = urlencode(params)
url = "https://api.thingspeak.com/update?" + params
response = urlopen(url)
#print(response.status, response.reason)
"""

# html page format
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Lab 5 - Stepper Control</title>')
print('</head>')
print('<body>')
print('<div style="width:600px;background:#ADD8E6;border:2px;text-align:center">')
print('<br>')
print('<font size="3" color="black" face="helvetica">')
print('<b>')
print('<h4> Use the slider to adjust the angle </h4>')
print('</b>')
print('</font>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('<font size="2" color="black" face="helvetica">') 
print('<input type="range" name="slider" min ="0" max="360" value="0"/>')
print('<br>')
print("Current Angle: %f" % inputAngle)
print('<br>')
print('<br>')
print('<input type="submit" name="action" value="Change Stepper Motor Angle"/>')
print('<input type="submit" name="action" value="Zero Stepper Motor Angle"/>')
print('</form>')
print('<br>')
print('<br>')
print('<iframe width="450" height="260" 
    style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550866/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs+Time&type=line&xaxis=Time&yaxis=Motor+Angle">')
print('</iframe>')
print('<br>')
print('<br>')
print('<iframe width="450" height="260" 
    style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550866/widgets/373037">')
print('</iframe>')
print('</body>')   
print('</html>')


