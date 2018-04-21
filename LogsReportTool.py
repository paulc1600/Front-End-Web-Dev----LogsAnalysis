#!/usr/bin/env python2.7
# -----------------------------------------------------------------
#  Logs Reporting Tool
#     A reporting tool that prints out reports (in plain text) based on the
#     data in a PostgreSQL database. This reporting tool is a Python 2.7 program
#     using the psycopg2 module to connect to the newsdata.sql database.
# -----------------------------------------------------------------
#  newdata.sql table structures were as follows:
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
#                (1) default nextval(’articles_id_seq’::regclass)
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
