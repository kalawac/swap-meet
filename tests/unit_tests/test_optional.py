import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_item_age_returns_correct_age():
    
    item_a = Item(age=6)
    item_b = Clothing(age=10)
    item_c = Decor(age=12)
    item_d = Electronics(age=8)

    assert item_a.age == 6
    assert item_b.age == 10
    assert item_c.age == 12
    assert item_d.age == 8


def test_swap_by_newest_returns_truthy():
    # me
    item_a = Decor(age=6)
    item_b = Electronics(age=10)
    item_c = Decor(age=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result
    assert len(tai.inventory) == len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_by_newest_with_duplicates():
    # me
    item_a = Electronics(age=10)
    item_b = Decor(age=6)
    item_c = Decor(age=6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=9)
    item_e = Decor(age=2)
    item_f = Clothing(age=4)
    item_g = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f, item_g]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 4
    assert item_a in tai.inventory
    assert item_b not in tai.inventory
    assert item_c in tai.inventory
    assert item_f in tai.inventory
    assert item_b in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f not in jesse.inventory
    assert item_g in jesse.inventory

def test_swap_by_newest_no_inventory_returns_falsy():
    # me
    tai = Vendor()

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_by_newest_no_other_inventory_returns_falsy():
    # me
    item_a = Decor(age=6)
    item_b = Electronics(age=10)
    item_c = Decor(age=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor()

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory


def test_swap_by_newest_no_categories():
    # me
    item_a = Electronics(age=10)
    item_b = Decor(age=8)
    item_c = Decor(age=6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=9)
    item_e = Decor(age=2)
    item_f = Clothing(age=3)
    item_g = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f, item_g]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 4
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c not in tai.inventory
    assert item_e in tai.inventory
    assert item_c in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e not in jesse.inventory
    assert item_f in jesse.inventory
    assert item_g in jesse.inventory

def test_swap_by_newest_one_vendor_category():
    # me
    item_a = Electronics(age=10)
    item_b = Decor(age=8)
    item_c = Decor(age=6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=9)
    item_e = Decor(age=2)
    item_f = Clothing(age=3)
    item_g = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f, item_g]
    )

    # Act
    result = tai.swap_by_newest(other=jesse, my_priority="Clothing")

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 4
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c not in tai.inventory
    assert item_f in tai.inventory
    assert item_c in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f not in jesse.inventory
    assert item_g in jesse.inventory