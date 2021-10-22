import sqlite3

conn = sqlite3.connect('pubsub.db')
c = conn.cursor()

# c.execute("DROP table eventBroker")
# c.execute("DROP table publisher")
# c.execute("DROP table subscriber")
#
# c.execute("""CREATE TABLE IF NOT EXISTS eventBroker(
#         eid INTEGER PRIMARY KEY,
#         eventData TEXT)
#         """)
#
# c.execute("INSERT INTO eventBroker VALUES(1,'')")
# c.execute("INSERT INTO eventBroker VALUES(2,'')")
# c.execute("INSERT INTO eventBroker VALUES(3,'')")
#
# c.execute("""CREATE TABLE IF NOT EXISTS publisher(
#         pid TEXT,
#         eid INTEGER,
#         advertisement INTEGER,
#         CONSTRAINT publisher_c UNIQUE (pid,eid))
#         """)
#
# c.execute("""CREATE TABLE IF NOT EXISTS subscriber(
#         sid TEXT,
#         eid INTEGER,
#         subscription INTEGER,
#         notification INTEGER,
#         CONSTRAINT subscriber_c UNIQUE (sid,eid))
#         """)
# ev1 = 'something'


conn.commit()
conn.close()
############################################################################
# queries

# c.execute("UPDATE eventBroker set eventData = ? WHERE eid = ?", (ev1,1))
# c.execute("SELECT * from eventBroker")
# print(c.fetchall())

# evid = 1
# ev1 = 'something'
# ev2 = 'something else'
# ev3 = 'nothing here'
#
# # for publisher to publish
# c.execute("UPDATE topics set event_data = ? WHERE eid = ?", (ev1, 1))
# c.execute("UPDATE topics set event_data = ? WHERE eid = ?",(ev2,2))
# c.execute("UPDATE topics set event_data = ? WHERE eid = ?",(ev3,3))
#
# # for subscriber to view/notify

# print(c.fetchall())


# pid = 'psaket'
# c.execute("INSERT INTO advertisement VALUES(?,?,?,?)",(pid,0,0,0))
# pid = 'pabhi'
# c.execute("INSERT INTO advertisement VALUES(?,?,?,?)",(pid,0,0,0))
# c.execute("SELECT * FROM advertisement ")
# print(c.fetchall())

#######################################################################

#
# sid = 'ssaket'
# c.execute("INSERT INTO subscription VALUES(?,?,?,?)",(sid,0,0,0))
# sid = 'sabhi'
# c.execute("INSERT INTO subscription VALUES(?,?,?,?)",(sid,0,0,0))
# c.execute("SELECT * FROM subscription ")
# print(c.fetchall())

# c.execute("UPDATE advertisement SET ad1 = 1 WHERE pid ='psaket'")
# c.execute("SELECT * FROM advertisement ")
# print(c.fetchall())
#
# c.execute("UPDATE subscription SET ev2 = 1 WHERE sid ='sabhi'")
# c.execute("SELECT * FROM subscription ")
# print(c.fetchall())
#

