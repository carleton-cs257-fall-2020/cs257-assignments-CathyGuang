window.onload = initialize;

function initialize() {
    createDriverLineChart();
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function createDriverLineChart() {
    var data = {
        labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        series: [
            { data: [17, -2, 4, 9, 11, 7, 2] },
            { data: [1, 2, 3, 5, 8, 13, 21] }
        ]
    };
    var options = {}

    new Chartist.Line('#sample-line-chart', data, options);

}