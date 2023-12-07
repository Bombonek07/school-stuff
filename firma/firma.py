class business:
    def __init__(self):
        self.branches = []
        self.positions = []

    def new_branch(self, name, adress):
        self.branches.append(branch(name, adress))

    def remove_branch(self, branch_name):
        for branch in self.branches:
            if branch.name == branch_name:
                self.branches.remove(branch)
                branch.delete()
    
    def new_position(self, name):
        self.positions.append(position(name))

    def remove_position(self, position_name):
        for position in self.positions:
            if position.name == position_name:
                self.positions.remove(position)
                position.delete()

    def get_branches(self):
        my_list = []
        for branch in self.branches:
            my_list.append(branch.name)
        return my_list

    def get_positions(self):
        my_list = []
        for position in self.positions:
            my_list.append(position.name)
        return my_list

class branch:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.employees = []

    def new_employee(self, name, position):
        self.employees.append(employee(name, position))
    
    def delete(self):
        del self

class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def remove_employee(self):
        pass

class position:
    def __init__(self, name):
        self.name = name

    def delete(self):
        del self

business = business()

business.new_branch("vojtos", "geto")
print(business.get_branches())

business.new_position("jirkos")
print(business.get_positions())