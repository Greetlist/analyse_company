from sqlalchemy import Column, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml
engine = None
session = None
mysql_configs = None

def load_configs():
    global mysql_configs
    f = open('config/config.yaml', 'r')
    mysql_configs = yaml.safe_load(f)['mysql']

def set_up_session():
    global engine, session, mysql_configs
    engine = create_engine('mysql://{user}:{passwd}@{host}/{database}'.format(**mysql_configs), encoding='utf-8')
    Session = sessionmaker(bind=engine)
    session = Session()

load_configs()
set_up_session()
Base = declarative_base()
Base.metadata.bind = engine


class business_activity_cash_income(Base):
    __tablename__ = 'business_activity_cash_income'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class business_activity_cash_outcome(Base):
    __tablename__ = 'business_activity_cash_outcome'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class business_activity_cash_total(Base):
    __tablename__ = 'business_activity_cash_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class investment_activity_cash_income(Base):
    __tablename__ = 'investment_activity_cash_income'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class investment_activity_cash_outcome(Base):
    __tablename__ = 'investment_activity_cash_outcome'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class investment_activity_cash_total(Base):
    __tablename__ = 'investment_activity_cash_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class fundraising_activity_cash_income(Base):
    __tablename__ = 'fundraising_activity_cash_income'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class fundraising_activity_cash_outcome(Base):
    __tablename__ = 'fundraising_activity_cash_outcome'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class fundraising_activity_cash_total(Base):
    __tablename__ = 'fundraising_activity_cash_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class bill_checkin(Base):
    __tablename__ = 'bill_checkin'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class funds_checkin(Base):
    __tablename__ = 'funds_checkin'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class inventory(Base):
    __tablename__ = 'inventory'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class fixed_asserts(Base):
    __tablename__ = 'fixed_asserts'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class flowable_asserts_total(Base):
    __tablename__ = 'flowable_asserts_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class non_flowable_asserts_total(Base):
    __tablename__ = 'non_flowable_asserts_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class asserts_total(Base):
    __tablename__ = 'asserts_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class bill_checkout(Base):
    __tablename__ = 'bill_checkout'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class funds_checkout(Base):
    __tablename__ = 'funds_checkout'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class flowable_debt_total(Base):
    __tablename__ = 'flowable_debt_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class non_flowable_debt_total(Base):
    __tablename__ = 'non_flowable_debt_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class total_debt(Base):
    __tablename__ = 'total_debt'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class trading_income_total(Base):
    __tablename__ = 'trading_income_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class trading_cost_total(Base):
    __tablename__ = 'trading_cost_total'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class trading_profit(Base):
    __tablename__ = 'trading_profit'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class trading_outside_income(Base):
    __tablename__ = 'trading_outside_income'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class trading_outside_cost(Base):
    __tablename__ = 'trading_outside_cost'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class total_profit(Base):
    __tablename__ = 'total_profit'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)

class pure_profit(Base):
    __tablename__ = 'pure_profit'

    id = Column(BigInteger, primary_key=True)
    inst_code = Column(String(64))
    date = Column(String(64))
    value = Column(BigInteger)


Base.metadata.create_all(engine)