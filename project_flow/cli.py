import click
from project_flow.models import User, Project, Task
from datetime import datetime

# Utility functions for input validation
def validate_project_input(input_data):
    project_name = input_data.get("project_name")
    start_date = input_data.get("start_date")
    end_date = input_data.get("end_date")

    if not project_name or not start_date or not end_date:
        raise ValueError("Please provide valid values for project_name, start_date, and end_date.")

    return input_data

def get_project_input():
    project_name = click.prompt("Enter project name", type=str)
    start_date_str = click.prompt("Enter start date (YYYY-MM-DD)", type=str)
    end_date_str = click.prompt("Enter end date (YYYY-MM-DD)", type=str)

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

    return {
        "project_name": project_name,
        "start_date": start_date,
        "end_date": end_date,
    }

# CLI commands
@click.group()
def cli():
    pass

@cli.command()
def add_user():
    click.echo("Command to add a new user to the database.")
    username = click.prompt("Enter username", type=str)

    # Database operation (replace with actual SQLAlchemy logic)
    new_user = User(username=username)

    # Print for demonstration purposes
    click.echo(f"Added user: {new_user.username}")

@cli.command()
def add_project():
    click.echo("Command to add a new project to the database.")
    click.echo("Please provide the following information:")
    project_data = get_project_input()
    validated_data = validate_project_input(project_data)

    # Database operation (replace with actual SQLAlchemy logic)
    new_project = Project(**validated_data)

    # Print for demonstration purposes
    click.echo(f"Added project: {new_project.project_name}, Start Date: {new_project.start_date}, End Date: {new_project.end_date}")

@cli.command()
def add_task():
    click.echo("Command to add a new task to the database.")
    task_name = click.prompt("Enter task name", type=str)
    description = click.prompt("Enter task description", type=str)
    deadline_str = click.prompt("Enter task deadline (YYYY-MM-DD)", type=str)

    # Database operation (replace with actual SQLAlchemy logic)
    new_task = Task(task_name=task_name, description=description, deadline=datetime.strptime(deadline_str, "%Y-%m-%d").date())

    # Print for demonstration purposes
    click.echo(f"Added task: {new_task.task_name}, Deadline: {new_task.deadline}")

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from project_flow.models import Base


    engine = create_engine('sqlite:///project_flow.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    cli()  # Run your Click CLI