# Project-3---LogsAnalysis

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
