### Flask Lecture Activities ###
Each of the two activities below involves creating a very simple Flask server. If you've read the pre-lecture notes and installed Flask, this should take no time at all. (If you haven't read the notes, you can find them [here](https://github.com/CS196Illinois/lecture-notes-sp19/blob/master/flask.md))

#### Activity 1: A Simple Greeting ####
In this activity, you will create a Flask server that handles a single GET request to the base URL. If no URL parameters are specified in the request, the server should return a simple welcome message. If the parameter 'name' is specified, the server should return a greeting that includes the given name.

Examples:

| URL                               | Response                    |
| :-------------------------------- | :-------------------------- |
| http://localhost:5000/            | Hey there stranger!         |
| http://localhost:5000/?name=Bob   | Hey Bob, nice to meet you!  |


Hint: *request.args.get(<parameter_name>)* will return *None* if there is no URL parameter matching <parameter_name>.

If you are having trouble, double check the URL parameter example in the pre-lecture notes.

<br>

#### Activity 2: Creating an API ####

In this activity, you will create a very basic API that formats a date. APIs revolve around the idea of an *interface* — a description of commands that can be used to send or retrieve information. To describe an API, we must specify parameters and responses for each command. (Note, however, that we don't generally care exactly how the commands themselves are implmented, we just care that the commands do what they're expected to do)

For this activity, you should create an API (i.e. a Flask server) with one command, called *dateconvert*, that converts a date given in MM/DD/YYYY format to one in \<Month Name\> DD, YYYY format.

Specifically, given a URL with the following structure:

> *http://<i></i>localhost:5000/**dateconvert**/Month/Day/Year*

where *Month, Day, and Year* are integers,

your API should return the following:

> *\<Month Name\> Day, Year*

where *Month Name* is the full name of the month. If the month specified is invalid, just return some text that indicates there was an error. Don't worry about other error checking, such as making sure the day of the month or the year are valid.

Examples:

| URL                                           | Response                    |
| :-------------------------------------------- | :-------------------------- |
| http://localhost:5000/dateconvert/2/2/2019    | February 2, 2019            |
| http://localhost:5000/dateconvert/12/29/2020  | December 29, 2020           |
| http://localhost:5000/dateconvert/15/29/2020  | Invalid Month!              |

Hint: You can use the *int()* function to cast the month parameter to an integer.

If you are unsure how to parse parameters in this format (i.e when the parameters are part of the URL path rather than specified at the end of the URL), reference the pre-lecture notes.

<br>

#### Submission ####

Once you have completed the two activites above, submit your files using [this form](https://goo.gl/forms/CxqxJyGhPwhlZ1Gd2).

Note that your submission **will not be autograded** in any way, but we will check the submissions for completion to see who is following along with the lecture activities.
