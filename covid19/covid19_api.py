#!/usr/bin/env python3
'''
    covid19_api.py
    Lingyu Wei and Cathy Guang, 16 Oct 2020
    COVID19 Data API.
'''
import sys
import argparse
import flask
import json
import psycopg2
import datetime

from config import password
from config import database
from config import user

app = flask.Flask(__name__)


# Connect to the database
try:
   	connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
   	print(e)
   	exit()

# use to iterate over the rows generated by your query.
try:
    cursor = connection.cursor()
    query = 'SELECT covid19_days.date, covid19_days.state_id, covid19_days.deaths,covid19_days.new_positive_tests,covid19_days.new_negative_tests,covid19_days.new_hospitalizations, states.abbreviation FROM covid19_days, states WHERE covid19_days.state_id = states.id'
    cursor.execute(query)
except Exception as e:
	print(e)
	exit()

state_list = []
for row in cursor:
	if row[6] not in state_list:
		state_list.append(row[6])

data_list = []
for row in cursor:
	data_list.append(row)



@app.route('/')
def hello():
    return 'Hello. Welcome to the COVID19 Data API'


@app.route('/state/<state-abbreviation>/daily')
def state_daily(state_abbreviation):
    ''' Returns a JSON list of dictionaries, each of which represents the COVID-19 statistics from the specified state on a single date. '''

    list_of_daily_stat = []
    state_abbreviation_upper = state_abbreviation.upper()

    for row in data_list:
        if row[-1] == state_abbreviation_upper:
            state_daily_stat_dict = {}
            state_daily_stat_dict["date"] = row[0].strftime("%Y-%m-%d")
            state_daily_stat_dict["state"] = row[6]
            state_daily_stat_dict["deaths"] = row[2]
            state_daily_stat_dict["positive"] = row[3]
            state_daily_stat_dict["negative"] = row[4]
            state_daily_stat_dict["hospitalizations"] = row[5]

        list_of_daily_stat.append(state_daily_stat_dict)
    print(state_daily_stat_dict)
    return json.dumps(list_of_daily_stat)


@app.route('/state/<state-abbreviation>/cumulative')
def state_cumulative(state_abbreviation):
    ''' Returns a single JSON dictionary representing the cumulative statistics for the specified state.
    '''
    state_abbreviation_upper = state-abbreviation.upper()
    state_cumulative_data_dict = {}

    for row in data_list:
        if row[-1] == state_abbreviation_upper:
            for i in range(2,6):
                if row[i] == None:
                    row[i] = 0
            death_sum += row[2]
            positive_sum += row[3]
            negative_sum += row[4]
            hospitalizations_sum += row[5]

    state_cumulative_data_dict["start_date"] = '2020-1-20'
    state_cumulative_data_dict["end_date"] = '2020-10-13'
    state_cumulative_data_dict["state"] = state_abbreviation_upper
    state_cumulative_data_dict["death"] = death_sum
    state_cumulative_data_dict["positive"] = positive_sum
    state_cumulative_data_dict["negative"] = negative_sum
    state_cumulative_data_dict["hospitalizations"] = hospitalizations_sum

    return json.dumps(state_cumulative_data_dict)


@app.route('/states/cumulative?sort=[deaths|cases|hospitalizations]')
def all_state_cumulative():
    ''' Returns a JSON list of dictionaries, each representing the
	cumulative COVID-19 statistics for each state. The dictionaries are
	sorted in decreasing order of deaths, cases (i.e. positive tests), or hospitalizations, depending on the value of the GET parameter "sort". If sort is not present, then the list will be sorted by deaths. '''
    list_of_cumulative_stat = []

    for state in state_list:
        state_cumulative_data_dict = {}
        for row in data_list:
            if row[-1] == state:
                for i in range(2,6):
                    if row[i] == None:
                        row[i] = 0

                death_sum += row[2]
                positive_sum += row[3]
                negative_sum += row[4]
                hospitalizations_sum += row[5]
                state_cumulative_data_dict["start_date"] = '2020-1-20'
                state_cumulative_data_dict["end_date"] = '2020-10-13'
                state_cumulative_data_dict["state"] = state_abbreviation_upper
                state_cumulative_data_dict["death"] = death_sum
                state_cumulative_data_dict["positive"] = positive_sum
                state_cumulative_data_dict["negative"] = negative_sum
                state_cumulative_data_dict["hospitalizations"] = hospitalizations_sum
        list_of_cumulative_stat.append(state_cumulative_data_dict)
    sort_order = flask.request.args.get('sort', default=death, type=string)
    if (sort_order == "death"):
        sorted_list = sorted(list_of_cumulative_stat,
                           key=lambda i: i['death'], reverse=True)
    if (sort_order == "cases"):
        sorted_list = sorted(list_of_cumulative_stat,
                           key=lambda i: i['cases'], reverse=True)
    if (sort_order == "hospitalizations"):
        sorted_list = sorted(list_of_cumulative_stat,
                           key=lambda i: i['hospitalizations'], reverse=True)
    return json.dumps(sorted_list)


@app.route('/help')
def get_help():
    help_message = ''
    with flask.current_app.open_resource('static/help.html', 'r') as f:
        help_message = f.read()
    return help_message

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Covid 19 data history/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

connection.close()
