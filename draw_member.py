from flask import Flask,g,render_template,request
import csv
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)
SQLITE_DB_PATH = 'members.db'
SQLITE_DB_SCHEMA = "create_db.sql"
MEMBER_CSV_PATH ="members.csv"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/draw',methods=["POST"])
def draw():
    db = get_db()
    #取得表單中group_name的值，預設是ALL
    group_name = request.form.get("group_name",'ALL')
    valid_members_sql = 'SELECT id FROM members '

    #選擇All就是選擇全部團體，列出全部團體下的memebers
    if group_name =="ALL":
        cursor = db.execute(valid_members_sql)
   #根據其選擇的團體列出資料
    else:
        valid_members_sql += 'WHERE group_name = ?'
        #很特別的家參數後面要加逗號，不然會顯示沒有這個type?
        cursor = db.execute(valid_members_sql, (group_name, ))
    valid_member_ids = [
        row[0] for row in cursor
    ]
    #如果選擇的團體沒有members，傳出錯誤訊息
    if not valid_member_ids:
        error_msg = "<p>No memebers in group '%s'</p>"%group_name
        return error_msg,404
    #最後傳回一個資料，任意選擇的幸運號碼
    lucky_memeber_id = random.choice(valid_member_ids)

    member_name, member_group_name = db.execute(
        'SELECT name, group_name FROM members WHERE id = ?',
        (lucky_memeber_id,)
    ).fetchone()

    with db:
        db.execute("insert into draw_histories (memberid) values(?)",(lucky_memeber_id,))
    return render_template('draw.html',name = member_name,group = group_name)

@app.route('/history')
def history():
    db = get_db()
    c = db.execute(
        'SELECT m.name, m.group_name, d.time AS "draw_time [timestamp]" '
        'FROM draw_histories AS d, members as m '
        'WHERE m.id == d.memberid '
        'ORDER BY d.time DESC '
        'LIMIT 10'
    ).fetchall()
    recent_histories = []
    for row in c:
        recent_histories.append({
            'name': row[0],
            'group': row[1],
            'draw_time': datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'),
        })
        return render_template('history.html',recent_histories = recent_histories)
def get_db():
    #取得g中的database參數，預設值為None，g是儲存當前環境的通用變數
    db = getattr(g,"_database",None)
    if db is None:
        db = g.__database = sqlite3.connect(SQLITE_DB_PATH)
        db.execute("PRAGMA foreign_keys= ON")
    return  db

#當環境要結束時會啟用這個，把db做close
@app.teardown_appcontext
def close_connection(exception):
    db  = getattr(g,'__database',None)
    if db is not None:
        db.close()



if __name__ =='__main__':
    app.debug = True
    app.run()

