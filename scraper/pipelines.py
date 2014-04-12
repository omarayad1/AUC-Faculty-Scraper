from sqlalchemy.orm import sessionmaker
from models import Faculty, db_connect, create_faculty_table


class faculty_pipeline(object):
    def __init__(self):
        engine = db_connect()
        create_faculty_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        faculty = Faculty(**item)
        session.add(faculty)
        session.commit()
        return item
