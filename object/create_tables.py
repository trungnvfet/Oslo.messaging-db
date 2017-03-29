
users = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(60) NOT NULL,
         LAST_NAME  CHAR(60),
         AGE INT,  
         SEX CHAR(60),
         INCOME FLOAT )"""

domains = """CREATE TABLE domains (
          id                    INT PRIMARY KEY,
          name                  VARCHAR(255) NOT NULL,
          master                VARCHAR(128) DEFAULT NULL,
          last_check            INT DEFAULT NULL,
          type                  VARCHAR(6) NOT NULL,
          notified_serial       INT DEFAULT NULL,
          account               VARCHAR(40) DEFAULT NULL
)"""