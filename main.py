'''
need to be refactor:
each group of item need their class. base class of item contains NAME,ID,QUANTITY
ADD(),EDIT(),DELETE(). all other class inharents from base class.
option for milk box container, option for transperent box.

'''
import json
import random
import database as db
def geting_detailes_from_user():
    """ need to be replace with GUI for gether info from user.
    add item button 
    field for entering all user input
    dropdown menu for location
    option for details about item.
     """
    item_name = input("item name:")
    quantity = input("quantity:")
    row_location = input("row location:")
    line_location = input("line location:")
    details = input("details:")
    description = input("description:")
    class_name_str = item(item_name,quantity,row_location,line_location,details,description)
    print(type(class_name_str))
    return class_name_str

class item:
    _item_name:str
    _item_id:int
    _item_quantity:int
    _item_location = {"row":str, "line":str}
    _details:str
    _item_description:str
    
    def GetItem(self):
        itemDict = {"name":self._item_name,"id":self._item_id,"quantity":self._item_quantity,
                    "location_row":self._item_location["row"],"location_line":self._item_location["line"],
                    "details":self._details,"description":self._item_description}
        return itemDict
        
    def __init__(self,item_name,item_quantity,item_row_location,item_line_location,details,item_description):
        self._item_name = item_name
        self._item_id = random.randrange(1,1000,1)
        self._item_quantity = item_quantity
        self._item_location["row"] = item_row_location
        self._item_location["line"] = item_line_location
        self._details = details
        self._item_description = item_description
    
    def AddItem(self):
        print("add item")
        pass

    def DeleteItem(self,item):
        pass

    def EditItem(self,item):
        """ connect to database and geting the relevant object.
        asked the user for what attributes need to be changed.
        update the relevant object
        writing to database the new info
         """
        pass
    def Details(self):
        self.details = "product name is:{}\nproduct uid: {}\nproduct description: {}\nproduct located at: unit {} shelf {}\n".format(self.name,self.id,self.description,self.location["UnitNumber"],self.location["ShelfNumber"])

    def class_to_dict(self):
        str_to_json = {"item_name": {self._item_name},
        "quantity": {self._item_quantity},
        "row_location": {self._item_location["row"]},
        "line_location": {self._item_location["line"]},
        "description": {self._item_description},
        "details": {self._details}}
        return str_to_json
def print_all_items():
    print(db.LoadingJsonFile())
def add_item():
    my_item = geting_detailes_from_user()
    db.start(my_item.GetItem())
def menu():
    print("Home Storage management tool")
    print("1) View all items.")
    print("2) Add item.")
    print("3) Edit item.")
    print("4) Delete item.")
    print("q  for end this program.")

def menu_choices():
    user_choice = input("Select:")
    quit_flag = True
    while quit_flag:
        if user_choice.lower() == "q":
            print("Bye Bye..")
            quit_flag = False
        elif user_choice == "1":
            print_all_items()
            break
        elif user_choice == "2":
            add_item()
            break
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            pass
def main():
    while True:
        menu()
        menu_choices()
if __name__ == "__main__":
    main()