from distutils.core import setup

setup(
    name="my_package",  # 模块名称
    version="1.0",  # 版本号
    description="这是一个对外发布的模块，测试",  # 描述
    author="wenw",  # 作者
    author_email="",  # 作者邮箱
    py_modules=["my_package.demo1", "my_package.demo2"]  # 要发布的模块
)
