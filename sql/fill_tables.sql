CREATE EXTENSION pgcrypto;

INSERT INTO movies (id, name, rating)
VALUES 
    (gen_random_uuid(), 'Titanic', 97),
    (gen_random_uuid(), 'Matrix', 91),
    (gen_random_uuid(), 'Toy Story', 85),
    (gen_random_uuid(), 'Oppenheimer', 94);