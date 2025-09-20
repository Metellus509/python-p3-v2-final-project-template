from models.__init__ import CURSOR, CONN


class Actor:
    all = {}

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return (f'<Actor:{self.id},{self.name},{self.age}>')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name should be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError("Age should be an integer")

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS actors(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
        )"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS actors;"""
        CURSOR.execute(sql)
        CONN.commit()

        #sql = """
        #DROP TABLE IF EXISTS movie_actor;"""
        #CURSOR.execute(sql)
        #CONN.commit()

    def save(self):
        sql = """ INSERT INTO actors(name,age) VALUES (?,?)"""
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE actors
            SET name = ?, age = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age,
                             self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM actors WHERE id =?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #sql = """DELETE FROM movie_actor where actor_id=?"""
        #CURSOR.execute(sql, (self.id,))
        #CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, age):
        actor = cls(name, age)
        actor.save()
        return actor

    @classmethod
    def instance_from_db(cls, row):

        actor = cls.all.get(row[0])
        if actor:
            actor.name = row[1]
            actor.age = row[2]
        else:
            actor = cls(row[1], row[2])
            actor.id = row[0]
            cls.all[actor.id] = actor
        return actor

    @classmethod
    def get_all(cls):
        sql = """ SELECT * FROM actors """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM actors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM actors
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def movies(self):
        """Return list of movies associated with current actor"""
        from models.movie import Movie
        sql = """
            SELECT * FROM movies
            WHERE actor_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Movie.instance_from_db(row) for row in rows
        ]

    