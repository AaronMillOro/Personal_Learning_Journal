# Learning journal Web app using Flask
The following project is an interface for a learning journal web application. 

The main (index) page lists journal entry titles and dates. Each journal entry title links to a detail page that displays the title, date, time spent, the journal entry, and related resources .

The application lets the user add or edit journal entries. When adding or editing a journal entry, the application prompts the user for title, date, time spent, what they learned, and resources to remember. The results for these entries are stored in a database (**Sqlite**) and displayed in a blog style website. Design was provided with **CSS** files and **HTML** files were refactored.

## Project details
* The application contains the following routes:

	* **/** - the homepage .
	* **/entries** - also will act as listing route
	* **/entries/new** - to create a route
	* **/entries/< id >** - the detail route
	* **/entries/< id >/edit** - the edit/update route
	* **/entries/delete** - to delete a given route


* The listing view is located in **" / "** and **" /entries "**.  This view render a listing page of all of the journal entries, where each entry displays the following fields:

	* **Title** - is a linked title, clicking it routes user to the detail page for the clicked entry.
	* **Date** - date of creation is listed.

* The add view (**"/entries/new"**) allows the user to add a journal entry with the following fields:

	* **Title** - string
	* **Date** - date
	* **Time Spent** - integer
	* **What You Learned** - text
	* **Resources to Remember** - text

>The page presents a new _blank Entry_ form allowing the user to _Create_ a new entry that will be stored in the database.


*  The details view (**" /entries/< id >"**) renders a detail page of a journal entry with the ** Title, Date,  Time spent, What you learned and Resources to remember** items.

* The edit view (**" /entries/< id >/edit"**) allows the user to edit the journal entry with a given **id**

* The supplied **HTML** and **CSS** files are stored in the folders _**templates**_ and _**static**_, respectively. 

* Python coding style complies with the PEP 8 guidelines.

* Dependencies used in this app are listed in  [**Pipfile**](https://github.com/AaronMillOro/Personal_Learning_Journal/blob/master/Pipfile).

## Test the application in terminal

1. Install and run 'pipenv' 

		1 pipenv install
		2 pipenv shell

2. Download the corresponding dependencies in the virtual environment 

		3 pip install -r requirements.txt
		4 pipenv graph

3. Run the application
		
		5 python3 app.py

4. Open your favorite web browser and type

		http://localhost:5000

Enjoy! :shipit: