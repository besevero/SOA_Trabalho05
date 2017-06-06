CREATE TABLE Artigo (
 id_artigo INT NOT NULL,
 nome VARCHAR(200),
 tipoArtigo VARCHAR(1)
);

ALTER TABLE Artigo ADD CONSTRAINT PK_Artigo PRIMARY KEY (id_artigo);


CREATE TABLE Autor (
 id_autor INT NOT NULL,
 nome VARCHAR(200),
 cpf VARCHAR(11) not null
);

ALTER TABLE Autor ADD CONSTRAINT PK_Autor PRIMARY KEY (id_autor);


CREATE TABLE AutorArtigo (
 id_autor INT NOT NULL,
 id_artigo INT NOT NULL
);

ALTER TABLE AutorArtigo ADD CONSTRAINT PK_AutorArtigo PRIMARY KEY (id_autor,id_artigo);


CREATE TABLE Forum (
 id_forum INT NOT NULL,
 nome VARCHAR(200),
 sigla VARCHAR(10)
);

ALTER TABLE Forum ADD CONSTRAINT PK_Forum PRIMARY KEY (id_forum);


CREATE TABLE Local (
 id_local INT NOT NULL,
 cidade VARCHAR(50)
);

ALTER TABLE Local ADD CONSTRAINT PK_Local PRIMARY KEY (id_local);


CREATE TABLE Qualis (
 id_qualis INT NOT NULL,
 codQualis VARCHAR(2),
 peso INT
);

ALTER TABLE Qualis ADD CONSTRAINT PK_Qualis PRIMARY KEY (id_qualis);


CREATE TABLE Edicao (
 id_edicao INT NOT NULL,
 id_forum INT NOT NULL,
 id_qualis INT NOT NULL,
 id_local INT NOT NULL,
 ano INT
);

ALTER TABLE Edicao ADD CONSTRAINT PK_Edicao PRIMARY KEY (id_edicao,id_forum,id_qualis,id_local);


CREATE TABLE ArtigoEdicao (
 id_edicao INT NOT NULL,
 id_forum INT NOT NULL,
 id_qualis INT NOT NULL,
 id_local INT NOT NULL,
 id_artigo INT NOT NULL
);

ALTER TABLE ArtigoEdicao ADD CONSTRAINT PK_ArtigoEdicao PRIMARY KEY (id_edicao,id_forum,id_qualis,id_local,id_artigo);


ALTER TABLE AutorArtigo ADD CONSTRAINT FK_AutorArtigo_0 FOREIGN KEY (id_autor) REFERENCES Autor (id_autor);
ALTER TABLE AutorArtigo ADD CONSTRAINT FK_AutorArtigo_1 FOREIGN KEY (id_artigo) REFERENCES Artigo (id_artigo);


ALTER TABLE Edicao ADD CONSTRAINT FK_Edicao_0 FOREIGN KEY (id_forum) REFERENCES Forum (id_forum);
ALTER TABLE Edicao ADD CONSTRAINT FK_Edicao_1 FOREIGN KEY (id_qualis) REFERENCES Qualis (id_qualis);
ALTER TABLE Edicao ADD CONSTRAINT FK_Edicao_2 FOREIGN KEY (id_local) REFERENCES Local (id_local);


ALTER TABLE ArtigoEdicao ADD CONSTRAINT FK_ArtigoEdicao_0 FOREIGN KEY (id_edicao,id_forum,id_qualis,id_local) REFERENCES Edicao (id_edicao,id_forum,id_qualis,id_local);
ALTER TABLE ArtigoEdicao ADD CONSTRAINT FK_ArtigoEdicao_1 FOREIGN KEY (id_artigo) REFERENCES Artigo (id_artigo);



--select a.nome from artigo b, artigoEdicao c, autorArtigo d, autor a where b.id_artigo = c.id_artigo and b.id_artigo = d.id_artigo and 
--a.id_autor = d.id_autor and b.id_artigo=1;


