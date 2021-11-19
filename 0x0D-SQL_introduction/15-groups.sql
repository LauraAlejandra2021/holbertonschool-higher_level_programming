-- delete records that match a specific parameter
SELECT score, COUNT(*) AS number FROM second-table GROUP by score ORDER by number DESC;
