import csv
from io import StringIO
from fastapi import FastAPI, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar

from db.models import History
from db.session import get_session

from calculator import evaluate_rpn

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/result")
async def create_result(
    *,
    session: AsyncSession = Depends(get_session),
    operation: list[str],
):
    result = evaluate_rpn(operation)
    history = History(operation=operation, result=result)
    session.add(history)
    await session.commit()
    await session.refresh(history)
    return history


@app.get("/history")
async def get_csv_history(
    *,
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
    response: Response,
):
    query_result = await session.exec(select(History).offset(skip).limit(limit))
    history = query_result.all()

    csv_data = StringIO()
    writer = csv.writer(csv_data, delimiter='#')
    writer.writerow(["id", "operation", "result"])

    for row in history:
        writer.writerow([row.id, row.operation, row.result])

    response.headers["Content-Disposition"] = "attachment; filename=history.csv"
    response.headers["Content-Type"] = "text/csv"

    return csv_data.getvalue()
