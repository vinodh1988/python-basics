select * from employees;
select first_name, last_name from employees;
select concat(first_name,last_name) as Name,hire_date from employees;
select distinct department_id from employees;
select * from employees where salary > 5000;
select * from employees where job_id=10;
select * from employees where job_id in (10,11,12);
select * from  employees where hire_date between '1990-1-1' and '1995-12-31';
select * from employees where first_name between 'A' and 'Kz';
select * from employees where first_name like 'A%';
select * from employees where salary> 5000 and department_id in (1,2,3,4,5);

update employees set hire_date = hire_date + interval '5000' day;

select first_name, to_char(hire_date, 'YYYY-MM-DD') as formatted_hire_date from employees;

select first_name, last_name, concat('$', format(salary, 2)) as salary_in_dollar from employees;

select department_id,max(salary) from employees group by department_id;
select  job_id , count(*) from employees group by job_id;
select  job_id , count(*) from employees group by job_id having count(*)>=2;
select job_id , count(*) from employees where salary> 7000 
group by job_id having count(*) >=3 order by job_id desc ;

create table testplayer (
    player_id int primary key,
    player_name varchar(50),
    test_runs int
);

create table onedayplayer (
    player_id int primary key,
    player_name varchar(50),
    odi_runs int
);

insert into testplayer (player_id, player_name, test_runs) values
(1, 'Sachin', 15921),
(2, 'Dravid', 13288),
(3, 'Lara', 11953),
(4, 'Ponting', 13378),
(5, 'Kallis', 13289),
(6, 'Cook', 12472),
(7, 'Gavaskar', 10122),
(8, 'Border', 11174);

insert into onedayplayer (player_id, player_name, odi_runs) values
(1, 'Sachin', 18426),
(3, 'Lara', 10405),
(4, 'Ponting', 13704),
(5, 'Kallis', 11579),
(6, 'Cook', 3204),
(8, 'Border', 6524),
(9, 'Dhoni', 10773),
(10, 'Kohli', 12898);

-- Example outer join
select t.player_id, t.player_name as test_name, t.test_runs, o.player_name as odi_name, o.odi_runs
from testplayer t
full outer join onedayplayer o on t.player_id = o.player_id;
