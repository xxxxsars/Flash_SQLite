#操作
##install package
```python
pip install Flask,jinja2
```
##create sqlite database
```python
python csv_insert.py
```
##run server
```python
python draw_member.py
```


#說明

##Slite 測試(建立test.db)
1.使用$sqlite3 test.db < create_db.sql，將sql轉為sqlite db
    
    
##用PYTHON 寫入cvs資料(建立實際使用的members.db，使用csv_insert.py)
1.利用csv_insert.py將csv資料寫入   
  +  讀取sql file
  +  建立資料庫
  +  讀取csv後寫入資料庫   
 

##寫抽籤程序(draw_member.py)
1.利用flask.g模組來做sqlite的連線與中斷處理
2.建立首頁資訊，呼叫index.html
3.建立/draw頁面(抽籤頁面)，詳細請看code
4.建立history頁面，透過view的history.html呈現，並繼承base.html的書籤列(/draw一樣處理方式)    



##建立Jinja2模板
  Jinja2模板都要放在templates資料夾下，當Flask利用render_templates呼叫時便可以被讀取    
  css樣板則要放在static之下

1.建立index.html
2.建立base.html，利用繼承方式，讓其他模板繼承常用功能


##參考資料
[用 Flask 與 SQLite 架抽籤網站](https://blog.liang2.tw/posts/2015/09/flask-draw-member/)     
[Jinja2官方文件](http://docs.jinkan.org/docs/flask/tutorial/dbcon.html)

