class Order :
    def __init__(self,order_id,customer_name,stauts):
        self.order_id = order_id
        self.customer_name = customer_name
        self.stauts = stauts
    def process(self):
        self.stauts = "processed"
    def check_status(self):
        if self.stauts == "processed":
            print(f"Order {self.order_id} for {self.customer_name} has been processed")
        else:
            print(f"Order {self.order_id} for {self.customer_name} is still pending")
        
order1 = Order("36","Nguyen Ba Thien","pending")
order1.process()
order1.check_status()
order2 = Order("37","Nguyen Van Hai","processed")
order2.check_status()