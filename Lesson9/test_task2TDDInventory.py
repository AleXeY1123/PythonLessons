import task2TDDInventory as task2

class TestTDDInventory:
    #Тесты нужно запускать по одному
    def test_add_item(self):
        '''Добавить предмет в инвенарь'''
        inv = task2.Inventory(30)
        assert inv.add_item('лопата') == 'Добавлен предмет "лопата"'
        assert inv.inventory_contents == ['лопата']

    def test_add_item_from_list(self):
        '''Добавлять предметы в инвентарь только из заданного диапазона'''
        inv = task2.Inventory(30)
        assert inv.add_item('палка') == 'Добавлен предмет "палка"'
        assert inv.add_item('часы') == 'Ошибка: предмета "часы" не существует'
        assert inv.inventory_contents == ['палка']

    def test_add_item_to_max(self):
        '''Добавлять предметы в интвентарь до максимального веса'''
        inv = task2.Inventory(25)
        assert inv.add_item('палка') == 'Добавлен предмет "палка"'
        assert inv.add_item('тарелка') == 'Добавлен предмет "тарелка"'
        assert inv.add_item('штаны') == 'Добавлен предмет "штаны"'
        assert inv.add_item('лопата') == 'Ошибка: в инвентаре нет места для добавления предмета "лопата"'
        assert inv.inventory_contents == ['палка','тарелка','штаны']

    def test_add_identical_items(self):
        '''Добавлять несколько одинаковых предметов в инвентарь'''
        inv = task2.Inventory(25)
        assert inv.add_item('книга') == 'Добавлен предмет "книга"'
        assert inv.add_item('книга') == 'Добавлен предмет "книга"'
        assert inv.add_item('книга') == 'Добавлен предмет "книга"'
        assert inv.inventory_contents == ['книга','книга','книга']

    def test_del_item(self):
        '''Удалить предмет из инвентаря'''
        inv = task2.Inventory(45)
        assert inv.add_item('палка') == 'Добавлен предмет "палка"'
        assert inv.add_item('тарелка') == 'Добавлен предмет "тарелка"'
        assert inv.add_item('штаны') == 'Добавлен предмет "штаны"'
        assert inv.inventory_contents == ['палка','тарелка','штаны']
        assert inv.del_item('тарелка') == 'Удален предмет "тарелка"'
        assert inv.del_item('куртка') == 'Ошибка: в инвентаре нет предмета "куртка"'
        assert inv.inventory_contents == ['палка','штаны']

    def test_show_inventory(self):
        '''Вывести содержимое инвентаря с количеством предметов и весом'''
        inv = task2.Inventory(45)
        assert inv.add_item('палка') == 'Добавлен предмет "палка"'
        assert inv.add_item('тарелка') == 'Добавлен предмет "тарелка"'
        assert inv.add_item('штаны') == 'Добавлен предмет "штаны"'
        assert inv.add_item('книга') == 'Добавлен предмет "книга"'
        assert inv.add_item('книга') == 'Добавлен предмет "книга"'
        assert inv.show() == [5, 31, ('палка', 10), ('тарелка', 5), ('штаны', 8), ('книга', 4), ('книга', 4)]

