window.onload = initialize;

function initialize() {
    createDriverBarChart();
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function createDriverBarChart(topNumber) {
    var url = getAPIBaseURL() + '/topdriver/' + topNumber;

    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(top_driver_list) {
        var labelList = [];
        var dataList = [];
        for (var k = 0; k < top_driver_list.length; k++) {
            var top_driver = top_driver_list[k];
            labelList.push(top_driver[0]);
            dataList.push(top_driver[1]);

        }
        var data = {

            labels: labelList,
            series: [dataList]
        };
        if (topNumber == 50) {
            var options = {
                seriesBarDistance: 10,
                horizontalBars: true,
                reverseData: true
            }
        } else {
            var options = {
                axisX: {
                    position: 'start'
                },
                axisY: {
                    position: 'end'
                }
            };
        }

        new Chartist.Bar('#topdriver-bar-chart', data, options);
    })

    .catch(function(error) {
        console.log(error);
    });
}