from pydantic import BaseModel
from typing import Optional

class ApplicationInput(BaseModel):

    SK_ID_CURR: int
    NAME_CONTRACT_TYPE: Optional[str] = None
    CODE_GENDER: Optional[str] = None
    FLAG_OWN_CAR: Optional[str] = None
    FLAG_OWN_REALTY: Optional[str] = None
    CNT_CHILDREN: Optional[int] = None
    AMT_INCOME_TOTAL: Optional[float] = None
    AMT_CREDIT: Optional[float] = None
    AMT_ANNUITY: Optional[float] = None
    AMT_GOODS_PRICE: Optional[float] = None
    NAME_TYPE_SUITE: Optional[str] = None
    NAME_INCOME_TYPE: Optional[str] = None
    NAME_EDUCATION_TYPE: Optional[str] = None
    NAME_FAMILY_STATUS: Optional[str] = None
    NAME_HOUSING_TYPE: Optional[str] = None
    REGION_POPULATION_RELATIVE: Optional[float] = None
    DAYS_BIRTH: Optional[int] = None
    DAYS_EMPLOYED: Optional[int] = None
    DAYS_REGISTRATION: Optional[int] = None
    DAYS_ID_PUBLISH: Optional[int] = None
    OWN_CAR_AGE: Optional[float] = None
    FLAG_MOBIL: Optional[int] = None
    FLAG_EMP_PHONE: Optional[int] = None
    FLAG_WORK_PHONE: Optional[int] = None
    FLAG_CONT_MOBILE: Optional[int] = None
    FLAG_PHONE: Optional[int] = None
    FLAG_EMAIL: Optional[int] = None
    OCCUPATION_TYPE: Optional[str] = None
    CNT_FAM_MEMBERS: Optional[float] = None
    REGION_RATING_CLIENT: Optional[int] = None
    REGION_RATING_CLIENT_W_CITY: Optional[int] = None
    WEEKDAY_APPR_PROCESS_START: Optional[str] = None
    HOUR_APPR_PROCESS_START: Optional[int] = None
    REG_REGION_NOT_LIVE_REGION: Optional[int] = None
    REG_REGION_NOT_WORK_REGION: Optional[int] = None
    LIVE_REGION_NOT_WORK_REGION: Optional[int] = None
    REG_CITY_NOT_LIVE_CITY: Optional[int] = None
    REG_CITY_NOT_WORK_CITY: Optional[int] = None
    LIVE_CITY_NOT_WORK_CITY: Optional[int] = None
    ORGANIZATION_TYPE: Optional[str] = None
    EXT_SOURCE_1: Optional[float] = None
    EXT_SOURCE_2: Optional[float] = None
    EXT_SOURCE_3: Optional[float] = None
    APARTMENTS_AVG: Optional[float] = None
    BASEMENTAREA_AVG: Optional[float] = None
    YEARS_BEGINEXPLUATATION_AVG: Optional[float] = None
    YEARS_BUILD_AVG: Optional[float] = None
    COMMONAREA_AVG: Optional[float] = None
    ELEVATORS_AVG: Optional[float] = None
    ENTRANCES_AVG: Optional[float] = None
    FLOORSMAX_AVG: Optional[float] = None
    FLOORSMIN_AVG: Optional[float] = None
    LANDAREA_AVG: Optional[float] = None
    LIVINGAPARTMENTS_AVG: Optional[float] = None
    LIVINGAREA_AVG: Optional[float] = None
    NONLIVINGAPARTMENTS_AVG: Optional[float] = None
    NONLIVINGAREA_AVG: Optional[float] = None
    FONDKAPREMONT_MODE: Optional[str] = None
    HOUSETYPE_MODE: Optional[str] = None
    TOTALAREA_MODE: Optional[float] = None
    WALLSMATERIAL_MODE: Optional[str] = None
    EMERGENCYSTATE_MODE: Optional[str] = None

    # ---- Bureau aggregates ----
    BUREAU_LOAN_COUNT: Optional[int] = None
    BUREAU_ACTIVE_COUNT: Optional[int] = None
    BUREAU_CLOSED_COUNT: Optional[int] = None
    BUREAU_DEBT_SUM: Optional[float] = None
    BUREAU_CREDIT_SUM: Optional[float] = None
    BUREAU_CREDIT_MEAN: Optional[float] = None
    BUREAU_DPD_MAX: Optional[float] = None
    BUREAU_DPD30_SUM: Optional[float] = None

    # ---- Previous application aggregates ----
    NUM_PREV_APPS: Optional[int] = None
    NUM_APPROVED: Optional[int] = None
    NUM_REFUSED: Optional[int] = None
    MEAN_PREV_AMT_CREDIT: Optional[float] = None
    MIN_DAYS_DECISION: Optional[float] = None
    MAX_DAYS_DECISION: Optional[float] = None
    APPROVAL_RATE: Optional[float] = None
    REFUSAL_RATE: Optional[float] = None

    # ---- POS aggregates ----
    POS_NUM_PREV: Optional[int] = None
    POS_MEAN_NUM_MONTHS: Optional[float] = None
    POS_MAX_NUM_MONTHS: Optional[float] = None
    POS_MEAN_COMPLETED_RATE: Optional[float] = None

    # ---- Installment aggregates ----
    INST_NUM_PREV: Optional[int] = None
    INST_MEAN_NUM_PAYMENTS: Optional[float] = None
    INST_MEAN_LATE_RATE: Optional[float] = None
    INST_MEAN_PAYMENT_PERC: Optional[float] = None
    INST_MAX_DAYS_LATE: Optional[float] = None

    # ---- Credit card aggregates ----
    CC_NUM_PREV: Optional[int] = None
    CC_MEAN_NUM_MONTHS: Optional[float] = None
    CC_MEAN_BALANCE: Optional[float] = None
    CC_MEAN_LIMIT: Optional[float] = None
    CC_MEAN_UTILIZATION: Optional[float] = None
    CC_MAX_UTILIZATION: Optional[float] = None
