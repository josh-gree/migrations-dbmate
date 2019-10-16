-- migrate:up

CREATE SCHEMA A;
CREATE SCHEMA B;

-- migrate:down

DROP SCHEMA A;
DROP SCHEMA B;