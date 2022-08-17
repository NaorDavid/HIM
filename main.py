'''
need to be refactor:
each group of item need their class. base class of item contains NAME,ID,QUANTITY
ADD(),EDIT(),DELETE(). all other class inharents from base class.
option for milk box container, option for transperent box.

'''
import json
import random
import database as db

""" need to be replace with GUI for gether info from user.
    add item button 
    field for entering all user input
    dropdown menu for location
    option for details about item.
     """

class item:
    _item_name:str
    _item_id:int
    _item_quantity:int
    _item_location = {"row":str, "line":str}
    _details:str
    _item_description:str
    
    def input_from_user(self):
        self._item_name = input("item name:")
        self._item_id = random.randrange(1,1000,1)
        self._item_quantity = input("quantity:")
        self._item_location["row"] = input("row location:")
        self._item_location["line"] = input("line location:")
        self._details = input("details:")
        self._item_description = input("description:")
        
    def GetItem(self):
        itemDict = {"name":self._item_name,"id":self._item_id,"quantity":self._item_quantity,
                    "location_row":self._item_location["row"],"location_line":self._item_location["line"],
                    "details":self._details,"description":self._item_description}
        return itemDict
        
    def __init__(self):
        self.input_from_user()
        

    def AddItem(self):
        db.start(self.GetItem())
    
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
            my_item = item()
            my_item.AddItem()
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