from typing import Union, Dict

class Stack:
    def __init__(self):
        self.__mas = []
        self.dict = {}
        self.indicator = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indicator >= len(self.__mas):
            self.indicator = 0
            raise StopIteration()
        current = self.get_element(self.indicator)
        self.indicator += 1
        return current

    def __len__(self):
        return len(self.__mas)

    def __getitem__(self, item: int):
        return self.get_element(item)

    def pop(self) -> Union[str, int]:
        self.set_dict(self.pop.__name__)
        return self.__mas.pop()


    def push(self, param: Union[str, int]) -> None:
        self.set_dict(self.push.__name__)
        self.__mas.append(param)

    def is_null(self) -> bool:
        self.set_dict(self.is_null.__name__)
        return len(self.__mas) == 0

    def clear(self) -> None:
        self.set_dict(self.clear.__name__)
        self.__mas.clear()


    def set_dict(self, name: Union[str, int]) -> None:
        if name not in self.dict:
            self.dict[name] = 1
        else:
            self.dict[name] += 1

    def get_dict(self) -> Dict[str, int]:
        return self.dict

    def get_element(self, item) -> Union[str, int]:
        return self.__mas[len(self.__mas) - item - 1]

# A = Stack()
# A.clear()
# A.push(1)
# A.push(2)
# A.push(3)
# A.push(4)

# for i in range(len(A)):
#     print(A[i])
#
# print("\n")
# for i in A:
#     print(i)