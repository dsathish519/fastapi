from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='posts', user='postgres', 
#                                 password='dsathish', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("sucessfully connected to database")
#         break
#     except Exception as err:
#         print(f"Connection Failed,Error: {err}")
#         time.sleep(5)


# op.create_table('votes',
#                     sa.Column('user_id', sa.Integer(), nullable=False),
#                     sa.Column('post_id', sa.Integer(), nullable=False),
#                     sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
#                     sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
#                     sa.PrimaryKeyConstraint('user_id', 'post_id')
#     )