class Item:
#     ID= []
    def __init__(self, id, name, cost):
#         assert id not in Item.ID, "ID da duoc su dung"
        self.id= id
        self.name= name
        self.cost= cost
#         Item.ID.append(id)
    
    def __str__(self):
        return f"""
        ID: {self.id}
        Name: {self.name}
        Cost: {self.cost}
        """
    def enter(self):
        self.id= int(input("ID:")) 
#         assert self.id not in Item.ID, "ID da duoc su dung"
        self.name= input("Name:")
        self.cost= input("Cost:")
#         Item.ID.append(self.id)
    
    def edit(self):
        x= input("Bạn muốn sửa gì?: ")
        new= input(f"Nhập {x} mới: ")
        if x == 'ID':
            self.id= int(new)
        if x == 'Name':
            self.name= new
        if x == 'Cost':
            self.cost= new
class ListItem:
    def __init__(self):
        self.lst= []
    
    def addItem(self, item):
        for it in self.lst:
            if it.id == item.id:
                raise ValueError(f"Đã tồn tại Item với id: {item.id}")
        self.lst.append(item)
    
    def editItem(self, idItem):
        item= None
        for it in self.lst:
            if idItem == it.id:
                item= it
                break
        if item is None:
            raise ValueError("ID Item ko dung")
        item.edit()
        print("Sửa xong!")
        
    def delItem(self, idItem):
        index= None
        for i, it in enumerate(self.lst):
            if idItem == it.id:
                index= i
                break
        if index is None:
            raise ValueError("ID Item ko dung")
        
#         self.lst.remove(item)
        del self.lst[index]
        
    def __str__(self):
        s= ''
        for it in self.lst:
            s += str(it)
        return s
    