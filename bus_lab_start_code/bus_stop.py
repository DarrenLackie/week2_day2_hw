class BusStop:
    def __init__(self, input_name_of_bus_stop):
        self.name = input_name_of_bus_stop
        self.queue = []

    def add_to_queue(self, input_passenger):
        self.queue.append(input_passenger)

    def queue_length(self):
        return len(self.queue)
    
    def clear(self):
        self.queue.clear()
    


    
        
    


    