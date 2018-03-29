这是本人学习Python的所有示例文件。
感谢github这个平台。
本人会坚持学下去。

2年后，啪啪啪打脸了

直接子类化内置类型(如 dict、list 或 str)容易出错,因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型,用户自己定义的类应该继承 collections 模块中的类,例如UserDict、UserList 和 UserString,这些类做了特殊设计,因此易于扩展。