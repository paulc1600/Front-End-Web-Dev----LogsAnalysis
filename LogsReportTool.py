#!/usr/bin/env python2.7
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
#  PPC | 04/21/2018 | Dummy database mockup
# -----------------------------------------------------------------
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
#
import psycopg2
import webbrowser
import os
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

    {q1_results_row1}
    {q1_results_row2}
    {q1_results_row3}

 2. Who are the most popular article authors of all time? Which authors get the
    most page views from all the articles they have written?

    {q2_results}

3. On which days did more than 1% of requests lead to errors?

    {q3_results}

===============================================================================

'''

def get_posts():
	"""Return all posts from the 'database', most recent first."""
	conn = psycopg2.connect("dbname=forum")
	cursor = conn.cursor()
	cursor.execute("select content, time from posts order by time desc")
	all_posts_list = cursor.fetchall()
	all_clean_list = []
	for one_post in all_posts_list:
		one_clean_post = ((),())
		# Use bleach to clean user content of post so no Jave Script injection attack
		one_clean_post = (bleach.clean(one_post[0]), one_post[1])
		all_clean_list.append(one_clean_post)
	conn.close()
	return all_clean_list

def open_report_page():
    # The text content for the report page
    content = ''

    # Append the answers from the "database"
    content += report_page.format(
        q1_results_row1='"Princess Shellfish Marries Prince Handsome" — 1201 views',
        q1_results_row2='"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views',
        q1_results_row3='"Political Scandal Ends In Political Scandal" — 553 views',
        q2_results='Ursula La Multa — 2304 views',
        q3_results='July 29, 2016 — 2.5% errors'
    )

    # Create or overwrite the output file
    output_file = open('newsdata_report.txt', 'w')

    # Output the file
    output_file.write(content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

# Main Path Code Here
open_report_page()                   # In this file
