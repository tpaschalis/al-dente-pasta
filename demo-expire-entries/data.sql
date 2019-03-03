-- Create initial table

-- Expire types
-- h : hourly
-- d : daily
-- w : weekly
-- m : montly
-- y : yearly
-- null : no expiry
CREATE TABLE IF NOT EXISTS expiry_demo(
    uuid text,
    isodate text,
    unixdate integer,
    expire_type text,
    content text
);


-- I have an Excel spreadsheet to easily create as many test cases as you'd like.


INSERT INTO expiry_demo(uuid, isodate, unixdate, expire_type, content) 
VALUES ("aaa11", "2019-03-01T15:16:27+00:00", 1551453387, "h", "Ipsum Lorem"),
("someid5", "2019-03-04T00:00:00+00:00", 1551657600, "h", "Ipsum Lorem"),
("someid6", "2019-03-02T00:00:00+00:00", 1551484800, "d", "One+ Day Ago"),
("someid7", "2019-03-01T00:00:00+00:00", 1551398400, "d", "One+ Day Ago"),
("someid8", "2019-02-20T00:00:00+00:00", 1550620800, "w", "One+ Week Ago"),
("someid9", "2019-02-19T00:00:00+00:00", 1550534400, "m", "One+ Week Ago"),
("someid10", "2019-01-18T00:00:00+00:00", 1547769600, "m", "One+ Month Ago"),
("someid11", "2019-02-01T00:00:00+00:00", 1548979200, "y", "One+ Month Ago"),
("someid12", "2018-01-01T00:00:00+00:00", 1514764800, "y", "One+ Year Ago"),
("someid13", "2018-02-05T00:00:00+00:00", 1517788800, "y", "One+ Year Ago");

-- Use these to enter singular rows
-- INSERT INTO expiry_demo(uuid, isodate, unixdate, expire_type, content) 
-- VALUES ("someid5", "2019-03-04T00:00:00+00:00", 1551657600, "h", "Ipsum Lorem");


-- To view and list the rows
-- SELECT * FROM expiry_demo WHERE expire_type = 'h' AND isodate < date('now', '-1 hours');
-- SELECT * FROM expiry_demo WHERE expire_type = 'd' AND isodate < date('now', '-1 days');
-- SELECT * FROM expiry_demo WHERE expire_type = 'w' AND isodate < date('now', '-7 days');
-- SELECT * FROM expiry_demo WHERE expire_type = 'm' AND isodate < date('now', '-1 months');
-- SELECT * FROM expiry_demo WHERE expire_type = 'y' AND isodate < date('now', '-1 years');

-- Then deleting them is simple as well
-- DELETE FROM expiry_demo WHERE expire_type = 'h' AND isodate < date('now', '-1 hours');
-- DELETE FROM expiry_demo WHERE expire_type = 'd' AND isodate < date('now', '-1 days');
-- DELETE FROM expiry_demo WHERE expire_type = 'w' AND isodate < date('now', '-7 days');
-- DELETE FROM expiry_demo WHERE expire_type = 'm' AND isodate < date('now', '-1 months');
-- DELETE FROM expiry_demo WHERE expire_type = 'y' AND isodate < date('now', '-1 years');

