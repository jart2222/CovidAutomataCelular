SELECT * FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and persona>='0';
SELECT *, CONCAT(nombre," ",  id_espacio) As identificador FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and personas_contenidas>0;

select * from covid19_automatas.persona where id_espacio in 
(SELECT id_espacio FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and personas_contenidas>0) and etapa=0;

select*,  CONCAT("Edad ",  edad) As identificador from covid19_automatas.persona where etapa=0;


select * from covid19_automatas.persona where id_persona=2;

select * from covid19_automatas.persona where trasporte=10;