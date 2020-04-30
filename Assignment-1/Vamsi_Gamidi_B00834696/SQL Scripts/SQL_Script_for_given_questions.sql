SELECT Faculty, count(Faculty) FROM mydb.faculty
where Last_Name like "A%"
group by Faculty
order by count(Faculty) desc;

SELECT faculty, count(program) FROM mydb.undergrad_programs
group by faculty
order by count(program) desc
limit 1;

