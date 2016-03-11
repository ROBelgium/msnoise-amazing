from msnoise.api import *

from .amazing_table_def import AmazingConfig
from .default import default

def main():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    AmazingConfig.__table__.create(bind=engine, checkfirst=True)
    for name in default.keys():
        session.add(AmazingConfig(name=name,value=default[name][-1]))

    session.commit()