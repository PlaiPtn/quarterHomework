USE mans_friends;
CREATE TABLE animals(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    Animal_group VARCHAR(30) NOT NULL
);

CREATE TABLE  packAnimals(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    Animal_Id INT,
    Animal_species VARCHAR(30) NOT NULL,
    FOREIGN KEY (Animal_Id) REFERENCES animals (Id)
);

CREATE TABLE  homeAnimals(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    Animal_Id INT,
    Animal_species VARCHAR(30),
    FOREIGN KEY (Animal_Id) REFERENCES animals (Id)
);

CREATE TABLE dog(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    HomeAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (HomeAnimals_Id) REFERENCES homeAnimals (Id)
);

CREATE TABLE cat(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    HomeAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (HomeAnimals_Id) REFERENCES homeAnimals (Id)
);

CREATE TABLE hamster(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    HomeAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (HomeAnimals_Id) REFERENCES homeAnimals (Id)
);

CREATE TABLE horse(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    PackAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (PackAnimals_Id) REFERENCES packAnimals (Id)
);

CREATE TABLE camel(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    PackAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (PackAnimals_Id) REFERENCES packAnimals (Id)
);

CREATE TABLE donkey(
	Id INT PRIMARY KEY AUTO_INCREMENT,
    PackAnimals_Id INT,
	Name VARCHAR(30) NOT NULL,
	Command TEXT NOT NULL,
	Birthday DATE NOT NULL,
    FOREIGN KEY (PackAnimals_Id) REFERENCES packAnimals (Id)
);

INSERT INTO animals(Animal_group) values
    ('Вьючные животные'),
    ('Домашние животные');

INSERT INTO packAnimals(Animal_Id, Animal_species) values
	(1, 'Лошадь'),
    (1, 'Верблюд'),
    (1, 'Осел');
    
INSERT INTO homeAnimals(Animal_Id, Animal_species) values
	(2, 'Собака'),
    (2, 'Кошка'),
    (2, 'Хомяк');

INSERT INTO dog (HomeAnimals_Id, Name, Command, Birthday) values 
	(1, 'Рада', 'Сидеть', '2018-07-27'),
	(1, 'Эля', 'Кушать', '2020-10-11'),
	(1, 'Бэти', 'Рядом', '2015-11-01');

INSERT INTO cat (HomeAnimals_Id, Name, Command, Birthday) values 
	(2, 'Оззи', 'Кушать', '2023-03-27'),
	(2, 'Звездочет', 'Брысь', '2021-08-11'),
	(2, 'Луна', 'Спать', '2012-03-01');

INSERT INTO hamster (HomeAnimals_Id, Name, Command, Birthday) values 
	(3, 'Беляк', 'Бегать', '2015-11-22'),
	(3, 'Хром', 'Кушать', '2021-08-11'),
	(3, 'Грок', 'Плавать', '2015-03-01');

INSERT INTO horse (PackAnimals_Id, Name, Command, Birthday) values 
	(1, 'Плотва', 'Стоять', '2013-07-27'),
	(1, 'Рысь', 'Галоп', '2022-10-11'),
	(1, 'Крош', 'Прыжок', '2016-04-01');

INSERT INTO camel (PackAnimals_Id, Name, Command, Birthday) values 
	(2,'Коти', 'Кушать', '2018-12-27'),
	(2,'Горбун', 'Вперед', '2020-09-19'),
	(2,'Гена', 'Стоять', '2015-03-24');

INSERT INTO donkey (PackAnimals_Id, Name, Command, Birthday) values 
	(3, 'Осел', 'Стоять', '2017-10-21'),
	(3, 'Медляк', 'Кушать', '2020-05-09'),
	(3, 'Стрела', 'Идти', '2013-11-03');

DROP TABLE IF EXISTS camel;

CREATE TABLE pack_animals AS
	SELECT Name, Command, Birthday from horse
	UNION ALL SELECT Name, Command, Birthday from donkey;



CREATE TABLE young_animals AS
	SELECT Name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) as Birthday_month 
	FROM dog WHERE TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) >= 1
	  AND TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) < 3
	UNION ALL SELECT Name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) as Birthday_month
	 FROM cat WHERE TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) >= 1
	  AND TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) < 3
	UNION ALL SELECT Name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) as Birthday_month 
	FROM hamster WHERE TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) >= 1
	  AND TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) < 3
	UNION ALL SELECT Name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) as Birthday_month 
	FROM pack_animals WHERE TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) >= 1
	  AND TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) < 3;
  
CREATE TABLE all_animals AS
SELECT Name, Command, Birthday, 'dog' as animal_species FROM dog
UNION ALL SELECT Name, Command, Birthday, 'cat' as animal_species FROM cat
UNION ALL SELECT Name, Command, Birthday, 'hamster' as animal_species FROM hamster
UNION ALL SELECT Name, Command, Birthday, 'horse' as animal_species FROM horse
UNION ALL SELECT Name, Command, Birthday, 'donkey' as animal_species FROM donkey;







