import psycopg2
import database_common
import sys


@database_common.connection_handler
def get_mentors(cursor):
    cursor.execute("SELECT * FROM mentors INNER JOIN schools ON mentors.city = schools.city ORDER BY mentors.id ASC;")
    info = cursor.fetchall()
    return info

@database_common.connection_handler
def all_school_list(cursor):
    cursor.execute("SELECT *,CASE WHEN first_name is NULL THEN 'No Data' END FROM mentors FULL JOIN schools ON mentors.city = schools.city ORDER BY mentors.id ASC;")
    info = cursor.fetchall()
    return info


@database_common.connection_handler
def count_mentors(cursor):
    cursor.execute("SELECT country,COUNT(mentors) AS count FROM mentors JOIN schools ON mentors.city = schools.city GROUP BY country ;")
    info = cursor.fetchall()
    return info

@database_common.connection_handler
def contacts(cursor):
    cursor.execute("SELECT schools.name,first_name,last_name FROM mentors JOIN schools ON mentors.id = schools.contact_person ;")
    info = cursor.fetchall()
    return info

@database_common.connection_handler
def applicants(cursor):
    cursor.execute("""SELECT application_code,first_name,creation_date 
    FROM applicants JOIN applicants_mentors ON applicants_mentors.applicant_id = applicants.id WHERE creation_date > '2016-01-01' ;""")
    info = cursor.fetchall()
    return info

@database_common.connection_handler
def applicants_and_mentors(cursor):
    cursor.execute("""SELECT application_code,applicants.first_name,mentors.last_name AS mentor_last,mentors.first_name AS mentor_first
    FROM applicants LEFT JOIN applicants_mentors ON applicants_mentors.applicant_id = applicants.id LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id ;""")
    info = cursor.fetchall()
    return info