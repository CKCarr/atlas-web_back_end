-- 5. Email validation to sent

-- Write a SQL script that creates a trigger
-- that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL,
-- but perfect for user email validation 
-- distribute the logic to the database itself!

DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = FALSE; -- or 0, depending on how you're storing this attribute
    END IF;
END$$

DELIMITER ;
