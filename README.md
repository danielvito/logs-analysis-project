# Logs Analysis Project
Source code to execute and genarate reports from a postgresql database.

# Project
The Log Analysis project consists of building an informative summary from logs avaiable in a postgresql database.
This project makes part of the [Full-Stack Web Nanodegree Program](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004) from Udacity.

# Code
Code is neatly formatted and follows the Python [PEP-8 Guidelines](http://pep8online.com/).

# Installation and Usage
In order to run this project you need python 3.x installed.
It's necessary a postgresql database up with all the data avaiable at `/files/newsdata.zip`.
The credentials for the database are:
    DBNAME = "news"
    USER = "postgres"
    PASSWORD = "123"

```sh
git clone https://github.com/danielvito/logs-analysis-project.git
cd logs-analysis-project
# you can generate the reports one by one
python report.py most_popular_articles
python report.py most_popular_authors
python report.py days_with_erros
# alternativaly, you can generate all reports together
python report.py all
```

It will generate csv files with the report content into the current directory.

There are examples of those files at `/files/` directory.

# License
All the code in this project is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.