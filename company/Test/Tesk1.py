'''
https://stackoverflow.com/questions/31761239/finding-the-difference-between-the-latest-and-the-second-latest-term
'''

'''
SELECT last_one.event_type, (last_one.value - second_last_one.value) AS value
FROM (SELECT event_type, value
      FROM   events
      GROUP BY event_type, time, value
      ORDER BY time ASC
      LIMIT 2 OFFSET 1) AS second_last_one ,
     (SELECT event_type, value
          FROM   events
          GROUP BY event_type, time, value
          ORDER BY time DESC
          LIMIT 2 OFFSET 0) AS last_one
WHERE last_one.event_type IN ( SELECT event_type
                        FROM events
                        GROUP BY event_type
                        HAVING COUNT(event_type) >= 2 )
AND last_one.event_type = second_last_one.event_type
ORDER BY last_one.event_type ASC
'''