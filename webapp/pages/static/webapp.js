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

function load20thCenRaceTable() {
    var url = getAPIBaseURL() + '/race/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_20_races) {
        var tableBody = '';
        for (var k = 0; k < list_of_20_races.length; k++) {
            var race = list_of_20_races[k];
            tableBody += '<tr>';
            tableBody += '<td>' + race['Name'] + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            tableBody += '<td>' + race['URL'] + '</td>';
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
        for (var k = 0; k < list_of_21_races.length; k++) {
            var race = list_of_21_races[k];
            tableBody += '<tr>';
            tableBody += '<td>' + race['Name'] + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            tableBody += '<td>' + race['URL'] + '</td>';
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
        done: onMapDone,
        fills: { defaultFill: 'crimson' },
        geographyConfig: {
            popupTemplate: hoverPopupTemplate,
            borderColor: '#eeeeee',
            highlightFillColor: '#eeeeee',
            highlightBorderColor: 'crimson',
        }
    });
}

function doneMap(dataMap) {
    dataMap.svg.selectAll('.datamaps-subunit').on('click', clickCountryRace, clickCountryDriver);
}

function clickCountryRace(geography) {
    var url = getAPIBaseURL() + '/race/country/' + geography.properties.name;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_country_races) {
        var tableBody = '';
        for (var k = 0; k < list_of_country_races.length; k++) {
            var race = list_of_country_races[k];
            tableBody += '<tr>';
            tableBody += '<td>' + race['Name'] + '</td>';
            tableBody += '<td>' + race['Date'] + '</td>';
            tableBody += '<td>' + race['Country'] + '</td>';
            tableBody += '<td>' + race['Location'] + '</td>';
            tableBody += '<td>' + race['Circuit'] + '</td>';
            tableBody += '<td>' + race['URL'] + '</td>';
            tableBody += '</tr>';
        }
        var countrySummaryElement = document.getElementById('country_race');
        if (race20ListElement) {
            race20ListElement.innerHTML = tableBody;
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
        for (var k = 0; k < list_of_country_drivers.length; k++) {
            var driver = list_of_country_drivers[k];
            tableBody += '<tr>';
            tableBody += '<td>' + driver['Forename'] + '</td>';
            tableBody += '<td>' + driver['Surname'] + '</td>';
            tableBody += '<td>' + driver['Date of Birth'] + '</td>';
            tableBody += '<td>' + driver['Nationality'] + '</td>';
            tableBody += '<td>' + driver['URL'] + '</td>';
            tableBody += '</tr>';
        }
        var countrySummaryElement = document.getElementById('country_driver');
        if (race20ListElement) {
            race20ListElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}