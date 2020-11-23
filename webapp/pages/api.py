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
def get_connection():
    return psycopg2.connect(database=database,
                            user=user,
                            password=password)

# return 20th or 21st century races info
@api.route('/race/<century>')
def get_races_by_century(century):
    query = '''SELECT races.id, races.year, races.round, races.circuitID, races.name,
            races.date, races.url, circuits.id, circuits.name, circuits.location, circuits.country, circuits.url
            FROM races, circuits
            WHERE races.circuitID = circuits.id'''
    list_of_20_races = []
    list_of_21_races = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            race_dict = {}
            race_dict["Name"] = row[4]
            race_dict["Date"] = row[5].strftime("%Y-%m-%d")
            race_dict["Country"] = row[10]
            race_dict["Location"] = row[9]
            race_dict["Circuit"] = row[8]
            race_dict["URL"] = row[6]

            if row[1] < 2000:
                list_of_20_races.append(race_dict)
            elif row[1] >= 2000:
                list_of_21_races.append(race_dict)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    if int(century) == 20:
        return json.dumps(list_of_20_races)
    elif int(century) == 21:
        return json.dumps(list_of_21_races)

@api.route('/race/country/<country_name>')
def get_races_by_country(country_name):
    query = '''SELECT races.id, races.year, races.round, races.circuitID, races.name,
            races.date, races.url, circuits.id, circuits.name, circuits.location, circuits.country, circuits.url
            FROM races, circuits
            WHERE races.circuitID = circuits.id'''
    list_of_country_races = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            if row[10] == country_name:
                race_dict = {}
                race_dict["Name"] = row[4]
                race_dict["Date"] = row[5].strftime("%Y-%m-%d")
                race_dict["Country"] = row[10]
                race_dict["Location"] = row[9]
                race_dict["Circuit"] = row[8]
                race_dict["URL"] = row[6]
                list_of_country_races.append(race_dict)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(list_of_country_races)

# on the home page: click on a country on the map, return a JSON list of drivers from that country
@api.route('/driver/country/<country_name>')
def get_drivers_by_country(country_name):
    query = '''SELECT drivers.id, drivers.forename, drivers.surname, drivers.dob, drivers.nationality, drivers.url, nationality.country, nationality.nationality
            FROM drivers, nationality
            WHERE drivers.nationality = nationality.nationality'''
    list_of_country_drivers = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.query.decode("UTF-8"))
        for row in cursor:
            if row[6] == country_name:
                driver_dict = {}
                driver_dict["Forename"] = row[1]
                driver_dict["Surname"] = row[2]
                driver_dict["Date of Birth"] = row[3].strftime("%Y-%m-%d")
                driver_dict["Nationality"] = row[4]
                driver_dict["URL"] = row[5]
                list_of_country_drivers.append(driver_dict)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(list_of_country_drivers)


# on the home page: click on "drivers" button in the navigation bar, jump to the drivers page and display a diagram of top players
@api.route('/topdriver/<number>')
def get_top_drivers(number):
    query = '''SELECT drivers.id, drivers.forename, drivers.surname, results.driverId, results.points
            FROM drivers, results
            WHERE drivers.id = results.driverId'''
    driver_points_dict = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            driver_name = str(row[1]) + " " + str(row[2])
            if driver_name not in driver_points_dict:
                driver_points_dict[driver_name] = int(row[-1])
            else:
                driver_points_dict[driver_name] += int(row[-1])
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    sorted_list = sorted(driver_points_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=False)
    top_driver_list = []
    for i in range(int(number)):
        cur_pair = sorted_list.pop()
        top_driver_list.append(cur_pair)

    return json.dumps(top_driver_list)


# return top three driver lapTime and pitStop info of a specific race
@api.route('/race/specific/<race_name>')
def get_specific_race(race_name):
    query = '''SELECT results.raceId, results.driverId, results.points,
            lapTimes.raceID, lapTimes.driverID, lapTimes.lap, lapTimes.time,
            pitStops.raceId, pitStops.driverId, pitStops.stop, pitStops.lap, pitStops.time, pitStops.duration,
            drivers.id, drivers.forename, drivers.surname, races.id, races.name
            FROM results, lapTimes, pitStops, drivers, races
            WHERE results.raceId = lapTimes.raceID AND results.raceId = pitStops.raceId AND results.raceId = races.id
                AND results.driverId = lapTimes.driverID AND results.driverId = pitStops.driverId AND results.driverId = drivers.id'''
    list_of_top_three_driver_lapTimes = []
    list_of_top_three_driver_pitStops = []
    race_driver_lapTimes_info = {}
    race_driver_pitStops_info = {}

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print(cursor.query.decode("UTF-8"))

        for row in cursor:
            return_list.append(row)
        for row in cursor:
            if row[-1].replace(" ", "") == race_name.replace(" ", "") and int(row[2]) == 10:
                list_of_top_three_driver_lapTimes.append("hahaha")
                race_driver_lapTimes_info['Driver Position'] = 1
                race_driver_lapTimes_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_lapTimes_info['Lap'] = row[3]
                race_driver_lapTimes_info['Lap Time'] = row[4]
                list_of_top_three_driver_lapTimes.append(race_driver_lapTimes_info)

                race_driver_pitStops_info['Driver Position'] = 1
                race_driver_pitStops_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_pitStops_info['Pit Stop Number'] = row[5]
                race_driver_pitStops_info['Pit Stop Lap Number'] = row[6]
                race_driver_pitStops_info['Pit Stop Time'] = row[7]
                race_driver_pitStops_info['Pit Stop Duration'] = row[8]
                list_of_top_three_driver_pitStops.append(race_driver_pitStops_info)

            elif row[-1].replace(" ", "") == race_name.replace(" ", "") and int(row[2]) == 8:
                race_driver_lapTimes_info['Driver Position'] = 2
                race_driver_lapTimes_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_lapTimes_info['Lap'] = row[3]
                race_driver_lapTimes_info['Lap Time'] = row[4]
                list_of_top_three_driver_lapTimes.append(race_driver_lapTimes_info)

                race_driver_pitStops_info['Driver Position'] = 2
                race_driver_pitStops_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_pitStops_info['Pit Stop Number'] = row[5]
                race_driver_pitStops_info['Pit Stop Lap Number'] = row[6]
                race_driver_pitStops_info['Pit Stop Time'] = row[7]
                race_driver_pitStops_info['Pit Stop Duration'] = row[8]
                list_of_top_three_driver_pitStops.append(race_driver_pitStops_info)

            elif row[-1].replace(" ", "") == race_name.replace(" ", "") and int(row[2]) == 6:
                race_driver_lapTimes_info['Driver Position'] = 3
                race_driver_lapTimes_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_lapTimes_info['Lap'] = row[3]
                race_driver_lapTimes_info['Lap Time'] = row[4]
                list_of_top_three_driver_lapTimes.append(race_driver_lapTimes_info)

                race_driver_pitStops_info['Driver Position'] = 3
                race_driver_pitStops_info['Driver Name'] = str(row[9]) + " " + str(row[10])
                race_driver_pitStops_info['Pit Stop Number'] = row[5]
                race_driver_pitStops_info['Pit Stop Lap Number'] = row[6]
                race_driver_pitStops_info['Pit Stop Time'] = row[7]
                race_driver_pitStops_info['Pit Stop Duration'] = row[8]
                list_of_top_three_driver_pitStops.append(race_driver_pitStops_info)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return_list = []
    return_list.append(list_of_top_three_driver_lapTimes)
    return_list.append(list_of_top_three_driver_pitStops)

    return json.dumps(return_list)
