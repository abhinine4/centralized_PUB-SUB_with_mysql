import sqlite3

class SubService:

    def subscribe(sid,eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM publisher WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 1 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 1, 0))
        conn.commit()
        conn.close()
        return

    def unsubscribe(sid,eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM publisher WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 0 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 0, 0))
        conn.commit()
        conn.close()
        return

    def viewNotification(sid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT * FROM subscriber WHERE sid = ? AND notification = 1",(sid,))
        val = c.fetchall()
        if val:
            message = "You new updates !"
        conn.commit()
        conn.close()
        return message

    def view(eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT eventData FROM eventBroker WHERE eid = ?",str(eid))
        updates = c.fetchone()
        conn.commit()
        conn.close()
        return updates

