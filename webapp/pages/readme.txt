AUTHORS:
Cathy Guang and Lingyu Wei


DATA:
Our dataset consists of 6 different csv documents
that have connections and present various information about formula 1 race car data
from 1950 all the way through the 2017 season, including drivers.


The raw data is from kaggle.com:
https://www.kaggle.com/cjgdev/formula-1-race-data-19502017?select=circuits.csv

Datamaps is Copyright (c) 2012 Mark DiMarco
https://github.com/markmarkoh/datamaps

TopDriver bar chart is adapted from the Chartist library samples
https://gionkunz.github.io/chartist-js/examples.html


STATUS:

In each html of our website, we have a navigation bar on the top part of the webpage.
The navigation bar consists of "Home" button, "Driver" button, and "Race" button.
When hovering on "Race" button, user will have a two elements' drop down list.

"Home" button:
Through clicking on the "Home" button, you will launch at the index page in the default form.
On the home page, there's a world map which is interactive with the users.
When hovering on the country, the country name will appear next to the cursor.
And after clicking on a specific country, two tables will appear on the bottom of this webpage.
The first table lists all the drivers from the country which user selected.
Each row consists of race name, date, country, location, and circuit name.
Clicking on the name of any driver name in the form, user will launch at the wikipedia page of this race.
The second table list all the races from the country which user selected.
Each row consists of driver name, date of birth, and nationality.
Clicking on the name of any race name in the form, user will launch at the wikipedia page of this race.

"Driver" button:
Through clicking on the "Driver" button, user will launch at a webpage that presents top 10 ranking drivers in the world.
The data will be presented in the form of bar chart.
The x-axis consists the names of the top drivers and the y-axis contains the cumulative points they have earned.
There's a drop down list on the relatively right top of the page, allowing user to change the number of the drivers 
that is presented in the bar chart.

"Race" button:
Through hovering on the "Race" button, a drop down list containing "20th century" and "21st century" will show up at the bottom of race button.
Clicking on either "20th century" button or "21st century" button, you will launch at a webpage that represents a table of information about corresponding century races.
Each row contains race name, date, country, location, and circuit name of a single race took place in that century.
Clicking on the name of any race in the form, user will launch at the wikipedia page of this race.

"Tile" button:
Through clicking on the the tile -- "Formula 1", user will launch back to the index page.
