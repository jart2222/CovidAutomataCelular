select * from espacios as e inner join 
persona as p on (p.id_espacio=e.id_espacio) 
where p.id_espacio=0 and p.ubicacionX=5 and p.ubicacionY=7;

select * from espacios as e inner join 
persona as p on (p.id_espacio=e.id_espacio) where p.id_espacio=1;

SELECT id_persona, edad, casa, trasporte, trabajo,id_espacio, etapa  FROM covid19_automatas.persona where id_persona=0;
SELECT id_espacio  FROM covid19_automatas.persona where id_persona=0;


SELECT * FROM covid19_automatas.espacios where id_espacio
 in (SELECT id_espacio  FROM covid19_automatas.persona where id_persona=0);	
