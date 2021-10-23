import sqlite3

conn = sqlite3.connect('pubsub.db')
c = conn.cursor()
#
# c.execute("DROP table eventBroker")
# c.execute("DROP table publisher")
# c.execute("DROP table subscriber")
#
# c.execute("""CREATE TABLE IF NOT EXISTS eventBroker(
#         eid INTEGER PRIMARY KEY,
#         eventData TEXT)
#         """)
#
# c.execute("INSERT INTO eventBroker VALUES(1,'Nothing new to see. Please publish!')")
# c.execute("INSERT INTO eventBroker VALUES(2,'Nothing new to see. Please publish!')")
# c.execute("INSERT INTO eventBroker VALUES(3,'Nothing new to see. Please publish!')")
#
# c.execute("""CREATE TABLE IF NOT EXISTS publisher(
#         pid TEXT,
#         eid INTEGER,
#         advertisement INTEGER DEFAULT 0)
#         """)
#
# c.execute("""CREATE TABLE IF NOT EXISTS subscriber(
#         sid TEXT,
#         eid INTEGER,
#         subscription INTEGER DEFAULT 0,
#         notification INTEGER DEFAULT 0)
#         """)


############################################################################
# queries

# c.execute("UPDATE eventBroker set eventData = ? WHERE eid = ?", (ev1,1))
# c.execute("SELECT * from eventBroker")
# print(c.fetchall())

# pid = 'asdasd'
# eid = 3
# c.execute("INSERT INTO publisher VALUES(?,?,?)",(pid,eid,1))
# c.execute("UPDATE publisher SET advertisement = 0 WHERE pid = ? AND eid = ?", (pid, eid))
# c.execute("SELECT * FROM publisher")
# print(c.fetchall())

# sid1 = 'aaaa'
# sid2 = 'bbbb'
# sid3 = 'cccc'
# eid1 = 1
# eid2 = 2
# c.execute("INSERT INTO SUBSCRIBER VALUES(?,?,?,?)", (sid1, 1, 0, 0))
# c.execute("INSERT INTO SUBSCRIBER VALUES(?,?,?,?)", (sid2, 2, 0, 0))
# c.execute("INSERT INTO SUBSCRIBER VALUES(?,?,?,?)", (sid2, 1, 0, 0))
#
# c.execute("UPDATE subscriber SET notification = 1 WHERE eid = ?", str(eid2))
# c.execute("UPDATE subscriber SET notification = 1 WHERE eid = ?", str(eid1))
# c.execute("SELECT DISTINCT * FROM subscriber WHERE sid = ? AND notification = 1", (sid2,))
# print(c.fetchall())

conn.commit()
conn.close()


#######################################################################
