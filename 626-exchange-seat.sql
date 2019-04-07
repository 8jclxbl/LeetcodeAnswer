select s.id , s.student from
(
select id-1 as id ,student from seat where mod(id,2)=0
union
select id+1 as id,student from seat where mod(id,2)=1 and id !=(select count(*) from seat)
union
select id,student from seat where mod(id,2)=1 and id = (select count(*) from seat)
) s order by id;

select (case
      when mod(id,2)!=0 and id!=counts then id+1
      when mod(id,2)!=0 and id=counts then id
      else id-1 end)as id,student
      from seat,(select count(*)as counts from seat)as seat_counts
                order by id;
