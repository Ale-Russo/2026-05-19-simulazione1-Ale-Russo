from database.DB_connect import DBConnect
from model.artista import artista


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select * 
                    from genre g
                    order by Name"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllArtists():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select * 
                        from artist
                        """
        cursor.execute(query)

        for row in cursor:
            result.append(artista(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllNodes(genreId, idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select distinct ar.ArtistId 
                    from artist ar, album al, track t 
                    where ar.ArtistId = al.ArtistId and 
                    t.AlbumId = al.AlbumId 
                    and t.GenreId = %s"""

        cursor.execute(query, (genreId,))

        for row in cursor:
            result.append(idMapA[row["ArtistId"]])

        cursor.close()
        conn.close()
        return result