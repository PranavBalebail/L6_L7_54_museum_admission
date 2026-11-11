from hypothesis import given, strategies as st
from museum_admission_parser import (
    format_visitor_name,
    parse_group_ages,
    parse_visit_date,
)


@given(st.text() | st.none())
def test_format_visitor_name_no_crash(s):
    try:
        format_visitor_name(s)
    except Exception as exc:
        assert False, f"format_visitor_name crashed with {s!r}: {exc}"


@given(st.text() | st.none())
def test_parse_group_ages_no_crash(s):
    try:
        parse_group_ages(s)
    except Exception as exc:
        assert False, f"parse_group_ages crashed with {s!r}: {exc}"


@given(st.text() | st.none())
def test_parse_visit_date_no_crash(s):
    try:
        parse_visit_date(s)
    except Exception as exc:
        assert False, f"parse_visit_date crashed with {s!r}: {exc}"


# Additional properties documenting the invalid-input behaviour.
@given(st.text())
def test_format_visitor_name_returns_string(s):
    assert isinstance(format_visitor_name(s), str)


@given(st.text())
def test_parse_group_ages_returns_list_of_integers(s):
    result = parse_group_ages(s)
    assert isinstance(result, list)
    assert all(isinstance(age, int) for age in result)


@given(st.text())
def test_parse_visit_date_returns_tuple_or_none(s):
    result = parse_visit_date(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 3
        and all(isinstance(part, int) for part in result)
    )