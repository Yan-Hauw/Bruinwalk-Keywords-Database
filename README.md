# Bruinwalk Keywords Database

A python program to search scrape and process the text of a page on bruinwalk.com for the appearance of specific keywords

## Run Locally

### Setup

Activate your virtual environment if you'd like to use it.

Install the base execution dependencies using:

```shell
$ pip install -r requirements/requirements.txt
```

If you would like, install both the base execution dependencies and development dependencies using:

```shell
$ pip install -r requirements/requirements.txt -r requirements/dev-requirements.txt
```

### Running the program

Within the Python code, add the keywords you would like to search for, and provide the bruinwalk class review url that you would like to scrape.

Then, simply run the Python file and a dictionary with each the number of occurences of each keyword will be printed.

#### Other notes

This project is a work-in-progress. For now, the program is just a scraper. After a database is set up to store the data that has been scraped, the data can be displayed in an organized way that allows for in-depth analysis of class information.
