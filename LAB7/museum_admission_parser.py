
from datetime import date


def format_visitor_name(name):
    """
    Formats a full name as 'Surname, Given names'.
    Returns an empty string for invalid or empty input.
    """
    if not isinstance(name, str):
        return ""

    parts = name.split()

    if not parts:
        return ""

    surname = parts[-1].title()
    given_names = " ".join(parts[:-1]).title()

    return surname + ", " + given_names


def parse_group_ages(text):
    """
    Parses space-separated ages into a list of integers.
    Returns an empty list for invalid input.
    """
    if not isinstance(text, str) or not text.strip():
        return []

    try:
        ages = [int(age) for age in text.split()]
    except ValueError:
        return []

    return ages


def parse_visit_date(text):
    """
    Parses a YYYY-MM-DD date into a (year, month, day) tuple.
    Returns None for invalid dates.
    """
    if not isinstance(text, str):
        return None

    try:
        if len(text) != 10:
            return None

        parsed_date = date.fromisoformat(text)

        return (
            parsed_date.year,
            parsed_date.month,
            parsed_date.day
        )

    except ValueError:
        return None


def main():
    print("==== Running format_visitor_name ====")
    value = input("Enter a visitor's full name (e.g. asha rao): ")
    print("Name on ticket:", format_visitor_name(value))

    print("\n==== Running parse_group_ages ====")
    value = input("Enter the ages in the group separated by spaces (e.g. 34 12 70): ")
    print("Group ages:", parse_group_ages(value))

    print("\n==== Running parse_visit_date ====")
    value = input("Enter the visit date as YYYY-MM-DD (e.g. 2026-11-05): ")
    print("Visit date (year, month, day):", parse_visit_date(value))


if __name__ == "__main__":
    main()