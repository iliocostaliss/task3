from datetime import datetime
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
            """
            func_name = func.__name__
            date_time = datetime.now().isoformat(sep=" ", timespec="seconds")
            input_params = f"args: {args}, kwargs: {kwargs}"
            start_msg = f"{date_time} - {func_name} - Started - {input_params}"
            _write_log(start_msg, filename)

            try:
                result = func(*args, **kwargs)
                finish_msg = f"{date_time} - {func_name} - Finished: {result}"
                _write_log(finish_msg, filename)
                return result
            except Exception as e:
                error_msg = f"{date_time} - {func_name} - Error: {type(e).__name__} - {str(e)} - Input: {input_params}"
                _write_log(error_msg, filename)
                raise

        return wrapper

    return decorator


def _write_log(message, filename=None):
    """Функция для записи лога в файл или консоль."""
    if filename:
        with open(filename, "a") as f:
            f.write(message + "\n")
    else:
        print(message)
