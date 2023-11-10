if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from project_flow.models import Base
    from project_flow.cli import cli

    engine = create_engine('sqlite:///project_flow.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    cli()  # Run your Click CLI
