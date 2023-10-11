CREATE TABLE hotel (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL
);

ALTER TABLE hotel
ADD COLUMN price INTEGER NOT NULL DEFAULT 0;

INSERT INTO hotel (room_num, check_in, check_out, grade, price) VALUES
('B203', '2021-12-31', '2022-01-03', 'suite', 900),
('1102', '2022-01-04', '2022-01-08', 'suite', 850),
('303', '2022-01-01', '2022-01-03', 'deluxe', 500),
('807', '2021-01-04', '2022-01-07', 'superior', 300),
('B205', '2022-01-04', '2022-01-07', 'deluxe', 550);

UPDATE hotel SET check_in='2022-01-04'
WHERE room_num='807';

SELECT * FROM hotel
WHERE room_num LIKE 'B%' OR grade='deluxe';