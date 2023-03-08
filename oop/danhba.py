class Info:
    id=0
    def __init__(self,name=None,number=None):
        self.id=Info.id
        self.name=name
        self.number=number
        Info.id+=1
    def __str__(self):
        return f"""
    ----------------------------
    ID: {self.id}
    Ho va ten: {self.name}      
    So dien thoai: {self.number}
    ----------------------------
    """
    def infoInput(self):
        self.name=input("Vui long nhap ho va ten: ")
        self.number=input("Vui long nhap so dien thoai: ")   
    def infoEdit(self):
        print("1. Sua ho va ten \n2. Sua so dien thoai")
        x=int(input("Ban muon sua thong tin nao: "))
        if x==1:
            self.name=input("Vui long nhap ten moi: ")
        if x==2:
            self.number=input("Vui long nhap so dien thoai moi: ")
class danhBa:
    def __init__(self):
        self.ds=[]
    def addInfo(self,info):
        for it in self.ds:
            if it.name==info.name or it.number==info.number:
                raise ValueError("So dien thoai da ton tai")
        self.ds.append(info)
    def suaDanhBa(self):
        temp=None
        so=None
        index=int(input("Nhap ID cua nguoi ma ban muon sua: "))
        for tt in self.ds:
            if index==tt.id:
                so=index
                break
        if so is None:
            raise ValueError("ID khong ton tai")
                
                
        temp=self.ds[so]
        temp.infoEdit()
        print("Da sua xong!")
    def xoaDanhba(self):
        temp=None
        so=None
        index=int(input("Nhap ID nguoi ma ban muon xoa: "))
        for tt in self.ds:
            if index==tt.id:
                so=index
                break
        if so is None:
        	raise ValueError("ID khong ton tai")
                
        del self.ds[so]
        print("Da xoa thanh cong")   
    def Output(self,fileName):
        f=open(fileName,"w")
        for tt in self.ds:
            f.write(tt.name + '\n')
            f.write(tt.number + '\n')
        f.close()
        print("Da xuat danh ba thanh cong")
    def Input(self,fileName):
        f=open(fileName,"r")
        while True:
            try:
                name=f.readline()[:-1]
                number=f.readline()[:-1]
            except:
                break
        info=Info(name,number)
        self.addInfo(info)
        f.close()
        print(f"Da nhap du lieu tu {fileName} xong")
    def __str__(self):
        lst=''
        for i in self.ds:
            lst+=str(i)
        return lst
a=Info()
a.infoInput()
b=Info()
b.infoInput()
c=Info()
c.infoInput()
danhba=danhBa()
danhba.addInfo(a)
danhba.addInfo(b)
danhba.addInfo(c)