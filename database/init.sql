CREATE TABLE IF NOT EXISTS ROUTES(
	ID INT PRIMARY KEY NOT NULL,
	SOURCE_LATITUDE CHAR(10) NOT NULL,
	SOURCE_LONGITUDE CHAR(10) NOT NULL,
	DESTINATION_LATITUDE CHAR(10) NOT NULL,
	DESTINATION_LONGITUDE CHAR(10) NOT NULL,
	DESCRIPTION TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS TRAFFICLOG(
	ID INT PRIMARY KEY NOT NULL,
	ROUTEID NOT NULL,
	TIMEOFLOG INT NOT NULL,
	TRAVELTIMEMINUTES INT NOT NULL,
	FOREIGN KEY(ROUTEID) REFERENCES ROUTES(ID)
);
INSERT INTO ROUTES(ID,SOURCE_LATITUDE,SOURCE_LONGITUDE,
	DESTINATION_LATITUDE,DESTINATION_LONGITUDE,
	DESCRIPTION) VALUES (1,'17.401698','78.559886',
	'17.451102','78.380788','Uppal X Roads to Cyber Towers'
);
INSERT INTO ROUTES(ID,SOURCE_LATITUDE,SOURCE_LONGITUDE,
	DESTINATION_LATITUDE,DESTINATION_LONGITUDE,
	DESCRIPTION) VALUES (2,'17.451175','78.381589',
	'17.401933','78.560109','Cyber Towers to Uppal X Roads'
);