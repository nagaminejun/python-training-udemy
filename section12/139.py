import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# 1. DBへの接続エンジンを作成 (JavaのDataSourceに相当)
# 'sqlite:///:memory:' は、メモリ上に一時的なDBを作る設定です
engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost/test_mysql_database2', echo=True)

# 2. モデルのベースクラスを作成
Base = sqlalchemy.ext.declarative.declarative_base()

# 3. テーブル定義をクラスで表現 (JavaのEntityクラスに相当)
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

# 4. エンジンを使ってテーブルを実際に作成する
Base.metadata.create_all(engine)

# 5. セッションの作成 (HibernateのSession/EntityManagerに相当)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# 6. データの作成と保存
person1 = Person(name='Mike')
session.add(person1)
person2 = Person(name='Nancy')
session.add(person2)
person3 = Person(name='JJJ')
session.add(person3)
person4 = Person(name='Mike')
session.add(person4)
session.commit() # ここでDBに反映

person5 = session.query(Person).filter_by(name='Mike').first()
person5.name = 'ZZZ'
session.add(person5)
session.commit()

persondel = session.query(Person).filter_by(name='Nancy').first()
persondel.name = 'ZZZ'
session.delete(persondel)
session.commit()

# 7. データの取得 (SQLを書かずにクエリを発行)
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
