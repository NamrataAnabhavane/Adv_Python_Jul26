from abc import ABCMeta
from registry.registry import ProductRegistry

class ProductMeta(ABCMeta):

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)

        if name != "BaseProduct":
            ProductRegistry.register(cls)

        return cls