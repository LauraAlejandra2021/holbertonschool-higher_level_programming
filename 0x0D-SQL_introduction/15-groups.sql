-- delete records that match a specific parameter
SELECT score, COUNT(*) AS number FROM second_table GROUP by score ORDER by number DESC;
