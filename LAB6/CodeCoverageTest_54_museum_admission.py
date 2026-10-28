
import pytest

from museum_admission import (
    ticket_price,
    group_discount,
    gallery_entry,
)


# Ticket pricing tests
def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 30, "tuesday", False)


def test_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


@pytest.mark.parametrize("age", [0, 4])
def test_free_ticket_for_children_under_five(age):
    assert ticket_price("adult", age, "tuesday", False) == 0


def test_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150


@pytest.mark.parametrize("day", ["saturday", "sunday"])
def test_weekend_surcharge(day):
    assert ticket_price("adult", 30, day, False) == 350


def test_guided_tour_for_student():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_guided_tour_for_non_student():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_monday_with_guided_tour():
    assert ticket_price("adult", 30, "monday", True) == 250


# Group discount tests
def test_invalid_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_school_group_below_twenty():
    assert group_discount(19, True) == 25


def test_school_group_of_twenty():
    assert group_discount(20, True) == 40


def test_non_school_group_below_eight():
    assert group_discount(4, False) == 0


def test_non_school_group_of_eight():
    assert group_discount(8, False) == 10


def test_non_school_group_of_fourteen():
    assert group_discount(14, False) == 10


def test_non_school_group_of_fifteen():
    assert group_discount(15, False) == 20


# Gallery entry tests
def test_gallery_at_capacity():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_above_capacity():
    assert gallery_entry(101, 100, True) == "wait"


def test_gallery_near_capacity_without_timed_slot():
    assert gallery_entry(90, 100, False) == "queue"


def test_gallery_near_capacity_with_timed_slot():
    assert gallery_entry(90, 100, True) == "enter"


def test_gallery_below_ninety_percent_capacity():
    assert gallery_entry(80, 100, False) == "enter"
