from flask import Flask, request, render_template, jsonify
import xml.etree.ElementTree as ET
import requests
import json


app = Flask(__name__)


@app.route("/alarm", methods=['GET', 'POST'])
def getInfo():
    smartTypeText = ""
    #print("Request Type", request.method)
    if(request.method != "GET"):
        textInput = request.data
        ### print(textInput)
        root = ET.fromstring(textInput)

        for child in root.findall("{http://www.ipc.com/ver10}smartType"):
                smartTypeText = child.text
                print("\n")
                print("INTRUSION ALERT:", smartTypeText)
                print("\n")
            
       #if smartTypeText == "PEA":
            #DoSomething(smartTypeText)

    else:
        print("Do Nothing")
        #DoSomething("Test")
            

    return "<p>BLANK</p>"

def DoSomething(text):
    webhook_url = 'https://webhook.site/b498f8f8-e68b-41a2-8d43-6dedef3f4f60'
    data = { 'smartType': text }
    r = requests.post(webhook_url, data = json.dumps(data), headers = {'Content-Type':'application/json'})

    
@app.route("/test")
def test():
    return "<p>TEST</p>"
