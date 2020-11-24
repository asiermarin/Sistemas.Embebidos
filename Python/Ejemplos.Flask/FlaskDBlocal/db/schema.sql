BEGIN TRANSACTION;

/* Tabla que almacena los sensores y su modelo*/
CREATE TABLE IF NOT EXISTS `sensors` (
	`sensorid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`description`	TEXT,
	`model`	TEXT
);
INSERT INTO `sensors` VALUES (1,'Luz','modelo-luz');
INSERT INTO `sensors` VALUES (2,'Temperatura','modelo-temp');
INSERT INTO `sensors` VALUES (3,'Aceleracion','modelo-acel');
INSERT INTO `sensors` VALUES (4,'Presion','modelo-presion');

/* -------------------------------------------------------------------------*/

/* Tabla que almacena las diferentes unidades asociadas al sensor
Un mismo sensor puede proporcionar medidas en diferentes unidades*/
CREATE TABLE IF NOT EXISTS `measurements` (
	`measurementid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`sensorid`	INTEGER,
	`unit`	TEXT
	
);
INSERT INTO `measurements` VALUES (1,2,'grados centigrados');
INSERT INTO `measurements` VALUES (2,2,'farenheit');
INSERT INTO `measurements` VALUES (3,1,'LUX-visible');
INSERT INTO `measurements` VALUES (4,1,'LUX-completo');
INSERT INTO `measurements` VALUES (5,3,'m/s2');
INSERT INTO `measurements` VALUES (6,4,'pascal');

/* -------------------------------------------------------------------------*/
/* Tabla para guardar las medidas asociadas a un sensor con su correspondiente unidad*/
CREATE TABLE IF NOT EXISTS `measurement-values` (
	`measurement-valueid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`measurementid`	INTEGER,
	`value`	INTEGER,
	`datetime`	TEXT
);
INSERT INTO `measurement-values` VALUES (1,5,22,'fecha-hora'); 
INSERT INTO `measurement-values` VALUES (2,5,24,'fecha-hora');
INSERT INTO `measurement-values` VALUES (3,5,10,"fecha-hora");
INSERT INTO `measurement-values` VALUES (4,1,25,'fecha-hora'); /* 25 grados centigrados*/
INSERT INTO `measurement-values` VALUES (5,2,80,'fecha-hora'); /* 80 grados farenheit*/
INSERT INTO `measurement-values` VALUES (6,6,101325,'hoy'); /* presion atmosferica en pascales*/
INSERT INTO `measurement-values` VALUES (7,6,50000,'ayer'); /* presion atmosferica en pascales*/


COMMIT;



