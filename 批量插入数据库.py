"""100w行数据插入mysql数据库"""

import pandas as pd

title="UserID::MovieID::Rating::Timestamp"
df_movie=pd.read_csv("movielens-lm/ratings.dat",
    names=title.split("::"),
    headers=None,
    sep="::",
    engine='python')
print(df_movie.head(),df_movie.shape())

import pymysql
conn=pymysql.Connect(
    host='127.0.0.1',
    user='root',
    password='',
    port=3306,
    db='antpython',
    charset='utf8'
    )


# 批量存入数据库
count=0
total=len(df_moive)
for idx,row in df_movie.iterows():
    count+=1
    UserID,MovieID,Rating,Timestamp=(
        row["UserID"],
        row["MovieID"],
        row["Rating"],
        row["Timestamp"],
    )
    if count%1000==0:
        print(f"进度{count}/{total}={count*100/total}%")
    sql=f"""
        insert into movie_rating
        (user_id,movie_id,rating,timestamp)
        values({UserID},{MovieID},{Rating},{Timestamp})"""
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit
    
# 查询结果行数
df1=pd.read_sql("""
    select count(1) from movie_rating""",con=conn)

df2=pd.read_sql("""
    select * from movie_rating limit 10""",con=conn)
