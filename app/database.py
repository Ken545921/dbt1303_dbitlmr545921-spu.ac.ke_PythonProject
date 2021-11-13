"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

   
    todo_list = [
        {
                "id": 1,
                "task": "task 1",
                "status": "Todo",
        }
        ,
        {
            "id": 2,
                "task": "task 2",
                "status": "Todo",
        }
    ]
    

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    pass


def update_status_entry(task_id: int, text: str) -> None:
    pass

   

def insert_new_task(text: str) ->  int:
    pass

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()
