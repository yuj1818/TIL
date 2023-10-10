CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');

INSERT INTO articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO articles (title, content, createdAt)
VALUES ('mytitle', 'mycontent', DATE());

UPDATE articles
SET title = 'update Title'
WHERE id = 1;

UPDATE articles
SET title = 'update Title', content = 'update Content'
WHERE id = 2;

UPDATE articles
SET title = 'update title', content = 'update content'
WHERE id = 3;

SELECT * FROM articles
ORDER BY id DESC;

DELETE FROM articles
WHERE id = 1;

DELETE FROM articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);

SELECT * FROM albums;

DELETE FROM albums
WHERE AlbumId = 5;