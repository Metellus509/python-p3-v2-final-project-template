from models.__init__ import CURSOR, CONN


class Movie:
    all = {}

    def __init__(self, name, prod_year, actor_id, id=None):
        self.id = id
        self.name = name
        self.prod_year = prod_year
        self.actor_id = actor_id

    def __repr__(self):
        return (f'<Movie : {self.id},{self.name},{self.prod_year},{self.actor_id}>')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Should be a string")

    @property
    def prod_year(self):
        return self._prod_year

    @prod_year.setter
    def prod_year(self, value):
        if isinstance(value, int) and (1900 < value <= 2025):
            self._prod_year = value
        else:
            raise ValueError("Should be an integer")
    
    @property
    def actor_id(self):
        return self._actor_id

    @actor_id.setter
    def actor_id(self, value):
        if isinstance(value, int):
            self._actor_id = value
        else:
            raise ValueError("Should be an integer")

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        prod_year INTEGER NOT NULL,
        actor_id INTEGER NOT NULL,
        FOREIGN KEY (actor_id) REFERENCES actors(id)
        )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS movies
        """
        CURSOR.execute(sql)
        CONN.commit()

        #sql = """
        #DROP TABLE IF EXISTS movie_actor
        #"""
        #CURSOR.execute(sql)
        #CONN.commit()

    def save(self):
        sql = """INSERT INTO movies(name,prod_year,actor_id) VALUES (?,?,?)"""
        CURSOR.execute(sql, (self.name, self.prod_year,self.actor_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE movies
            SET name = ?, prod_year = ?, actor_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.prod_year,self.actor_id,
                             self.id))
        CONN.commit()



    def delete(self):
        sql = """DELETE FROM movies WHERE id=?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #sql = """DELETE FROM movie_actor where movie_id=?"""
        #CURSOR.execute(sql, (self.id,))
        #CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, year,actor_id):
        movie = cls(name, year,actor_id)
        movie.save()
        return movie

    @classmethod
    def instance_from_db(cls, row):

        movie = cls.all.get(row[0])
        if movie:
            movie.name = row[1]
            movie.prod_year = row[2]
            movie.actor_id = row[3]
        else:
            movie = cls(row[1], row[2],row[3])
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movies
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM movies
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM movies
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
