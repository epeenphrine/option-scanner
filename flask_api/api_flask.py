from flask import Flask, request, render_template, jsonify
from option_scripts.filter_json import *
from flask_cors import CORS
import json


#from callie_scripts.make_options_req import MakeRequest 
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    message = "" 
    return "home"


@app.route('/rawData', methods=['GET'])
def raw_data():
    if request.method == 'GET':
        with open('/tmp/json/optionChainsListLong.json', 'r') as f:
            raw_dat = json.load(f)
            return jsonify(raw_dat)

#example : yourip:5000/api/callieSpreads?days=20&goldenRatio=.7&volume=50
@app.route('/callieSpreads', methods=['GET'])
def callie_spreads():
    if request.method == 'GET':
        days = request.args.get('days', 14, int)
        goldenRatio = request.args.get('goldenRatio', .65,type=float)
        totalVolume = request.args.get('totalVolume', 500,  type=int)
        openInterest = request.args.get('openInterest', 1000, type=int)
        option_filter = get_callies(
            date_delta=days,
            goldenRatio=goldenRatio,
            totalVolume=totalVolume, 
            openInterest=openInterest,
            )
        data = option_filter
        return jsonify(data) 

@app.route('/callieSpreadsLong', methods=['GET'])
def callie_spreads_long():
    if request.method == 'GET':
        days = request.args.get('days', 14, int)
        goldenRatio = request.args.get('goldenRatio', .65,type=float)
        totalVolume = request.args.get('totalVolume', 500,  type=int)
        openInterest = request.args.get('openInterest', 1000, type=int)
        option_filter = get_callies_long(
            date_delta=days,
            goldenRatio=goldenRatio,
            totalVolume=totalVolume, 
            openInterest=openInterest,
            )
        data = option_filter
        return jsonify(data) 

@app.route('/bigTrades', methods=['GET'])
def big_trades():
    if request.method == "GET":
        ratio = request.args.get('ratio', 4,type=float)
        volume = request.args.get('volume', 1000,  type=int)
        open_interest = request.args.get('openInterest', 1000, type=int)
        option_filter = get_big_trades(
            ratio_user=ratio, 
            volume_user=volume,
            open_interest_user= open_interest,
            )
        data = option_filter
        return jsonify(data) 
    pass
@app.route('/options/rawData', methods=['GET'])
def rawData():
    if request.method == "GET":
        with open('/tmp/json/optionsChainsList.json', 'r') as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/earningsThisWeek')
def earningsThisWeek():
    if request.method =="GET":
        with open('/tmp/json/companies_earnings.json') as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/earnings')
def earningsThisWeek():
    if request.method =="GET":
        with open('/tmp/json/companies_earnings.json') as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/ipo/thisWeek', methods=['GET'])
def ipoThisWeek():
    if request.method == "GET":
        with open("/tmp/json/upcoming_ipos.json", "r") as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/ipo/nextWeek', methods=['GET'])
def ipoNextWeek():
    if request.method == "GET":
        with open("/tmp/json/next_week.json", "r") as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
