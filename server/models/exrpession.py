from sqlmodel import SQLModel, Field

class Expression(SQLModel, table=True):
    id: int = Field(primary_key=True)
    expr: str
