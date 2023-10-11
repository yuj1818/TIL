CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


-- 1)
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
-- 2)
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

-- 결과: 3
-- 1번은 ROLLBACK으로 인해 그 결과가 database에 반영되지 않음
-- 2번은 COMMIT으로 인해 그 결과가 database에 반영
-- eat필드 값이 ominivore인 column을 모두 삭제했으므로
-- 결과값은 3