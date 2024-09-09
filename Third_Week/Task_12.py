class DataTypeComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other):
        return type(self.value1) == type(other.value1) and type(self.value2) == type(other.value2)

    def compare(self):
        if self == DataTypeComparator(self.value1, self.value2):
            return f"The types of {self.value1} and {self.value2} are the same."
        else:
            return f"The types of {self.value1} and {self.value2} are different."

comparator = DataTypeComparator(10, 20)
print(comparator.compare())  # Output: The types of 10 and 20 are the same.

comparator2 = DataTypeComparator(10, "Hello")
print(comparator2.compare())  # Output: The types of 10 and Hello are different.
