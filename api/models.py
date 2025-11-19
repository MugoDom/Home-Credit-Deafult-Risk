# api/models.py
from pydantic import BaseModel
from typing import Optional

class ApplicationInput(BaseModel):
    """
    Input fields MUST match the raw columns expected by Notebook 05
    before preprocessing. These are the exact columns in train_merged.csv.
    """
    # At minimum include SK_ID_CURR and every raw feature in train_merged.
    # Example subset:
    SK_ID_CURR: int
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    AMT_GOODS_PRICE: Optional[float] = None
    CNT_CHILDREN: int
    CNT_FAM_MEMBERS: int
    DAYS_BIRTH: int
    DAYS_EMPLOYED: int
    DAYS_REGISTRATION: int
    DAYS_ID_PUBLISH: int

    # Add ALL remaining columns from train_merged.csv
