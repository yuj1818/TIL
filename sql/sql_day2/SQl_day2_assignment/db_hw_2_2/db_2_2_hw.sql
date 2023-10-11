CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 데이터 입력 순서가 달라 에러가 발생하진 않지만 저장 된 값이 의도한 바와 다르게 저장됨
--    필드 목록을 작성함으로써 원하는 필드에 데이터가 저장되도록 함
INSERT INTO zoo (age, height, weight, name, eat) VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) zoo 테이블에 rowid라는 필드가 존재하지 않아서 발생
--    rowid 필드를 추가하거나 추가하고자 하는 값에서 rowid를 빼면 에러 해결
INSERT INTO zoo (name, eat, weight, age) VALUES
--(10,'dolphin', 'carnivore', 210, 3),
--(10, 'alligator', 'carnivore', 250, 50);
('dolphin', 'carnivore', 210, 3),
('alligator', 'carnivore', 250, 50);

-- 3) weight가 null값이 허용되지 않으므로 데이터를 입력할 때, 반드시 not null인 필드에 값을 입력해주어야 함
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 210);
