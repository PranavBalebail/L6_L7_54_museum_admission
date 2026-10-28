
import pytest

from museum_admission import (
    ticket_price,
    group_discount,
    gallery_entry,
)


# ticket_price: category validation
def test_category_valid_and_invalid():
    assert ticket_price("adult", 30, "tuesday", False) == 300

    with pytest.raises(ValueError):
        ticket_price("unknown", 30, "tuesday", False)


# ticket_price: age validation and free admission
def test_age_branches():
    with pytest.raises(ValueError):
        ticket_price("adult", -1, "tuesday", False)

    assert ticket_price("adult", 4, "tuesday", False) == 0
    assert ticket_price("adult", 5, "tuesday", False) == 300


# ticket_price: Monday, weekend and ordinary days
def test_day_branches():
    assert ticket_price("adult", 30, "monday", False) == 150
    assert ticket_price("adult", 30, "saturday", False) == 350
    assert ticket_price("adult", 30, "sunday", False) == 350
    assert ticket_price("adult", 30, "tuesday", False) == 300


# ticket_price: guided tour decision and nested category decision
def test_guided_tour_branches():
    assert ticket_price("student", 20, "tuesday", True) == 200
    assert ticket_price("adult", 20, "tuesday", True) == 400
    assert ticket_price("student", 20, "tuesday", False) == 150


# group_discount: invalid size and school group branches
def test_school_group_branches():
    with pytest.raises(ValueError):
        group_discount(0, True)

    assert group_discount(19, True) == 25
    assert group_discount(20, True) == 40


# group_discount: non-school group thresholds
def test_non_school_group_branches():
    assert group_discount(15, False) == 20
    assert group_discount(8, False) == 10
    assert group_discount(7, False) == 0


# gallery_entry: full, overfull, and below capacity
def test_gallery_capacity_branches():
    assert gallery_entry(100, 100, False) == "wait"
    assert gallery_entry(101, 100, True) == "wait"
    assert gallery_entry(80, 100, False) == "enter"


# gallery_entry: both outcomes of the near-capacity condition
def test_gallery_ninety_percent_and_timed_slot_branches():
    assert gallery_entry(90, 100, False) == "queue"
    assert gallery_entry(90, 100, True) == "enter"


# gallery_entry: near-capacity comparison is false
def test_gallery_below_threshold():
    assert gallery_entry(89, 100, False) == "enter"
