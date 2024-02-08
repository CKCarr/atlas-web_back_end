-- 4. Buy buy buy
-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

-- Context: Updating multiple tables for one action from your application
-- can generate issue: network disconnection, crash, etc… 
-- to keep your data in a good shape, let MySQL do it for you!

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Temporary variable to hold the average score
    DECLARE avgScore FLOAT;
    
    -- Calculate the average score
    SELECT AVG(score) INTO avgScore
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update the average score in the users table
    UPDATE users
    SET average_score = avgScore
    WHERE id = user_id;
END$$

DELIMITER ;
