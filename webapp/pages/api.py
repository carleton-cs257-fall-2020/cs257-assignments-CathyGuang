'''
    formula1_webapp.py
    Lingyu Wei and Cathy Guang

    Tiny Flask API to support the tiny Formula one web application.
    CS 257
'''
import sys
import flask
import json
import config
import psycopg2
import datetime
import operator

from config import password
from config import database
from config import user

api = flask.Blueprint('api', __name__)

# Connect to the database
try:
   	connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
   	print(e)
   	exit()


# try:
#     cursor_race_with_circuit = connection.cursor()
#     query = '''SELECT races.id, races.year, races.round, races.circuitID, races.name, 
#     races.date, races.url, circuits.id, circuits.name, circuits.location, circuits.country, circuits.url 
#     FROM races, circuits 
#     WHERE races.circuitID = circuits.id'''
#     cursor_race_with_circuit.execute(query)
# except Exception as e:
# 	print(e)
# 	exit()

# race_with_circuit_list = []
# for row in cursor_race_with_circuit:
# 	race_with_circuit_list.append(row)

# # return 20th or 21st century races info
# @api.route('/race/<century>')
# def get_country_races(century):
#     list_of_20_races = []
#     list_of_21_races = []

#     for row in race_with_circuit_list:
#         race_dict = {}

#         race_dict["Name"] = row[4]
#         race_dict["Date"] = row[5].strftime("%Y-%m-%d")
#         race_dict["Country"] = row[10]
#         race_dict["Location"] = row[9]
#         race_dict["Circuit"] = row[8]
#         race_dict["URL"] = row[6]

#         if row[1] < 2000:
#             list_of_20_races.append(race_dict)
#         elif row[1] >= 2000:
#             list_of_21_races.append(race_dict)

#     if int(century) == 20:
#         return json.dumps(list_of_20_races)
#     elif int(century) == 21:
#         return json.dumps(list_of_21_races)

# @api.route('/race?country={country_name}')
# def get_country_races(country_name):
#     list_of_races = []
#     for row in race_with_circuit_list:
#         if row[9] == country_name:
#             race_dict = {}
#             race_dict["Name"] = row[4]
#             race_dict["Date"] = row[5]
#             race_dict["Country"] = row[9]
#             race_dict["Circuit"] = row[7]
#             race_dict["URL"] = row[6]

#             list_of_races.append(race_dict)

#     return json.dumps(list_of_races)

# on the home page: click on a country on the map, return a JSON list of drivers from that country
try:
    cursor_driver = connection.cursor()
    query = '''SELECT drivers.id, drivers.forename, drivers.surname, drivers.dob, drivers.nationality, drivers.url 
    FROM drivers'''
    cursor_driver.execute(query)
except Exception as e:
	print(e)
	exit()

driver_list = []
for row in cursor_driver:
	driver_list.append(row)

# @api.route('/driver?country={country_name}')
# def get_country_drivers(country_name):
#     list_of_drivers = []
#     for row in driver_list:
#         if row[4] == country_name:
#             driver_dict = {}
#             driver_dict["Forename"] = row[1]
#             driver_dict["Surname"] = row[2]
#             driver_dict["Date of Birth"] = row[3]
#             driver_dict["Nationality"] = row[4]
#             driver_dict["URL"] = row[5]

#         list_of_drivers.append(driver_dict)

#     return json.dumps(list_of_drivers)


# on the home page: click on a country on the map, return a JSON list of races held in that country
# on the home page: click on "drivers" button in the navigation bar, jump to the drivers page and display a diagram of top players
try:
    cursor_drivers_with_results = connection.cursor()
    query = '''SELECT drivers.id, results.driverId, results.points 
    FROM drivers, results 
    WHERE drivers.id = results.driverId'''
    cursor_drivers_with_results.execute(query)
except Exception as e:
	print(e)
	exit()

drivers_with_results_list = []
for row in cursor_drivers_with_results:
	drivers_with_results_list.append(row)

@api.route('/topdriver/<number>')
def get_country_races(number):
    driver_points_dict = {}
    for driver in driver_list:
        driver_points = 0
        driver_name = str(driver_list[1]) + " " + str(driver_list[2])
        for row in drivers_with_results_list:
            if row[0] == driver[0]:
                driver_points += row[2]
        driver_points_dict[driver_name] = int(driver_points)
    
    print(driver_points_dict)
    # sorted_driver_points_list = []
    # for i in sorted (driver_points_dict): 
    #     sorted_driver_points_list.append((i, driver_points_dict[i]))
    # # sorted_driver_points_dict = sorted(driver_points_dict, key=lambda i: i[driver_name], reverse=False)

    # top_driver_list = []
    # for i in range(int(number)):
    #     ######## how to get the first key-value pair of the dictionary
    #     cur_pair = sorted_driver_points_list.pop()
    #     top_driver_list.append(cur_pair)

    return json.dumps(driver_points_dict)


# # return top three driver lapTime and pitStop info of a specific race
# # 吐血，未完待续......
# try:
#     cursor_results_lapTime_pitStop = connection.cursor()
#     query = 'SELECT results.raceId, results.driverId, results.points, lapTime.raceID, lapTimes.driverID, lapTimes.time, pitStops.raceId, pitStop.driverId, pitStop.duration, drivers.id, drivers.forename, drivers.surname FROM results, lapTimes, pitStops, drivers WHERE drivers.id = results.driverId'
#     cursor_results_lapTime_pitStop.execute(query)
# except Exception as e:
# 	print(e)
# 	exit()

# race_topThree_info = []
# for row in cursor_results_lapTime_pitStop:
# 	race_topThree_info.append(row)

# # information about a specific race
# @api.route('/race?raceid={raceid}')
# def get_country_races(raceid):
#     list_of_top_three_driver_lapTimes = []
#     list_of_top_three_driver_pitTimes = []

#     num_one_driver

#     for row in race_topThree_info:
#         if row[0] == raceid:
#             if row[2] == !!!!!need to be checked:
#                 num_one_driver == row[]



#     return json.dumps()





connection.close()
