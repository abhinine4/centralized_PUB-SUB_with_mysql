import sqlite3

conn = sqlite3.connect('pubsub.db')
c = conn.cursor()

# c.execute("DROP table eventBroker")
# c.execute("DROP table publisher")
# c.execute("DROP table subscriber")
# #
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

# c.execute("select * from subscriber")
# print(c.fetchall())
# c.execute("SELECT * FROM subscriber WHERE sid = 's2' AND eid = '2' AND subscription = 1")
# val = c.fetchone()
# if val is not None:
#     print('None')
conn.commit()
conn.close()