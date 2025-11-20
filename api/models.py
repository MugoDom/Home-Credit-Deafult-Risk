from pydantic import BaseModel
from typing import Optional

class ApplicationInput(BaseModel):
    SK_ID_CURR: int
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: Optional[float] = None
    AMT_GOODS_PRICE: Optional[float] = None
    CNT_CHILDREN: int
    CNT_FAM_MEMBERS: int
    DAYS_BIRTH: int
    DAYS_EMPLOYED: int
    DAYS_REGISTRATION: int
    DAYS_ID_PUBLISH: int

    NAME_CONTRACT_TYPE: str
    CODE_GENDER: str
    NAME_INCOME_TYPE: str
    NAME_EDUCATION_TYPE: str
    NAME_FAMILY_STATUS: str
    NAME_HOUSING_TYPE: str

    class Config:
        extra = "allow"