class TaskDuplicationError(Exception):
    """
    Used to indicate that another task with the credentials exists and thus
    name of the task need to be changed to maintain the integrity of the
    system.
    """

    pass
