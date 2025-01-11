"""
模块文档 
"""
def greet(name):
    print(f"Hello, {name}!")
## 来写函数文档 模块文档 类文档
def add(a, b) -> float:
    """ 函数简短说明

    函数描述：加法运算

    Args:
        a (int): 第一个加数
        b (int): 第二个加数

    Raises:
        TypeError: 如果a或b不是数字类型
        

    Returns:
        C (float): 加法结果

    """
    """使用Python 谷歌文档规范:加饭 
    - 模块名 : src.test
    - 函数名 : add
    - 函数参数 : a , b
    - 函数描述: 加法运算
    
      """
    print("123")
    return a+b