class CustomList:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList([a + b for a, b in zip(self.data, other.data)])
        elif isinstance(other, list):
            return CustomList([a + b for a, b in zip(self.data, other)])
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def get_data(self):
        return self.data

    def __repr__(self):
        return f"CustomList({self.data})"

# Example usage
list1 = CustomList([1, 2, 3])
list2 = CustomList([4, 5, 6])

print(list1)

# Add CustomList objects
result = list1 + list2
print(result)  # CustomList([5, 7, 9])

# Add the internal lists
result2 = list1.get_data() + list2.get_data()
print(result2)  # [1, 2, 3, 4, 5, 6]

print(2*[1,2,3])
