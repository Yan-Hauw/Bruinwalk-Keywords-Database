# Bruinwalk-scraper-and-analyzer

A program to search a subset of the pages on bruinwalk.com for the appearance of specific keywords

## Run Locally

### Setup

Activate your virtual environment if you'd like to use it.

Install the base execution dependencies using:

```shell
$ pip install -r requirements.txt
```

Install the base execution dependencies and development dependencies using:

```shell
$ pip install -r requirements.txt -r dev-requirements.txt
```

### Running the program

Within the Python code, add the keywords you would like to search for, and provide the bruinwalk class review url that you would like to scrape.

Then, simply run the Python file and a dictionary with each the number of occurences of each keyword will be printed.
