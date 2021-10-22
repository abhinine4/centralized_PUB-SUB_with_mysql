import sqlite3
from eventService import Events


class PubService:
    def advertise(pid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM publisher WHERE pid = ? AND eid = ?", (pid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE publisher SET advertisement = 1 WHERE pid = ? AND eid = ?", (pid, eid))
        else:
            c.execute("INSERT INTO publisher VALUES(?,?,?)", (pid, eid, 1))
        conn.commit()
        conn.close()
        return

    def deadvertise(pid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM publisher WHERE pid = ? AND eid = ?", (pid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE publisher SET advertisement = 0 WHERE pid = ? AND eid = ?", (pid, eid))
        else:
            c.execute("INSERT INTO publisher VALUES(?,?,?)", (pid, eid, 0))
        conn.commit()
        conn.close()
        return

    def notify(pid,eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM publisher WHERE pid = ? AND eid = ? AND advertisement = 1", (pid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET notification = 1 WHERE eid = ?",str(eid))
        conn.commit()
        conn.close()
        return

    def publish(pid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM publisher WHERE pid = ? AND eid = ?", (pid, eid))
        val = c.fetchone()
        if val:
            Events.eventService(eid)
            PubService.notify(pid,eid)
        conn.commit()
        conn.close()
        return
