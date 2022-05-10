create database aula_rad

use aula_rad

create table xpto
( cod int primary key identity,
	descricao varchar (30) not null,
	flag int
)

1:N

alter table xpto add qqcoisa varchar(10)

alter table xpto drop column qqcoisa

insert into xpto (descricao,flag) values ('teste2', 22)
insert into xpto (descricao,flag) values ('teste3', 33)
insert into xpto (descricao,flag) values ('teste4', 44)
insert into xpto (descricao,flag) values ('teste5', 55)


create table xpto_filha
( cod int primary key identity,
	cod_pai int,
	descricao varchar (30) not null,
	valor int,
	constraint fk_pai foreign key(cod_pai) references xpto(cod)
)

insert into xpto_filha (descricao,cod_pai,valor) values ('juliano',null,10)
insert into xpto_filha (descricao,cod_pai,valor) values ('maria',cod, 22)
insert into xpto_filha (descricao,cod_pai,valor) values ('joao', , 44)
insert into xpto_filha (descricao,cod_pai,valor) values ('joana', , 55.55)


select * from xpto
select * from xpto_filha







delete from xpto
delete from xpto_filha

drop table xpto
drop table xpto_filha
