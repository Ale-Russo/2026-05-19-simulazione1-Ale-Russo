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

    @staticmethod
    def getPopularity(genere):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select distinct ar.ArtistId, sum(i.Quantity) as Popolarita
                    from artist ar,album al,track t, invoiceline i 
                    where ar.ArtistId = al.ArtistId
                    and t.AlbumId = al.AlbumId
                    and t.TrackId = i.TrackId
                    and t.GenreId = %s
                    group by ar.ArtistId"""

        cursor.execute(query, (genere,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAcquisti(genere):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select i.CustomerId, a.ArtistId
                    from invoice i, invoiceline iv, track t, album a
                    where i.InvoiceId = iv.InvoiceId
                    and iv.TrackId = t.TrackId
                    and t.AlbumId = a.AlbumId
                    and t.GenreId = %s
                    group by i.CustomerId, a.ArtistId"""

        cursor.execute(query, (genere,))
        for row in cursor:
            result.append((row["CustomerId"], row["ArtistId"]))
        cursor.close()
        conn.close()
        return result