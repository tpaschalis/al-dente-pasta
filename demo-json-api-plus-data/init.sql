-- Create initial table

CREATE TABLE copypastas (
	uniqueId TEXT NOT NULL,
	isodate TEXT NOT NULL,
	expireType TEXT NOT NULL,
	content TEXT NOT NULL,
	views INTEGER,
	author text,
	shard text,
	PRIMARY KEY(uniqueId)
);

