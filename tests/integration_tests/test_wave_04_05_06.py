import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
@pytest.mark.integration_test
def test_integration_wave_04_05_06():
    camila = Vendor()
    valentina = Vendor()

    item_clothing1 = Clothing(condition=1.0)
    item_clothing2 = Clothing(condition=2.0)
    item_electronics1 = Electronics(condition=1.0)
    item_electronics2 = Electronics(condition=2.0)
    item_decor1 = Decor(condition=1.0)
    item_decor2 = Decor(condition=2.0)

    camila.add(item_electronics1)
    camila.add(item_clothing1)
    camila.add(item_clothing2)

    valentina.add(item_electronics2)
    valentina.add(item_decor1)
    valentina.add(item_decor2)
    

    # swap first item
    result = camila.swap_first_item(valentina)
    
    assert result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_clothing2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_decor2 in valentina.inventory

    # swap_best_category - falsy
    result = camila.swap_best_by_category(valentina, "Clothing", "Decor")

    assert not result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_clothing2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_decor2 in valentina.inventory

    # swap_best_category - truthy
    result = camila.swap_best_by_category(valentina, "Decor", "Clothing")

    assert result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_decor2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_clothing2 in valentina.inventory



