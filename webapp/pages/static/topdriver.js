window.onload = initialize;

function initialize() {
    createDriverBarChart();
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function createDriverBarChart() {
    var url = getAPIBaseURL() + '/topdriver/20';

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(top_driver_list) {

        // var label_list = [];
        // for (var k = 0; k < top_driver_list.length; k++) {
        //     var top_driver = top_driver_list[k];
        //     label_list.push(top_driver);
        // }
        var data = {
            labels: [Mon, Tue],
            series: [
                [17, -2]
            ]
        };

        var options = {
            seriesBarDistance: 10
        }
        new Chartist.Bar('#sample-bar-chart', data, options);
    })

    .catch(function(error) {
        console.log(error);
    });
}