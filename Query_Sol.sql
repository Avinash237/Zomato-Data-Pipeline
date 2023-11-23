/*Write a query to pull back the most recent redemption count, by redemption date, for the date
range 2023-10-30 to 2023-11-05, for retailer "ABC Store". Your result should have 2 columns
and 7 rows. Provide the query and answer the following questions.*/

------------------------------------------------------------------------------------------------------

WITH RankedRedemptions AS (
  SELECT
    id,
    retailerId,
    redemptionDate,
    redemptionCount,
    createDateTime,
    ROW_NUMBER() OVER (PARTITION BY redemptionDate ORDER BY createDateTime DESC) AS rn
  FROM
    tblRedemptions_byday
  WHERE
    redemptionDate BETWEEN '2023-10-30' AND '2023-11-05'
    AND retailerId = 300 
)
SELECT
  redemptionDate,
  redemptionCount
FROM
  RankedRedemptions
WHERE
  rn = 1;
  
  ---------------------------------------------------------------------------------------------------------------
 -- 1) Which date had the least number of redemptions and what was the redemption count?

SELECT
  redemptionDate,
  MIN(redemptionCount) AS minRedemptionCount
FROM
  tblRedemptions_byday
WHERE
  redemptionDate BETWEEN '2023-10-30' AND '2023-11-05'
  AND retailerId = 300
GROUP BY
  redemptionDate
ORDER BY
  minRedemptionCount
LIMIT 1;
---------------------------------------------------------------------------------------------------------------------------------------------------
--2) Which date had the most number of redemptions and what was the redemption count?

SELECT
  redemptionDate,
  MAX(redemptionCount) AS maxRedemptionCount
FROM
  tblRedemptions-ByDay
WHERE
  redemptionDate BETWEEN '2023-10-30' AND '2023-11-05'
  AND retailerId = 300
GROUP BY
  redemptionDate
ORDER BY
  maxRedemptionCount DESC
LIMIT 1;

--------------------------------------------------------------------------------------------------------------------
--3) What was the createDateTime for each redemptionCount in questions 1 and 2? 

SELECT
  createDateTime
FROM
  tblRedemptions_byday
WHERE
  redemptionDate = 'date_with_least_redemptions'
  AND redemptionCount = minRedemptionCount;
  
------------------------------------------------------------------------------------------
-- For the date with the least number of redemptions:
SELECT
  createDateTime
FROM
  tblRedemptions_byday
WHERE
  redemptionDate = 'date_with_most_redemptions'
  AND redemptionCount = maxRedemptionCount;
  
----------------------------------------------------------------------------------------------------------------------------------------------
/*Is there another method you can use to get the same answer? In words, describe how you would do this:

Another method to get the same answer is to use the RANK() window function to rank the records based on the redemptionCount in descending order for each redemptionDate. Then, filter for the rank = 1 to get the most recent redemption count for each date. This eliminates the need for the subqueries used in the previous approach.*/
  