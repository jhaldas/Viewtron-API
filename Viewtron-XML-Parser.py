from flask import Flask, request, render_template, jsonify
import xml.etree.ElementTree as ET


app = Flask(__name__)


@app.route("/alarm", methods=['GET', 'POST'])
def getInfo():
    smartTypeText = ""
    print("Request Type", request.method)
    if(request.method != "GET"):
        textInput = request.data
        ### print(textInput)
        root = ET.fromstring(textInput)

        for child in root.findall("{http://www.ipc.com/ver10}smartType"):
                smartTypeText = child.text
                print(smartTypeText)
            
        if smartTypeText == "PEA":
            print("Do Something")
        else:
            print("Do Nothing")
            

    return "<p>BLANK</p>"

    
@app.route("/test")
def test():
    return "<p>TEST</p>"
