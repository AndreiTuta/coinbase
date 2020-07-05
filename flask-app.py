from flask import Flask, Response, request

import datetime
from cb import generate_stats

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1> Hello World </h1>"

  """
  - now req param means making an API call to get current data

  Returns:
      [type]: [description]
  """
@app.route("/get-result-csv/<date_csv>", methods=['GET'])
def getPlotCSV(date_csv):
    now = bool(request.args.get('now'))
    if(now):
          return Response(
      str(now),
      mimetype="text/csv")
    else:               
        filepath = './results/result' + str(date_csv) + '.csv'
        with open(filepath) as fp:
          csv = fp.read()
        return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                  "attachment; filename=results.csv"})

if __name__ =="__main__":
  app.run(debug=True,port=8080) 
