from MySQLHandler import MySQLHandler

user = "root"
password = "root"
host = "localhost"
port = 3306
class Item:
    def __init__(self, name:str,  
                manufacturer:str, item_type:str, price:float, amount:int):
        self.item_id = None
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.item_type = item_type
        self.amount = amount

###Getter, Setter###
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        self._name = name
    
    @property
    def item_id(self):
        return self._item_id
    
    @item_id.setter
    def item_id(self, item_id:int):
        self._item_id = item_id

    @property
    def item_type(self):
        return self._item_type
    @item_type.setter
    def item_type(self, item_type:str):
        self._item_type = item_type


    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer:str):
        self._manufacturer = manufacturer

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price:float):
        self._price = price

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount:int):
        self._amount = amount

###Getter, Setter End###

###### Item add and delete #####
Items = []


def fetch_items():
    try:
        mysql_handler = MySQLHandler(host, user, password)
        mysql_handler.connect()
        query = "select * from inventory"
        data = mysql_handler.fetch_data(query)

        for row in data:
            item = Item(
                name=row[1],
                manufacturer=str(row[2]),
                item_type=str(row[3]),
                price=row[4],
                amount=row[5],
            )
            item.item_id = int(row[0])
            Items.append(item)
        mysql_handler.disconnect()
        print(f"Er")
    except Exception as err:
        print(f"Error Fetching: {err}")


def add_item(name: str, manufacturer: str, item_type: str, price: float, amount: int):
    try:
        new_item = Item(mng_id, name, manufacturer, item_type, price, amount)
        Items.append(new_item)
        query = "insert into item (name, manufacturer, item_type,price,amount)"
        values = (name, manufacturer, item_type, price, amount)
        mysql_handler = MySQLHandler()
        mysql_handler.connect()
        mysql_handler.execute_query(query, values)
        return "Entry success"
    except Exception as err:
        return "Entry failed"


def remove_item(id: int):
    try:
        for item in Items:
            if id == item.id:
                mysql.connect()
                run_query(f"Delete from item where id= {item.id}")
                Items.remove(item)
                mysql.close()
                return "Delete success!"
    except Exception as err:
        print(f"Error: {err}")

###### Item add and delete end #####