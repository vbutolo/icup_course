class Car(object):
    vendor = ''
    model = ''
    cubic_size = 0

    def __init__(self, vendor, model, cubic_size):
        self.vendor = vendor
        self.model = model
        self.cubic_size = cubic_size

    def __str__(self):
        string = 'Vendor: %s, Model: %s, Cubic Size: %d' % (self.vendor, self.model, self.cubic_size)
        return  string

    def print(self):
        print(self)

cars = [Car('Renault', 'Clio', 1400), Car('Fiat', 'Punto', 1200), Car('Toyota', 'Yaris', 1300)]  

for car in cars:
    car.print()