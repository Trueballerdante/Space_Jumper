import sqlite3

db_name = "Controller/database/top_time.db"

def get_all():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM top_times ORDER BY time")
    records = c.fetchall()

    conn.close()

    return records

def get_times():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELECT time FROM top_times ORDER BY time")
    times = c.fetchall()

    conn.close()

    return times

def get_slowest_time():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELECT time FROM top_times ORDER BY time DESC")
    time = c.fetchone()

    conn.close()

    return time[0]

def get_fastest_time():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELECT time FROM top_times ORDER BY time")
    time = c.fetchone()[0]

    conn.close()

    return time

def get_num_of_records():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM top_times")
    num_records = c.fetchone()[0]

    conn.close()

    return num_records

def add_new_time(player_name, player_time):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    num_records = get_num_of_records()
    print()

    if num_records == 0:
        c.execute("INSERT INTO top_times VALUES (?, ?)", (player_name, player_time))
    else:
        slowest_time = get_slowest_time()
        if player_time < slowest_time:
            records = get_all()
            for record in records:
                if player_time < record[2]:
                    prev_row = record
                    c.execute("""UPDATE top_times SET name = (?), time = (?) 
                            WHERE rowid = (?)""", (player_name, player_time, record[0]))
                    player_name = prev_row[1]
                    player_time = prev_row[2]
            if prev_row[0] < 5:
                c.execute("INSERT INTO top_times VALUES (?, ?)", (player_name, player_time))
        elif num_records < 5:
            c.execute("INSERT INTO top_times VALUES (?, ?)", (player_name, player_time))

    if num_records == 6:
        c.execute("DELETE FROM top_times WHERE rowid = 6")

    conn.commit()
    conn.close()

def get_placement(time):
    placement = 1
    p = ""
    for t in get_times():
        if time < t[0]:
            break
        placement += 1

    if placement == 1:
        p = "1st"
    elif placement == 2:
        p = "2nd"
    elif placement == 3:
        p = "3rd"
    elif placement == 4:
        p = "4th"
    else:
        p = "5th"

    return p


#run tests
#print(get_all())