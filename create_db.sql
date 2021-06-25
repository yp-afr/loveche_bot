create table if not exists items
(
    id serial PRIMARY KEY,
    author_id integer not null,
    author_username varchar(50) not null,
    photo varchar(255),
    caption varchar(255) not null,
    type varchar(50) not null,
    category varchar(50) not null,
    posted TIMESTAMP
);

create table if not exists admins
(
    id serial primary key,
    admin_id varchar(50) not null unique
);