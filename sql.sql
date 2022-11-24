CREATE TABLE aulas.evento (
	idevento INT auto_increment NULL,
	nome varchar(100) NULL,
	descricao varchar(100) NULL,
	CONSTRAINT evento_PK PRIMARY KEY (idevento)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
