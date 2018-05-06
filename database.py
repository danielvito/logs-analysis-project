# Database code for the reports of the Logs Analysis Project.

import psycopg2

DBNAME = "news"
USER = "postgres"
PASSWORD = "123"


def get_connection_string():
    """Return the connection string"""
    conn_string = "dbname='" + DBNAME + "' user='" + USER + "' password='" \
                  + PASSWORD + "'"
    return conn_string


def execute_query(query):
    """Execute a query and return the data and the columns names."""
    db = psycopg2.connect(get_connection_string())
    c = db.cursor()
    c.execute(query)
    column_names = [desc[0] for desc in c.description]
    rows = c.fetchall()
    db.close()
    return [column_names, rows]


def most_popular_three_articles():
    """Return the most popular three articles of all time"""
    query = """
    select
        l.path, a.title as "article_name", a.slug,
        l.status as "request_status", count(l.id) as page_views
    from
        log l
        left join articles a on a.slug = substring(l.path from 10)
    where
        1 = 1
        and l.path like '%article%'
        and l.status = '200 OK'
    group by
        l.path, a.title, a.slug, l.status
    order by page_views desc
        limit 3"""
    return execute_query(query)


def most_popular_authors_of_all_time():
    """Return the most popular authors of all time"""
    query = """
    select
        t."name" as "author_name", count(l.id) as page_views
    from
        log l
        inner join articles a on a.slug = substring(l.path from 10)
        inner join authors t on t.id = a.author
    where
        1 = 1
        and l.path like '%article%'
        and l.status = '200 OK'
    group by
        t."name"
    order by page_views desc"""
    return execute_query(query)


def days_with_more_than_1perc_errors():
    """Return the days that more than 1% of requests lead to errors"""
    query = """
    select
        to_char(time, 'YYYY-MM-DD') as "day",
        count(id) as total_requests,
        sum(
            case when status = '200 OK' then 1
            else 0 end
        ) as "total_success",
        sum(
            case when status <> '200 OK' then 1
            else 0 end
        ) as "total_errors",
        (sum(
            case when status <> '200 OK' then 1
            else 0 end
        ) * 100)::numeric / count(*) as "percentual_errors"
    from
        log l
    where
        1 = 1
    group by
        to_char(time, 'YYYY-MM-DD')
    having
        (sum(
            case when status <> '200 OK' then 1
            else 0 end
        ) * 100)::numeric / count(*) >= 1
    order by "percentual_errors" desc"""
    return execute_query(query)
