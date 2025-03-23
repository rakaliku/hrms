from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from ..core.config import settings

# Database Configuration
username = "root"
password = "Mysql%400195"
DATABASE_URL = "mysql+pymysql://{0}:{1}@127.0.0.1:3306/hrms_db".format(username, password)
# print(settings.DB_PASSWORD)
# DATABASE_URL = (
#     f"mysql+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}"
#     f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
# )

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  # Providing DB session
    except Exception as e:
        print(f"Database error: {e}")  # Log the error
        raise e  # ✅ Re-raise the exception
    finally:
        db.close()


def create_tables():
    """Function to create database tables"""
    from ..models import department, employee, leave, roles, salary,attendance,student,class_detail, student_attendance  # Import all models
    print("Registered tables are: ",Base.metadata.tables.keys())  # This will show all tables mapped to Base
    inspector = inspect(engine)

    registered_tables =set(Base.metadata.tables.keys())
    existing_tables = set(inspector.get_table_names())
    need_to_be_create_table = registered_tables - existing_tables

    if need_to_be_create_table:

        new_tables = [Base.metadata.tables[table] for table in need_to_be_create_table]

        Base.metadata.create_all(engine,tables= new_tables)
        print("Database tables created successfully")
    else:
        print("Database tables already exist")


