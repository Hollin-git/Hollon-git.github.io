
# mymodule.py

 
# 写一个类文档 类名 : MyClass
# 类描述: 一个简单的类，用于演示如何编写类文档
# 类参数: value
# 类方法: display_value
# 方法描述: 打印类的值
# 方法参数: 无
# 方法返回值: 无
# 方法示例: MyClass(10).display_value() # 输出: The value is: 10
# 方法示例: MyClass("Hello").display_value() # 输出: The value is: Hello
# 方法示例: MyClass(3.14).display_value() # 输出: The value is: 3.14
# 方法示例: MyClass(True).display_value() # 输出: The value is: True
# 方法示例: MyClass(None).display_value() # 输出: The value is: None
# 方法示例: MyClass([1, 2, 3]).display_value() # 输出: The value is: [1, 2, 3]
# 方法示例: MyClass({"a": 1, "b": 2}).display_value() # 输出: The value is: {'a': 1, 'b': 2}
# 方法示例: MyClass((1, 2, 3)).display_value() # 输出: The value is: (1, 2, 3)
class MyClass:

    """
    写一个类文档 类名 : MyClass  简短描述

    类描述: 一个简单的类，用于演示如何编写类文档 更多说明
    
    attributes:
      name (String): The value of the class
      age (int): The age of the class

    Example:

        >>> display_value(10)
        10
        
        >>> add(5)
        15

    """
    """    
      - MyClass(10).display_value() # 输出: The value is: 10
      - MyClass("Hello").display_value() # 输出: The value is: Hello

    类参数: value
    
    类方法: display_value
    方法描述: 打印类的值
    方法参数: 无
    方法返回值: 无
    方法示例: MyClass(10).display_value() # 输出: The value is: 10
    方法示例: MyClass("Hello").display_value() # 输出: The value is: Hello
    方法示例: MyClass(3.14).display_value() # 输出: The value is: 3.14
    方法示例: MyClass(True).display_value() # 输出: The value is: True
    方法示例: MyClass(None).display_value() # 输出: The value is: None
    方法示例: MyClass([1, 2, 3]).display_value() # 输出: The value is: [1, 2, 3]
    方法示例: MyClass({"a": 1, "b": 2}).display_value() # 输出: The value is: {'a': 1, 'b': 2}
    方法示例: MyClass((1, 2, 3)).display_value() # 输出: The value is: (1, 2, 3)"""
    def __init__(self, value):
        self.value = value
 
    def display_value(self):
        print(f"The value is: {self.value}")

    def add(self, value):
        print(f"The value is: {self.value}")
        return self.value + value
 
# 可以添加其他函数、类或变量