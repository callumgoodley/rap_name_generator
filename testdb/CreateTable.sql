CREATE TABLE IF NOT EXISTS users
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          first_name VARCHAR(30) NOT NULL,
                          last_name  VARCHAR(30) NOT NULL,
                          rapper_name      VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

