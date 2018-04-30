# Project-3---LogsAnalysis

 -----------------------------------------------------------------
 ## Udacity Course 
 Full Stack Web Developer
 
 ### Proj #3 
 Logs Reporting Tool
 
 ### Purpose 
 A reporting tool that prints out reports (in plain text) based on
 the data in a PostgreSQL database. This reporting tool is a
 Python 2.7 program using the psycopg2 module to connect to the
 newsdata.sql database.

 ### Running Project Code / Files  
 To run project (in Python 2.7), simply run
 ```
 python LogsReportTool.py
 ```
 from the command line. Text report will appear in console. A copy of the report 
 just created will also be stored in _newsdata_report.txt_ 
 
 * LogsReportTool.py   -- report writing code
 * newsdata_report.txt -- output report text file
 
 
  |     | Date       | Code Changes
  | --- | ---------- | -----------------------------------------
  | PPC | 04/20/2018 | Dummy database mockup code
  | PPC | 04/21/2018 | Dump completed report directly to console
  | PPC | 04/30/2018 | Cleaned up PEP8 issues

----------------------------------------------------------------------------
Question 1 VIEW (viewstable) -- Currently In Database
----------------------------------------------------------------------------
```
CREATE VIEW viewstable  AS Select path, substring(path from 10 for char_length(path) - 9) as slugpath, count(*) as views from log where char_length(path) > 1 and status = '200 OK' group by path ORDER BY views DESC;
```

```
select * from viewstable;
```

 | path                               | slugpath                  | views
 | ---------------------------------- | ------------------------- | ------
 | /article/candidate-is-jerk         | candidate-is-jerk         | 338647
 | /article/bears-love-berries        | bears-love-berries        | 253801
 | /article/bad-things-gone           | bad-things-gone           | 170098
 | /article/goats-eat-googles         | goats-eat-googles         |  84906
 | /article/trouble-for-troubled      | trouble-for-troubled      |  84810
 | /article/balloon-goons-doomed      | balloon-goons-doomed      |  84557
 | /article/so-many-bears             | so-many-bears             |  84504
 | /article/media-obsessed-with-bears | media-obsessed-with-bears |  84383


----------------------------------------------------------------------------
Question 2 VIEW (authorstable) -- Currently In Database
----------------------------------------------------------------------------
```
CREATE VIEW authorstable AS SELECT articles.author, articles.title, viewstable.views FROM articles JOIN viewstable on articles.slug = viewstable.slugpath ORDER BY viewstable.views DESC; 
```

| author |               title                | views
| ------ | ---------------------------------- | -------
|      2 | Candidate is jerk, alleges rival   | 338647
|      1 | Bears love berries, alleges bear   | 253801
|      3 | Bad things gone, say good people   | 170098
|      1 | Goats eat Google's lawn            |  84906
|      2 | Trouble for troubled troublemakers |  84810
|      4 | Balloon goons doomed               |  84557
|      1 | There are a lot of bears           |  84504
|      1 | Media obsessed with bears          |  84383


----------------------------------------------------------------------------
Question 3 VIEW (StatusCounts) -- Currently In Database
----------------------------------------------------------------------------
```
CREATE VIEW StatusCounts AS Select time, status, to_char(cast(time as timestamp), 'Mon DD, YYYY') as mydate, cast(status <> '200 OK' as integer) as Mybad, cast(status = '200 OK' or status = '404 NOT FOUND' as integer) as MyTotal from log Order By mydate;
```

```
news=> select * from statuscounts limit 10;
```

| time                   | status | mydate       | mybad | mytotal
| ---------------------- | ------ | ------------ | ----- | --------
| 2016-07-01 07:00:47+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:34+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:52+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:23+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:05+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:54+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:15+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:01:13+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:21+00 | 200 OK | Jul 01, 2016 |     0 |       1
| 2016-07-01 07:00:00+00 | 200 OK | Jul 01, 2016 |     0 |       1




