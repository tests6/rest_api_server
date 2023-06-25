from sqlmodel import SQLModel, Field, Column, String
from sqlalchemy.dialects import postgresql


class History(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    operation: list[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    result: float
