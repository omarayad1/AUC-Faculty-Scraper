from sqlalchemy.orm import sessionmaker
from models import faculty, db_connect, create_faculty_table


class faculty_pipeline(object):
    def __init__(self):
        engine = db_connect()
        create_faculty_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        Faculty = faculty(**item)

        try:
            session.add(Faculty)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
