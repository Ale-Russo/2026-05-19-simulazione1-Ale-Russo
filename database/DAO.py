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
    def getAllNodes(n, idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.ID, t.IATA_CODE, count(*) as N
                        FROM (select a.ID, a.IATA_CODE, f.AIRLINE_ID, count(*)
                        from airports a, flights f
                        where a.ID = f.ORIGIN_AIRPORT_ID 
                        or a.ID = f.DESTINATION_AIRPORT_ID 
                        GROUP BY a.ID, a.IATA_CODE, f.AIRLINE_ID ) t
                        GROUP BY t.ID, t.IATA_CODE
                        having N >= %s
                        order by N asc"""

        cursor.execute(query, (n,))

        for row in cursor:
            result.append(idMapA[row["ID"]])

        cursor.close()
        conn.close()
        return result