CREATE SCHEMA IF NOT EXISTS ispc;
SET search_path TO ispc, public;

CREATE TABLE "USERS"(
	id_user serial PRIMARY KEY,
	name varchar(64),
	email varchar(320),
	pwd varchar(256)
);

/* A futuro se pueden expandir con campos como:
 * dni
 * is_active (definir si la cuenta tiene que estar activa o no)
 * cretion_time (para saber cuando se creo)
 */

select * from ispc."USERS";


SET search_path TO ispc, public;

INSERT INTO "USERS" (name, email, pwd)
VALUES (
    'Admin Test',
    'admin@test.com',
    '$2b$12$Kx8J1zQmN9vL3pY7wR5uOeHtGfDcBaXsIqMnPjUyVkWoEhCrTlAs'
);
UPDATE ispc."USERS"
SET pwd = '$2b$12$D0k7ipYq5TfGgDFN1fcwgeA1JbBac4lpPVMremyzwYLCEIIdxoi0a'
WHERE email = 'admin@test.com';


-- Verificar que se insertó
SELECT * FROM ispc."USERS";