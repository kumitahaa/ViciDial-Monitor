# routes.py

from flask import jsonify, render_template
from app import app
from app.utils import fetch_real_time_data, fetch_agent_stat_report, fetch_list_report,fetch_logged_agents

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/real_time_data')
def real_time_data():
    return jsonify(fetch_real_time_data())

@app.route('/logged_agents_data')
def logged_in_agents():
    return jsonify(fetch_logged_agents())


@app.route('/agent_stat_report/<agent_id>/<a>/<b>')
def agent_stat_report(agent_id,a,b):
    return jsonify(fetch_agent_stat_report(agent_id,a,b))

@app.route('/list/<list_id>')
def list_report(list_id):
    return jsonify(fetch_list_report(list_id))

@app.route('/real_time')
def data():
    return render_template('real_time.html')

@app.route('/logged_agents')
def logged_agents():
    return render_template('login_agents.html')

@app.route('/agent_data')
def agent_data():
    return render_template('agent_data.html')


@app.route('/list_data')
def list_data():
    return render_template('list_data.html')
