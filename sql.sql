CREATE TABLE aulas.cliente (
	idcliente INT auto_increment NULL,
	nome varchar(100) NULL,
	endereco varchar(100) NULL,
	uf varchar(100) NULL,
	cep varchar(100) NULL,
	nascimento varchar(100) NULL,
	cidade varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
