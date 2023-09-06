USE crypto;

CREATE TABLE Cryptocurrencies(
    crypto_id INT NOT NULL AUTO_INCREMENT,
    crypto_name VARCHAR(255) NOT NULL,
    symbol VARCHAR(10),
    main_link VARCHAR(255),
    historical_link VARCHAR(255),
    github_link VARCHAR(255),
    rnk INT,
    PRIMARY KEY (crypto_id)
);

CREATE TABLE Tags (
  tag_id INT NOT NULL AUTO_INCREMENT,
  tag_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (tag_id)
);

CREATE TABLE CryptoTags (
    crypto_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (crypto_id, tag_id),
    FOREIGN KEY (crypto_id) REFERENCES Cryptocurrencies(crypto_id),
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id)
);

CREATE TABLE Dates (
    date_id INT NOT NULL AUTO_INCREMENT,
    date DATE UNIQUE,
    PRIMARY KEY (date_id)
);

CREATE TABLE CryptoDailyHistory (
    crypto_daily_id INT NOT NULL AUTO_INCREMENT,
    crypto_id INT NOT NULL ,
    date_id INT NOT NULL,
    market_cap DOUBLE PRECISION,
    volume DOUBLE PRECISION,
    circulating_supply BIGINT,
    PRIMARY KEY (crypto_daily_id),
    FOREIGN KEY (crypto_id) REFERENCES Cryptocurrencies(crypto_id),
    FOREIGN KEY (date_id) REFERENCES Dates(date_id)
);

CREATE TABLE CryptoPriceTypes (
    crypto_price_type_id INT NOT NULL AUTO_INCREMENT,
    crypto_price_type_name ENUM('Open', 'Close', 'Low', 'High'),
    PRIMARY KEY (crypto_price_type_id)
);

CREATE TABLE CryptoPriceTimes (
    crypto_price_time_id INT NOT NULL AUTO_INCREMENT,
    crypto_daily_id INT NOT NULL,
    crypto_price_type_id INT NOT NULL,
    crypto_price_time TIME(3),
    PRIMARY KEY (crypto_price_time_id),
    FOREIGN KEY (crypto_daily_id) REFERENCES CryptoDailyHistory(crypto_daily_id),
    FOREIGN KEY (crypto_price_type_id) REFERENCES CryptoPriceTypes(crypto_price_type_id)
);


CREATE TABLE CryptoHistoricalPrices (
    id INT NOT NULL AUTO_INCREMENT,
    crypto_price_time_id INT NOT NULL,
    crypto_price DOUBLE PRECISION,
    PRIMARY KEY (id),
    FOREIGN KEY (crypto_price_time_id) REFERENCES CryptoPriceTimes(crypto_price_time_id)
);

