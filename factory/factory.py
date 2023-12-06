class product:
    def __init__(self, name):
        self.name = name if name else None

    def __str__(self):
        return (f'{self.name}')
    
class monitor(product):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("name"))
        self.diagonal = kwargs.get("diagonal")
        self.resolution = kwargs.get("resolution")
        self.refresh_rate = kwargs.get("refresh_rate")

    def __str__(self):
        return f'          Name: {self.name}\n      Diagonal: {self.diagonal}\n    Resolution: {self.resolution}\n  Refresh rate: {self.refresh_rate}\n'
            
class pc(product):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("name"))
        self.cpu = kwargs.get("cpu")
        self.ram = kwargs.get("ram")
        self.gpu = kwargs.get("gpu")

    def __str__(self):
        return f'          Name: {self.name}\n           CPU: {self.cpu}\n           RAM: {self.ram}\n           GPU: {self.gpu}\n'

class mouse(product):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("name"))
        self.type = kwargs.get("type")
        self.ergo_type = kwargs.get("ergo_type")
        self.dpi = kwargs.get("dpi")

    def __str__(self):
        return f'          Name: {self.name}\n          Type: {self.type}\nErgonomic type: {self.ergo_type}\n           DPI: {self.dpi}\n'
    
class keyboard(product):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("name"))
        self.type = kwargs.get("type")
        self.size = kwargs.get("size")
        self.switches = kwargs.get("switches")

    def __str__(self):
        return f'          Name: {self.name}\n          Type: {self.type}\n          Size: {self.size}\n      switches: {self.switches}\n'    
    
class factory:
    iner_products = ["pc", "monitor", "keyboard", "mouse"]

    @staticmethod
    def create(**kwargs):
        if kwargs["product"] in factory.iner_products:
            return globals()[kwargs["product"]](**kwargs)
        else:
            return None

products = []
products.append(factory.create(product = "monitor", name = "MSI", diagonal = "23,5", resolution = "Full HD", refresh_rate = "144Hz"))
products.append(factory.create(product = "pc", name = "ASUS", cpu = "razen 7 3800x", ram = "16Gb", gpu = "AMD 6700 XT Sapphire pulse"))
products.append(factory.create(product = "mouse", name = "Logitech", type = "wireless", ergo_type = "universal", dpi = "25600"))
products.append(factory.create(product = "keyboard", name = "Logitech", type = "wireless", size = "80%", switches = "blue clicki"))

for product in products:
    print(product)