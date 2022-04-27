DROP TABLE IF EXISTS animaux;
DROP TABLE IF EXISTS familles;
DROP TABLE IF EXISTS types;
DROP TABLE IF EXISTS animaux_types;
DROP TABLE IF EXISTS velages;
DROP TABLE IF EXISTS animaux_velages;
DROP TABLE IF EXISTS complications;
DROP TABLE IF EXISTS velages_complications;



CREATE TABLE animaux (
  id            INTEGER             NOT NULL,
  famille_id    INTEGER             NOT NULL,
  sexe          TEXT                NOT NULL,
  presence      TEXT                NOT NULL,
  apprivoise    TEXT                NOT NULL,
  mort_ne       TEXT                NOT NULL,
  decede        TEXT                NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (famille_id) REFERENCES familles(id)
);

CREATE TABLE familles (
  id            INTEGER             NOT NULL,
  nom           TEXT                NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE types (
  id            INTEGER             NOT NULL,
  type          TEXT                NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE animaux_types (
  animal_id     INTEGER             NOT NULL,
  type_id       INTEGER             NOT NULL,
  pourcentage   REAL                NOT NULL,
  PRIMARY KEY (animal_id,type_id),
  FOREIGN KEY (animal_id) REFERENCES animaux(id),
  FOREIGN KEY (type_id) REFERENCES types(id)
);

CREATE TABLE velages (
  id            INTEGER             NOT NULL,
  mere_id       INTEGER             NOT NULL,
  pere_id       INTEGER             NOT NULL,
  date          TEXT                NOT NULL,
  FOREIGN KEY (mere_id) REFERENCES animaux(id),
  FOREIGN KEY (pere_id) REFERENCES animaux(id),
  PRIMARY KEY (id)
);

CREATE TABLE animaux_velages (
  animal_id     INTEGER             NOT NULL,
  velage_id     INTEGER             NOT NULL,
  PRIMARY KEY (animal_id,velage_id),
  FOREIGN KEY (animal_id) REFERENCES animaux(id),
  FOREIGN KEY (velage_id) REFERENCES velages(id)
);

CREATE TABLE complications (
  id            INTEGER             NOT NULL,
  complication  TEXT                NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE velages_complications (
  velage_id        INTEGER             NOT NULL,
  complication_id  INTEGER             NOT NULL,
  PRIMARY KEY (complication_id,velage_id),
  FOREIGN KEY (complication_id) REFERENCES complications(id),
  FOREIGN KEY (velage_id) REFERENCES velages(id)
);