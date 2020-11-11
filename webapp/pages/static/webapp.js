/*
 * webapp.js
 * Jeff Ondich
 * 6 November 2020
 *
 * A little bit of Javascript for the tiny web app sample for CS257.
 */

window.onload = initialize;

function initialize() {
    loadRaceTable();
    var element = document.getElementById('20th century');
    if (element) {
        element.onclick = on20Button;
    }

    var element = document.getElementById('21st century');
    if (element) {
        element.onclick = on21Button;
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function loadRaceTable() {
    var url = getAPIBaseURL() + '/race/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_20_races) {
        var listBody = '';
        for (var k = 0; k < list_of_20_races.length; k++) {
            var race = list_of_20_races[k];
            listBody += '<li>' + race['Name'] +
                ', ' + race['Date'] +
                '-' + race['Country'] +
                ', ' + race['Circuit'] +
                '-' + race['URL'] +
                '</li>\n';
        }
        var race20ListElement = document.getElementById('20centuryRace');
        if (race20ListElement) {
            race20ListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function on20Button() {
    var url = getAPIBaseURL() + '/race/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_20_races) {
        var listBody = '';
        for (var k = 0; k < list_of_20_races.length; k++) {
            var race = list_of_20_races[k];
            listBody += '<li>' + race['Name'] +
                ', ' + race['Date'] +
                '-' + race['Country'] +
                ', ' + race['Circuit'] +
                '-' + race['URL'] +
                '</li>\n';
        }

        var race20ListElement = document.getElementById('20centuryRace');
        if (race20ListElement) {
            race20ListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function on21Button() {
    var url = getAPIBaseURL() + '/race/21';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(list_of_21_races) {
        var listBody = '';
        for (var k = 0; k < list_of_21_races.length; k++) {
            var race = list_of_21_races[k];
            listBody += '<li>' + race['Name'] +
                ', ' + race['Date'] +
                '-' + race['Country'] +
                ', ' + race['Circuit'] +
                '-' + race['URL'] +
                '</li>\n';
        }

        var race20ListElement = document.getElementById('21centuryRace');
        if (race20ListElement) {
            race20ListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}