CREATE TABLE aulas.evento (
	idevento INT auto_increment,
	nome varchar(100),
	descricao varchar(100),
	CONSTRAINT evento_PK PRIMARY KEY (idevento)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.palestrante (
	idpalestrante INT auto_increment,
	nome varchar(100),
	email varchar(100),
	cpf varchar(100),
	CONSTRAINT palestrante_PK PRIMARY KEY (idpalestrante)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.semana (
	idsemana INT auto_increment,
	nome varchar(100),
	datainicio varchar(100),
	datatermino varchar(100),
	CONSTRAINT semana_PK PRIMARY KEY (idsemana)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.participante (
	idparticipante INT auto_increment,
	nome varchar(100),
	email varchar(100),
	cpf varchar(100),
	CONSTRAINT participante_PK PRIMARY KEY (idparticipante)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.eventoxparticipante (
	idevento INT,
	idparticipante INT,
	CONSTRAINT eventoxparticipante_PK PRIMARY KEY (idevento,idparticipante)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.eventoxpalestrante (
	idevento INT,
	idpalestrante INT,
	idsemana INT,
	CONSTRAINT eventoxpalestrante_PK PRIMARY KEY (idevento,idpalestrante,idsemana)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

ALTER TABLE aulas.evento ADD `data` varchar(100);
ALTER TABLE aulas.evento ADD horario varchar(100);
ALTER TABLE aulas.evento ADD idsemana INT;
ALTER TABLE aulas.evento ADD `local` varchar(100);
ALTER TABLE aulas.evento ADD idpalestrante INT;
ALTER TABLE aulas.semana ADD descricao varchar(100);
ALTER TABLE aulas.semana ADD `local` varchar(100);



