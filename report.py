# Use database class to generate the reports files.

import sys
import datetime
from database import *

INSTRUCTIONS = """You must choose a valid option of report. Use:
    python report.py most_popular_articles
    python report.py most_popular_authors
    python report.py days_with_erros
    python report.py all
    """


def create_file(file_name, content):
    """ Create a text file using the name file pattern and the content. """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    with open(file_name + "_" + timestamp + ".csv", 'wb') as output:
        output.write(str.encode(content))


def row_to_string(row, separator, break_line):
    """ Converts a row into a string format. """
    line = ""
    sep_aux = ""
    for value in row:
        line += sep_aux + str(value)
        sep_aux = separator
    return line + break_line


def generate_report(data):
    """ Generate the report content based on the data """
    columns = data[0]
    rows = data[1]

    break_line = "\n"
    sep = ","
    csv_content = ""

    csv_content += row_to_string(columns, sep, break_line)

    for row in rows:
        csv_content += row_to_string(row, sep, break_line)
    return csv_content

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Error: missing type of file argument")
        print(INSTRUCTIONS)
        sys.exit(1)

    if sys.argv[1] not in ['most_popular_articles', 'most_popular_authors',
                           'days_with_erros', 'all']:
        print("Error: invalid type of file (" + sys.argv[1] + ")")
        print(INSTRUCTIONS)
        sys.exit(2)

    if (sys.argv[1] in ['most_popular_articles', 'all']):
        create_file('most_popular_articles',
                    generate_report(most_popular_three_articles()))
    if (sys.argv[1] in ['most_popular_authors', 'all']):
        create_file('most_popular_authors',
                    generate_report(most_popular_authors_of_all_time()))
    if (sys.argv[1] in ['days_with_erros', 'all']):
        create_file('days_with_erros',
                    generate_report(days_with_more_than_1perc_errors()))
    print('Done.')
