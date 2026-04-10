from sqlmodel import create_engine, Session

DATABASE_url="sqlite:///./app.db"

engine = create_engine(DATABASE_url)

def get_session():
    with Session(engine) as session:
        yield session