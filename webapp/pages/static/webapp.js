window.onload = initialize;

function initialize() {
    load20thCenRaceTable();
    load21thCenRaceTable();
    initializeMap();
    var button = document.getElementById('searchButton');
    button.onclick = onRaceSearchButton;
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function load20thCenRaceTable() {
    var url = getAPIBaseURL() + '/race/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_20_races) {
        var tableBody = '';
        tableBody += '<tr>';
        tableBody += '<td>' + 'Race Name' + '</td>';
        tableBody += '<td>' + 'Date' + '</td>';
        tableBody += '<td>' + 'Country' + '</td>';
        tableBody += '<td>' + 'Location' + '</td>';
        tableBody += '<td>' + 'Circuit Name' + '</td>';
        tableBody += '</tr>';
        for (var k = 0; k < list_of_20_races.length; k++) {
            var race = list_of_20_races[k];
            tableBody += '<tr>';
            // tableBody += '<td>' + race['Name'] + '</td>';
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

function load21thCenRaceTable() {
    var url = getAPIBaseURL() + '/race/21';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_21_races) {
        var tableBody = '';
        tableBody += '<tr>';
        tableBody += '<td>' + 'Race Name' + '</td>';
        tableBody += '<td>' + 'Date' + '</td>';
        tableBody += '<td>' + 'Country' + '</td>';
        tableBody += '<td>' + 'Location' + '</td>';
        tableBody += '<td>' + 'Circuit Name' + '</td>';
        tableBody += '</tr>';
        for (var k = 0; k < list_of_21_races.length; k++) {
            var race = list_of_21_races[k];
            tableBody += '<tr>';
            // tableBody += '<td>' + race['Name'] + '</td>';
            tableBody += '<td>' + '<a href=' + race['URL'] + '>' + race['Name'] + '</a>' + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            // tableBody += '<td>' + race['URL'] + '</td>';
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

function clickCountryRace(geography) {
    var url = getAPIBaseURL() + '/race/country/' + geography.properties.name;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_races) {
        var tableBody = '';
        if (list_of_country_races.length == 0) {
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

function clickCountryDriver(geography) {
    var url = getAPIBaseURL() + '/driver/country/' + geography.properties.name;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_drivers) {
        var tableBody = '';
        if (list_of_country_drivers.length == 0) {
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

function onRaceSearchButton() {
    // var countryNameElement = document.getElementById('countryInput');
    var input = window.location.search;
    var countryName = input.split("=").pop();

    var url = getAPIBaseURL() + '/driver/country/' + countryName;
    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_races) {
        var tableBody = '';
        if (list_of_country_races.length == 0) {
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

        var countryRaceSummaryElement = document.getElementById('country_race_by_search');
        if (countryRaceSummaryElement) {
            countryRaceSummaryElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function getInfo() {
    var countryRaceSummaryElement = document.getElementById('country-form');

}