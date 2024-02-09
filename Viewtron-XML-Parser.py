from flask import Flask, request, render_template, jsonify
import xml.etree.ElementTree as ET


app = Flask(__name__)


@app.route("/alarm", methods=['GET', 'POST'])
def getInfo():
    print("Request Type", request.method)
    if(request.method != "GET"):
        textInput = request.data
        ### print(textInput)
        root = ET.fromstring(textInput)

        for child in root:
            print("'" + child.tag + "'", child.attrib, child.text)

        print("=======================")

        for child in root:
            if child.tag == 'smartType':
                smartTypeText = child.text
                print(smartTypeText)
                break
        

    return "<p>BLANK</p>"

    
@app.route("/test")
def test():
    return "<p>TEST</p>"
