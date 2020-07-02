from flask import Flask, Response

import datetime
from cb import generate_stats

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1> Hello World </h1>"


@app.route("/get-result-csv")
def getPlotCSV():
    current = datetime.datetime.now()
    csv = generate_stats(None, current)
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})

if __name__ =="__main__":
  app.run(debug=True,port=8080) 
