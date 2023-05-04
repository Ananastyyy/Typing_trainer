import pytest

from trainer.window.logic.line_handler import LineHandler

line_handler = LineHandler()
line_handler.set_blocked_text("Hello World")

handle_text = [
    ("", ("", True)),
    ("Hedd", ("Hed", False)),
    ("Hello World", ("Hello World", True))
]


@pytest.mark.parametrize("text, expected", handle_text)
def test_handle_text_with_empty_string(text, expected):
    result = line_handler.handle_text(text)
    expected_result = expected
    assert result, expected_result
