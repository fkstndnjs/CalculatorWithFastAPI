from fastapi import APIRouter, Depends, status, HTTPException
from database.connection import get_session
from models.exrpession import Expression
from typing import List

calc_router = APIRouter(tags=["Expression"])

@calc_router.post("/eval", status_code=status.HTTP_201_CREATED)
async def calc(new_calc: Expression, session=Depends(get_session)) -> dict:
    session.add(new_calc)  
    session.commit() 
    session.refresh(new_calc)
    
    try:
        result = eval(new_calc.expr)
    except Exception as e:
        return {"error": str(e)}

    return {"result": result}


@calc_router.post("/mem", status_code=status.HTTP_200_OK)
async def recall_expression(request: dict, session=Depends(get_session)):
    recall = request.get("recall")

    if recall == "all":
        expressions = session.query(Expression).all()
        if not expressions:
            return {"expr": ["No Expressions to Recall"]}
        return {"expr": [expression.expr for expression in expressions]}
    else:
        try:
            recall_id = int(recall)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid recall ID")

        expression = session.get(Expression, recall_id)

        if expression:
            return {"expr": [expression.expr]}
        else:
            raise HTTPException(status_code=404, detail="No Such Expression: " + str(recall_id))
