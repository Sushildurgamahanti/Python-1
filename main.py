from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'DataEngineer',
  'location': 'Delhi India',
  'salary': 'Rs. 50000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Pune India',
  'salary': 'Rs. 40000'
}, {
  'id': 3,
  'title': 'DBA',
  'location': 'Chennai India',
  'salary': 'Rs. 20000'
}, {
  'id': 4,
  'title': 'Admin',
  'location': 'Hyderabad India',
  
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Trinipi')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
