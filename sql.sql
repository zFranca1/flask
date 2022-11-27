CREATE TABLE aulas.evento (
	idevento INT auto_increment NULL,
	nome varchar(100) NULL,
	descricao varchar(100) NULL,
	CONSTRAINT evento_PK PRIMARY KEY (idevento)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.palestrante (
	idpalestrante INT auto_increment NULL,
	nome varchar(100) NULL,
	email varchar(100) NULL,
	cpf varchar(100) NULL,
	CONSTRAINT palestrante_PK PRIMARY KEY (idpalestrante)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.semana (
	idsemana INT auto_increment NULL,
	nome varchar(100) NULL,
	datainicio varchar(100) NULL,
	datatermino varchar(100) NULL,
	CONSTRAINT semana_PK PRIMARY KEY (idsemana)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE aulas.participante (
	idparticipante INT auto_increment NULL,
	nome varchar(100) NULL,
	email varchar(100) NULL,
	cpf varchar(100) NULL,
	CONSTRAINT participante_PK PRIMARY KEY (idparticipante)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

