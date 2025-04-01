import pytest

from src.decorators import log


@log()
def decorator_func(a, b):
    return a + b


def test_log(capsys):
    result = decorator_func(6, 4)
    assert result == 10
    captured = capsys.readouterr()
    logs = [log.strip() for log in captured.out.strip().split("\n")]
    assert len(logs) == 2
    assert any("Started" in log and "decorator_func" in log and "(6, 4)" in log for log in logs)
    assert any("Finished" in log and "decorator_func" in log and "10" in log for log in logs)


def test_log_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    assert len(output) == 2
    assert "divide  Started with inputs: (6, 0), {}" in output[0]
    assert "divide  Error: ZeroDivisionError" in output[1]


def test_log_metadata():
    @log()
    def example():
        """Example docstring"""
        pass

    assert example.__name__ == "example"
    assert example.__doc__ == "Example docstring"


def test_log_empty_filename(capsys):
    @log()
    def test_func():
        return " "

    test_func()

    captured = capsys.readouterr()
    assert "test_func" in captured.out
