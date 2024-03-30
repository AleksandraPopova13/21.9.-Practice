class Customers:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city=city

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'


costomer_1 = Customers('Анна','Петрова','Ижевск',50)
costomer_2 = Customers('Владислав','Донской','Киров',50)
costomer_3 = Customers('Ольга','Иванова','Николаево',50)

guest_list=[costomer_1,costomer_2,costomer_3]


for guest in guest_list:
    print(guest.get_guest())