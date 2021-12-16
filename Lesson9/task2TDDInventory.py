class Inventory:
    inventory_contents = []
    inventory_current_weight = 0
    allowed_items = {'палка': 10, 
                    'лопата':15, 
                    'ложка': 3, 
                    'тарелка':5, 
                    'книга': 4, 
                    'карандаш':2, 
                    'куртка': 10, 
                    'штаны':8, 
                    'ботинки':6}
        
    allowed_items_list = list(allowed_items.keys())

    def __init__ (self, max_weight):
        self.max_weight = max_weight

    def add_item(self, item):
        if item in self.allowed_items_list:
            if self.max_weight >= self.inventory_current_weight + self.allowed_items.get(item):
                self.inventory_current_weight += self.allowed_items.get(item)
                self.inventory_contents.append(item)
            else:
                return 'Ошибка: в инвентаре нет места для добавления предмета ' + '"' + item + '"'
            return 'Добавлен предмет ' + '"' + item + '"'
        elif item not in self.allowed_items_list:
            return 'Ошибка: предмета ' + '"' + item + '"' + ' не существует'

    def del_item(self, item):
        if item in self.inventory_contents:
            self.inventory_current_weight -= self.allowed_items.get(item)
            self.inventory_contents.remove(item)
            return 'Удален предмет ' + '"' + item + '"'
        else:
            return 'Ошибка: в инвентаре нет предмета ' + '"' + item + '"'

    def show(self):
        out =[]
        out.append(len(self.inventory_contents))
        out.append(self.inventory_current_weight)
        for i in range(len(self.inventory_contents)):
            out.append((self.inventory_contents[i], self.allowed_items.get(self.inventory_contents[i])))
        return out
