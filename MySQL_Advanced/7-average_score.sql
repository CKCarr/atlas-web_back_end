-- 7. Average score

-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

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
