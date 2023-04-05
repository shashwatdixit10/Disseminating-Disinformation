# Arithmetic-Terror
Finding/profiling websites disseminating disinformation and their links

To see the project:

Setup
Download the code as a ZIP.
Install all the required Python libraries.
Run app.py.
Server is now running on localhost.
All routes can only be accessed if the user has previously logged in on the same computer.
Feature requests
I am taking feature requests! Create an issue with the label Feature request and i will consider adding it.

Problem statement:
Design and develop a technological solution/software tool that may read information on web pages, and identify possible instances of dissemination information. The system may send notifications. Over a period of time, a dynamic infringing website list (IWL) may be developed and maintained. The system may send notifications to online social media like Facebook for blacklisting of such websites, thereby discouraging such activities.

ALGORITHM:
The user enters a URL or link in a text input field on the web page.
The user presses  "Enter" to initiate a search for information related to the URL or link.
The web page sends an AJAX request to the Flask app with the URL or link as a parameter.
The Flask app receives the AJAX request and extracts relevant information from the webpage, such as the title, description, keywords, and links.
The Flask app analyzes the extracted information from the pre-existing database created using Maltego.
It searches for senstitve words and quotes in the article, checks weather the website is already a disinformative website and generates a suitable result
The Flask app sends the analyzed information back to the web page in string format.
The web page displays the analyzed information in a designated output section on the page.

TECHNOLOGY USED:
Flask: A micro web framework written in Python that is used for building web applications and APIs.
Pandas: An open source data manipulation and analysis library that provides  data structures for efficiently storing and manipulating large datasets.
Chrome APIs: The Chrome API is a set of JavaScript functions that allows developers to interact with the Chrome browser and access various browser functionalities, such as browser tabs, bookmarks, history, and storage.
Content Scripts: Content scripts are JavaScript files that can be injected into web pages to modify the behavior of the page. This is an important technology used in many Chrome extensions.
Materialize: A modern responsive front-end framework based on Material Design.
Bootstrap: A free and open-source CSS framework directed at responsive, mobilend web development.
