import os
from sqlmodel import SQLModel, Field, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


if os.getenv("DATABASE_URL"):
    engine = create_engine(os.getenv("DATABASE_URL"))
else:
    engine = None


def create_db_and_tables() -> bool:
    """Create a tables in database.

    Returns:
        bool: True if tables created, False if not.
    """
    if engine:
        SQLModel.metadata.create_all(engine)
        return True
    else:
        return False
