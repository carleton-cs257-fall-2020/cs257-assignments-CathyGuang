/*
 * topdriver.js
 * Lingyu Wei and Cathy Guang, 23 November 2020
 *
 * Javascript for Formula One top driver graph
 * TopDriver bar chart is adapted from the Chartist library samples
 * https://gionkunz.github.io/chartist-js/examples.html
 */


window.onload = initialize;

function initialize() {
    var driverSelector = document.getElementById('top');
    if (driverSelector) {
        driverSelector.onchange = onTopSelectorChanged;
        createDriverBarChart(10);
    }
}

function onTopSelectorChanged() {
    var driverSelector = document.getElementById('top');
    if (driverSelector) {
        createDriverBarChart(driverSelector.value);
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

/*
 * createDriverBarChart()
 * Load a bar chart that represents the top drivers. 
 */
function createDriverBarChart(topNumber) {
    var url = getAPIBaseURL() + '/topdriver/' + topNumber;
    fetch(url, { method: 'get' })

    .then((response) => response.json())

    .then(function(top_driver_list) {
        var labelList = [];
        var dataList = [];
        for (var k = 0; k < top_driver_list.length; k++) {
            // Add driver names and points to label list and data list 
            var top_driver = top_driver_list[k];
            labelList.push(top_driver[0]);
            dataList.push(top_driver[1]);

        }
        var data = {

            labels: labelList,
            series: [dataList]
        };
        if (topNumber == 10) {
            var options = {
                axisX: {
                    position: 'start'
                },
                axisY: {
                    position: 'end'
                }
            };

        } else {
            var options = {
                axisX: {
                    position: 'start'
                },
                seriesBarDistance: 20,
                horizontalBars: true,
                reverseData: true
            }
        }

        new Chartist.Bar('#topdriver-bar-chart', data, options);
    })

    .catch(function(error) {
        console.log(error);
    });
}