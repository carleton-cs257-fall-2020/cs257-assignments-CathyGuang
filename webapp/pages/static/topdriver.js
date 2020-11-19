window.onload = initialize;

function initialize() {
    createDriverBarChart();
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function createDriverBarChart(number) {
    var url = getAPIBaseURL() + '/topdriver/' + 20;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(top_driver_list) {

        var label_list = [];
        for (var k = 0; k < top_driver_list.length; k++) {
            var top_driver = top_driver_list[k];
            label_list.push(top_driver);
        }
        var data = {
            labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
            series: [
                { data: [17, -2, 4, 9, 11, 7, 2] },
                { data: [1, 2, 3, 5, 8, 13, 21] }
            ]
        };
        new Chartist.Bar('#sample-bar-chart', data, options);
    })

    .catch(function(error) {
        console.log(error);
    });
}