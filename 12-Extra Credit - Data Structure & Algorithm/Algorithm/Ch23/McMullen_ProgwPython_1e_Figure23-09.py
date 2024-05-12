class Contact():
    def __init__(self, first_name, last_name, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        
    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        return False
    
    def __lt__(self, other):
        if self.first_name < other.first_name:
            return True
        return False
    
    def __gt__(self, other):
        if self.first_name > other.first_name:
            return True
        return False