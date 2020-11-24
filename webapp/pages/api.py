'''
    api.py

    Lingyu Wei and Cathy Guang

    Flask API for Formula 1 Data Summary
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

'''
    Connect to the database
'''
def get_connection():
    return psycopg2.connect(database=database,
                            user=user,
                            password=password)

'''
    Returns a JSON list of information about all the formula 1 races took place in 20th century or 21st century.
'''
@api.route('/race/<century>')
def get_races_by_century(century):
    # Connect with the database
    query = '''SELECT races.id, races.year, races.round, races.circuitID, races.name,
            races.date, races.url, circuits.id, circuits.name, circuits.location, circuits.country, circuits.url
            FROM races, circuits
            WHERE races.circuitID = circuits.id'''

    # Create two lists to contain races separately according to the century
    list_of_20_races = []
    list_of_21_races = []

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor:
            # Create dictionary for each race
            race_dict = {}

            race_dict["Name"] = row[4]
            race_dict["Date"] = row[5].strftime("%Y-%m-%d")
            race_dict["Country"] = row[10]
            race_dict["Location"] = row[9]
            race_dict["Circuit"] = row[8]
            race_dict["URL"] = row[6]

            # Append each dictionary into corresponding list according to the century
            if row[1] < 2000:
                list_of_20_races.append(race_dict)
            elif row[1] >= 2000:
                list_of_21_races.append(race_dict)

        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    # Return the correct JSON list according to the request
    if int(century) == 20:
        return json.dumps(list_of_20_races)
    elif int(century) == 21:
        return json.dumps(list_of_21_races)

'''
    After clicking on one country in the map of index page, returns a JSON list of information about all the races that were held in the specific country.
'''
@api.route('/race/country/<country_name>')
def get_races_by_country(country_name):
    # Connect with the database
    query = '''SELECT races.id, races.year, races.round, races.circuitID, races.name,
            races.date, races.url, circuits.id, circuits.name, circuits.location, circuits.country, circuits.url
            FROM races, circuits
            WHERE races.circuitID = circuits.id'''

    # Create a list to contain all the races that were held in the specific country
    list_of_country_races = []

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor:
            # Check if the race in each row mwas held in the specific country
            if row[10] == country_name:
                # Create a dicitonary for each race that meet condition
                race_dict = {}

                race_dict["Name"] = row[4]
                race_dict["Date"] = row[5].strftime("%Y-%m-%d")
                race_dict["Country"] = row[10]
                race_dict["Location"] = row[9]
                race_dict["Circuit"] = row[8]
                race_dict["URL"] = row[6]

                # Append each dictionary into the list
                list_of_country_races.append(race_dict)

        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(list_of_country_races)

'''
    After clicking on one country in the map of index page, returns a JSON list of information about all the drivers who are from the specific country.
'''
@api.route('/driver/country/<country_name>')
def get_drivers_by_country(country_name):
    # Connect with the database
    query = '''SELECT drivers.id, drivers.forename, drivers.surname, drivers.dob, drivers.nationality, drivers.url, nationality.country, nationality.nationality
            FROM drivers, nationality
            WHERE drivers.nationality = nationality.nationality'''

    # Create a list to contain all the drivers who are from the specific country
    list_of_country_drivers = []

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor:
            # Check if the race in each row mwas held in the specific country
            if row[6] == country_name:
                # Create a dicitonary for each driver that meet condition
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


'''
    Returns a JSON list of top drivers according to their cumulative points. The size of the JSON list can be changed by request.
'''
@api.route('/topdriver/<number>')
def get_top_drivers(number):
    query = '''SELECT drivers.id, drivers.forename, drivers.surname, results.driverId, results.points
            FROM drivers, results
            WHERE drivers.id = results.driverId'''

    # Create a dictionary for each driver to calculate their cumulative points
    driver_points_dict = {}

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor:
            driver_name = str(row[1]) + " " + str(row[2])
            # Check if the driver is already in the dictionary and sum his or her points
            if driver_name not in driver_points_dict:
                driver_points_dict[driver_name] = int(row[-1])
            else:
                driver_points_dict[driver_name] += int(row[-1])

        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    # Sort the dictionary with respect to the values
    sorted_list = sorted(driver_points_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=False)

    # Create a list to store the information that is required
    top_driver_list = []
    # Select the drivers who are in the requested range and append them to the return list
    for i in range(int(number)):
        cur_pair = sorted_list.pop()
        top_driver_list.append(cur_pair)

    return json.dumps(top_driver_list)
