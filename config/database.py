import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()


#engine object to connect to db
engine = create_async_engine(url= os.getenv('DATABASE_URL'), echo = True)

async_session = sessionmaker(engine, expire_on_commit=False, class_= AsyncSession)

Base = declarative_base()

