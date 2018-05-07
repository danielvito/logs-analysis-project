#!/usr/bin/env python

# Use database class to generate the reports files.

import sys
import datetime
from database import *

INSTRUCTIONS = """You must choose a valid option of report.
    Usage: ./report.py report_option [output_type]

    Report options: most_popular_articles, most_popular_authors, days_with_erros, all
    Output types: csv, inline (default: inline)

    Examples:
    ./report.py most_popular_articles csv
    ./report.py most_popular_authors inline
    ./report.py days_with_erros csv
    ./report.py all inline
    """  # NOQA


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


def generate_report(data, type, unit=''):
    """ Generate the report content based on the data """
    columns = data[0]
    rows = data[1]

    if (type == 'csv'):
        break_line = "\n"
        sep = ","
        csv_content = ""

        csv_content += row_to_string(columns, sep, break_line)

        for row in rows:
            csv_content += row_to_string(row, sep, break_line)
        return csv_content

    inline_content = ""
    for row in rows:
        print(rows)
        inline_content += row[0] + " - " + str(row[len(row) - 1]) + unit + "\n"
    return inline_content

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Error(1): missing type of file argument")
        print(INSTRUCTIONS)
        sys.exit(1)

    if sys.argv[1] not in ['most_popular_articles', 'most_popular_authors',
                           'days_with_erros', 'all']:
        print("Error(2): invalid type of file (" + sys.argv[1] + ")")
        print(INSTRUCTIONS)
        sys.exit(2)

    type = 'inline'
    if len(sys.argv) >= 3 and sys.argv[2]:
        type = sys.argv[2]

    if type not in ['csv', 'inline']:
        print("Error(3): type must be csv or inline")
        print(INSTRUCTIONS)
        sys.exit(3)

    if (sys.argv[1] in ['most_popular_articles', 'all']):
        report = generate_report(most_popular_three_articles(), type, ' views')
        if type == 'csv':
            create_file('most_popular_articles', report)
        else:
            print("Most popular articles:")
            print(report)

    if (sys.argv[1] in ['most_popular_authors', 'all']):
        report = generate_report(most_popular_authors_of_all_time(), type,
                                 ' views')
        if type == 'csv':
            create_file('most_popular_authors', report)
        else:
            print("Most popular authors:")
            print(report)

    if (sys.argv[1] in ['days_with_erros', 'all']):
        report = generate_report(days_with_more_than_1perc_errors(), type, '%')
        if type == 'csv':
            create_file('days_with_erros', report)
        else:
            print("Days with more than 1% error on requests:")
            print(report)

    print('Done.')
