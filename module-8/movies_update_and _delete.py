UPPDATE player
SET team_id = 2,
    first_name = 'Tiger',
    last_name = 'Woods'
WHERE first_name = 'GOAT';

DELETE FROM player
WHERE first_name = 'GOAT';

INSERT INTO player (first_name, last_name, team_id)
    VALUES('GOAT', 'Golfers', 1);