/*
 * webapp.js
 * Lingyu Wei and Cathy Guang, 11 November 2020
 *
 * Javascript for Formula One website design
 *
 * Datamaps is Copyright (c) 2012 Mark DiMarco
 * https://github.com/markmarkoh/datamaps
 */


window.onload = initialize;

function initialize() {
    load20thCenRaceTable();
    load21thCenRaceTable();
    initializeMap();
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

/*
 * load20thCenRaceTable()
 * Load table with data of 20th century race information.
 */
function load20thCenRaceTable() {
    var url = getAPIBaseURL() + '/race/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_20_races) {
        var tableBody = '';
        // Add table title
        tableBody += '<tr>';
        tableBody += '<th>' + 'Race Name' + '</th>';
        tableBody += '<th>' + 'Date' + '</th>';
        tableBody += '<th>' + 'Country' + '</th>';
        tableBody += '<th>' + 'Location' + '</th>';
        tableBody += '<th>' + 'Circuit Name' + '</th>';
        tableBody += '</tr>';
        for (var k = 0; k < list_of_20_races.length; k++) {
            var race = list_of_20_races[k];
            // Add table contents
            tableBody += '<tr>';
            tableBody += '<td>' + '<a href=' + race['URL'] + '>' + race['Name'] + '</a>' + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            tableBody += '</tr>';
        }
        var race20ListElement = document.getElementById('20centuryRace');
        if (race20ListElement) {
            race20ListElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

/*
 * load21thCenRaceTable()
 * Load table with data of 21st century race information.
 */
function load21thCenRaceTable() {
    var url = getAPIBaseURL() + '/race/21';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_21_races) {
        var tableBody = '';
        // Add table title
        tableBody += '<tr>';
        tableBody += '<th>' + 'Race Name' + '</th>';
        tableBody += '<th>' + 'Date' + '</th>';
        tableBody += '<th>' + 'Country' + '</th>';
        tableBody += '<th>' + 'Location' + '</th>';
        tableBody += '<th>' + 'Circuit Name' + '</th>';
        tableBody += '</tr>';
        for (var k = 0; k < list_of_21_races.length; k++) {
            var race = list_of_21_races[k];
            tableBody += '<tr>';
            // Add table contents
            tableBody += '<td>' + '<a href=' + race['URL'] + '>' + race['Name'] + '</a>' + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            tableBody += '</tr>';
        }
        var race21ListElement = document.getElementById('21centuryRace');
        if (race21ListElement) {
            race21ListElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
/*
 * initializeMap()
 * Create a new map.
 */
function initializeMap() {
    var map = new Datamap({
        element: document.getElementById('world_map'),
        scope: 'world',
        projection: 'mercator',
        done: doneMap,
        fills: { defaultFill: 'crimson' },
        geographyConfig: {
            borderColor: '#eeeeee',
            highlightFillColor: '#eeeeee',
            highlightBorderColor: 'crimson',
        }
    });
}

function doneMap(dataMap) {
    dataMap.svg.selectAll('.datamaps-subunit').on('click', onClickCountry);
}

function onClickCountry(geography) {
    clickCountryRace(geography);
    clickCountryDriver(geography);
}

/*
 * clickCountryRace()
 * When user clicks on a country, draw the table with races information for that country.
 */
function clickCountryRace(geography) {
    var url = getAPIBaseURL() + '/race/country/' + geography.properties.name;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_races) {
        var tableBody = '';
        if (list_of_country_races.length == 0) {
            // Draw an empty table if there's no race took place in the specific country
            tableBody += '<tr>';
            tableBody += '<td>' + 'No Race Available for This Country' + '</td>';
            tableBody += '</tr>';
        } else {
            tableBody += '<tr>';
            tableBody += '<th>' + 'Race Name' + '</th>';
            tableBody += '<th>' + 'Date' + '</th>';
            tableBody += '<th>' + 'Country' + '</th>';
            tableBody += '<th>' + 'Location' + '</th>';
            tableBody += '<th>' + 'Circuit Name' + '</th>';
            tableBody += '</tr>';
            for (var k = 0; k < list_of_country_races.length; k++) {
                // Add all the race information from list into table
                var race = list_of_country_races[k];
                tableBody += '<tr>';
                tableBody += '<td>' + '<a href=' + race['URL'] + '>' + race['Name'] + '</a>' + '</td>';
                tableBody += '<td>' + race['Date'] + '</td>';
                tableBody += '<td>' + race['Country'] + '</td>';
                tableBody += '<td>' + race['Location'] + '</td>';
                tableBody += '<td>' + race['Circuit'] + '</td>';
                tableBody += '</tr>';
            }
        }

        var countryRaceSummaryElement = document.getElementById('country_race');
        if (countryRaceSummaryElement) {
            countryRaceSummaryElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

/*
 * clickCountryDriver()
 * When user clicks on a country, draw the table with drivers information for that country.
 */
function clickCountryDriver(geography) {
    var url = getAPIBaseURL() + '/driver/country/' + geography.properties.name;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_drivers) {
        var tableBody = '';
        if (list_of_country_drivers.length == 0) {
            // Draw an empty table if there's no driver from the specific country
            tableBody += '<tr>';
            tableBody += '<td>' + 'No Driver Available for This Country' + '</td>';
            tableBody += '</tr>';
        } else {
            tableBody += '<tr>';
            tableBody += '<th>' + 'Driver Name' + '</th>';
            tableBody += '<th>' + 'Date of Birth' + '</th>';
            tableBody += '<th>' + 'Nationality' + '</th>';
            tableBody += '</tr>';
            for (var k = 0; k < list_of_country_drivers.length; k++) {
                // Add all the driver information from list into table
                var driver = list_of_country_drivers[k];
                tableBody += '<tr>';
                tableBody += '<td>' + '<a href=' + driver['URL'] + '>' + driver['Forename'] + driver['Surname'] + '</a>' + '</td>';
                tableBody += '<td>' + driver['Date of Birth'] + '</td>';
                tableBody += '<td>' + driver['Nationality'] + '</td>';
                tableBody += '</tr>';
            }
        }
        var countryDriverSummaryElement = document.getElementById('country_driver');
        if (countryDriverSummaryElement) {
            countryDriverSummaryElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
