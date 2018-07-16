from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://ucurzlfkjmcwqf:0ef9496e10a6f8fd80f6af62bc2c7b200a7f1e6b08f20ba815d9bbc9be550518@ec2-54-227-240-7.compute-1.amazonaws.com:5432/dct3cpbvs21gfs")
db = scoped_session(sessionmaker(bind=engine))


def create_table_user():
    db.execute(
        """
        CREATE TABLE user_info (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            register_date DATE NOT NULL
        );
        """

    )
    db.commit()

def create_table_notes():
    db.execute(
        """
        CREATE TABLE notes (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            note VARCHAR(255) NOT NULL
        );
        """

    )
    db.commit()

def notes():
    array = db.execute("SELECT * FROM notes").fetchall()
    print(array)

def users():
    users = db.execute("SELECT * FROM user_info").fetchall()
    for user in users:
        print(user.username,user.password)

users()
print("success")
