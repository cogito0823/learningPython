from math import log
class Myarray():

    def __init__(self, capacity=None):
        if not capacity:
            self.capacity = 0
        self.last_index = -1
        self.array = [None] * self.capacity
        
    def __repr__(self):
        string_repr = "["
        str_list = [str(i) for i in self.array[:self.last_index + 1]]
        string_repr += ', '.join(str_list)
        string_repr += "]"
        return string_repr
        
    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= -(self.last_index+1) and index <= self.last_index:
                return self.array[index]
            else:
                raise Exception("数组越界")
        elif isinstance(index, slice):
            start = index.start
            stop = index.stop
            if (stop < 0 and stop % (self.capacity) >= self.last_index + 1) or (stop >= 0 and stop >= self.last_index + 1):
                return self.array[start:self.last_index + 1]
            return self.array[index]
            
    def __setitem__(self, index, value):
        if index >= -(self.last_index+1) and index <= self.last_index:
            self.array[index] = value
        else:
            raise Exception("数组越界")
    
    def __str__(self):
        return self.__repr__()

    def __resize(self):
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity = 2 ** (int(log(self.capacity, 2) // 1 + 1))
        
        new_array = [None] * self.capacity
        for i in range(self.last_index + 1):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def insert(self, index, value):
        if index >= -(self.last_index+1) and index <= self.last_index + 1:
            if self.last_index + 1 >= self.capacity:
                self.__resize()
            for i in range(self.last_index, index - 1, -1):
                self.array[i+1] = self.array[i]
            self.array[index] = value
            self.last_index += 1
        else:
            raise Exception("数组越界")

    def append(self, value):
        if self.last_index >= self.capacity - 1:
            self.__resize()
        self.last_index += 1
        self.array[self.last_index] = value

if __name__ == "__main__":
    array = Myarray()
    array.append(1)
    array.append(2)
    array.append(3)
    array.insert(0,0)
    array.insert(3,3)
    print(array)
