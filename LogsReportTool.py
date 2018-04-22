#!/usr/bin/env python2.7
# encoding=utf8
# -----------------------------------------------------------------
# Udacity Course: Full Stack Web Developer
# Proj #3: Logs Reporting Tool
# Purpose: A reporting tool that prints out reports (in plain text) based on
#          the data in a PostgreSQL database. This reporting tool is a
#          Python 2.7 program using the psycopg2 module to connect to the
#          newsdata.sql database.
#
#          See README.md for description of required database VIEWS.
#
# Files:  LogsReportTool.py            -- report writing code (this file)
#         newsdata_report.txt          -- output report text file
#
# -----------------------------------------------------------------
#  PPC | 04/20/2018 | Dummy database mockup code
#  PPC | 04/21/2018 | Dump completed report directly to console
# -----------------------------------------------------------------
#
import psycopg2   
import datetime
import calendar
import re

report_page = '''
===============================================================================
  Udacity Course: Full Stack Web Developer
  Proj #3 --- Logs Reporting Tool
  Purpose:   A reporting tool that prints out database reports (in plain text)
  Database:  newsdata.sql
  Date:      {report_date}
  
===============================================================================
1. What are the most popular three articles of all time? Which articles have
   been accessed the most?

{q1_results}

 2. Who are the most popular article authors of all time? Which authors get the
    most page views from all the articles they have written?

{q2_results}

3. On which days did more than 1% of requests lead to errors?

{q3_results}

===============================================================================
'''

def open_report_page():
    # The text content for the report page
    content = ''
    
    # Build Date String for Report
    now = datetime.datetime.now()
    my_date = calendar.month_abbr[now.month]+' '+str(now.day)+', '+str(now.year)
	
    # Access database, answer 1st question: What are the most popular three articles?
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute("SELECT articles.title, viewstable.views FROM articles JOIN viewstable on articles.slug = viewstable.slugpath ORDER BY viewstable.views DESC limit 3")
    q1_rows_list = cursor.fetchall()

    # Answer 2nd question: Who are the most popular article authors?
    cursor.execute("SELECT authors.name, SUM(authorstable.views) as TotalViews FROM authors JOIN authorstable ON authorstable.author = authors.id GROUP BY authors.name ORDER BY TotalViews DESC")
    q2_rows_list = cursor.fetchall()
	
    # Build Question Answer 1 String for Report
    q1_results_str = ""    
    for q1_results_row in q1_rows_list:
        q1_results_str = q1_results_str + '\t' + str(q1_results_row[0]) + ' -- ' + str(q1_results_row[1]) + ' views ' + '\n'

    # Build Question Answer 2 String for Report
    q2_results_str = ""    
    for q2_results_row in q2_rows_list:
        q2_results_str = q2_results_str + '\t' + str(q2_results_row[0]) + '\t \t -- ' + str(q2_results_row[1]) + ' views ' + '\n'	
	
    # Fill in text report template with all built strings and database answers
    content += report_page.format(
        report_date = my_date,
	q1_results = q1_results_str,
	# Append remaining answers from the "database"
        q2_results = q2_results_str,
        q3_results = 'July 29, 2016 — 2.5% errors'
    )

    # No longer need database
    conn.close()
	
    # Create or overwrite the output file
    output_file = open('newsdata_report.txt', 'w')

    # Output the file
    output_file.write(content)
    output_file.close()

    # read the output file to the console 
    with open('newsdata_report.txt', 'r') as fin:
    	print fin.read()
    fin.close()
	
# Main Path Code Here
open_report_page()                   # In this file


# -----------------------------------------------------------------
#  newsdata.sql table structures were as follows:
#
#  Table articles
#   --------+---------------------------+--------------------------
#   Column  | Type                      | Modifiers
#   --------+---------------------------+--------------------------
#   author  | integer                   | not null
#   title   | text                      | not null
#   slug    | text                      | not null
#   lead    | text                      |
#   body    | text                      |
#   time    | timestamp with time zone  | default now()
#   id      | integer                   | not null (1)
#   --------+---------------------------+--------------------------
#                (1) default nextval('articles_id_seq'::regclass)
#
#   Table authors
#   --------+---------+--------------------------------------------
#   Column  |  Type   | Modifiers
#   --------+---------+--------------------------------------------
#   name    | text    | not null
#   bio     | text    |
#   id      | integer | not null (2)
#   --------+---------+--------------------------------------------
#               (2) default nextval('authors_id_seq'::regclass)
#   Indexes:
#       "authors_pkey" PRIMARY KEY, btree (id)
#   Referenced by:
#       TABLE "articles" CONSTRAINT "articles_author_fkey"
#              FOREIGN KEY (author) REFERENCES authors(id)
#
#   Table log
#   --------+--------------------------+--------------------------
#   Column  | Type                     | Modifiers
#   --------+--------------------------+--------------------------
#   path    | text                     |
#   ip      | inet                     |
#   method  | text                     |
#   status  | text                     |
#   time    | timestamp with time zone | default now()
#   id      | integer                  | not null (3)
#   --------+--------------------------+--------------------------
#                 (3) default nextval('log_id_seq'::regclass)
#   Indexes:
#      "log_pkey" PRIMARY KEY, btree (id)
#
# -----------------------------------------------------------------
