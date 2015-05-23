select * from online_history as a
    where a.id = (select max(id) from online_history where user_id = a.user_id group by user_id)
    group by user_id;
