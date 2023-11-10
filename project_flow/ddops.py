
# dbops.py
from sqlalchemy.orm import sessionmaker
from models import User, Project, Task, Base
from sqlalchemy import create_engine




engine = create_engine('sqlite:///project_flow.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def add_user(username):
    session = Session()
    try:
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
        return new_user
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def add_project(project_data):
    session = Session()
    try:
        validated_data = validate_project_input(project_data)
        new_project = Project(**validated_data)
        session.add(new_project)
        session.commit()
        return new_project
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def add_task(task_data):
    session = Session()
    try:
        new_task = Task(**task_data)
        session.add(new_task)
        session.commit()
        return new_task
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

