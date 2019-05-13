# Learning journal Web app using Flask
The following project is an interface for a learning journal web application. 

The main (index) page lists journal entry titles and dates. Each journal entry title links to a detail page that displays the title, date, time spent, the journal entry, and related resources .

The application lets the user add or edit journal entries. When adding or editing a journal entry, the application prompts the user for title, date, time spent, what they learned, and resources to remember. The results for these entries are stored in a database (**Sqlite**) and displayed in a blog style website. HTML and CSS files were provided for this app.

## Project details
* The application contains the following routes:
>
**/** - the homepage .
**/entries** - also will act as listing route
**/entries/new** - to create a route
**/entries/< id > ** - the detail route
**/entries/< id >/edit** - the edit/update route
**/entries/< id >/delete** - to delete a given route


* The listing view is located in **" / "** and **" /entries "**.  This view render a listing page of all of the journal entries, where each entry displays the following fields:
>
** Title ** - should be a linked title, clicking it routes user to the detail page for the clicked entry.
** Date ** - the date of creation is listed.

*  The details view (**" /entries/< id >"**) renders a detail page of a journal entry with the following items:
>**
Title
Date
Time Spent
What You Learned
Resources to Remember**
>
This page contains a link/button that takes the user to the Edit route for the Entry with the < id >.

* The add view (**"/entries/new"**) that allows the user to add a journal entry with the following fields:
>
**Title** - string
**Date** - date
**Time Spent** - integer
**What You Learned** - text
**Resources to Remember** - text
>
The page presents a new _blank Entry_ form that allows the user to _Create_ a new entry that will be stored in the database.

* The edit view (**" /entries/< id >/edit"**) allows the user to edit the journal entry with a given **id**
>
**Title
Date
Time Spent
What You Learned
Resources to Remember**
>
Each form field contains the existing data on load.
>
NOTE: Updating an Entry should not result in a new Entry being created, this behavior would not be seen as editing this would be adding a new entry. To check this, you can simply make an edit and then reload the listing page to see if a duplicate record was created.

* The supplied **HTML** and **CSS** are stored in the folders _**templates**_ and _**static**_, respectively. 

* Python coding style complies with the PEP 8 guidelines.

* Dependencies used in this app are listed in the **requirements.txt** file.
