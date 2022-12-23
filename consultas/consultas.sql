select * from espacios as e inner join 
persona as p on (p.id_espacio=e.id_espacio) 
where p.id_espacio=0 and p.ubicacionX=5 and p.ubicacionY=7;

select * from espacios as e inner join 
persona as p on (p.id_espacio=e.id_espacio) where p.id_espacio=1;