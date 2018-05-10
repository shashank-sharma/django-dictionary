# Django dictionary

![Heroku](https://heroku-badge.herokuapp.com/?app=django-dictionary&root=admin&style=flat)

Live version: [Site](http://django-dictionary.herokuapp.com/)

Sample Django web app which will show words on the basis of letter and show their meanings.

1. Clicking on a letter will show all words related to that word.
2. Option to add and remove words.
3. Reopening the application will show words.

Obviously the usability is not final but the core concept which is used for creating this web app was quite simple and used to achieve the given steps only.

### Technologies used

1. Django 2.0 verison
2. Materialize Framework
3. PostgreSQL

### Overview

On opening the website you will see two section. On left you will find words which were saved by the user (currently there is no user model used so everything is getting saved globally). And on right you will see all the letters available in english which is from a-z.

So user first step is to click on any one of the card from a-z, on clicking it will open new page where again there is 2 columns. First column will show all the words which are available. Note that they are case sensitive which needs to be removed and also all the words are not necessarily are words from English Grammar. Those words were extract from nltk wordnet and saved it in json format. And now the right side of column will show the meaning of the word.

Each card on left can do:

1. Hide the card
2. Save the card
3. Search the meaning of the given card

1. Hide will simply remove the card for that particular instance
2. Save the card will save the given word in database
3. Search will make one API request and get its meaning from there. Which means there will be one AJAX call and in return it will update the HTML.

To see the saved data, you will need to go back to the homepage to view it again.

### How to use ?

1. Clone this repository
2. Install everything from requirements.txt
3. Add secret key and API credentials at /dictionary/views.py.

API credentials will be found here: https://developer.oxforddictionaries.com/

4. Make migrations and migrate everything
5. Now run the server and you will be good to go

In case if there is any error then please let me know.
