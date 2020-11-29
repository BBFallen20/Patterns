from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """Базовый интерфейс абстрактной фабрики."""
    @abstractmethod
    def create_pc(self) -> AbstractPC:
        pass

    @abstractmethod
    def create_notebook(self) -> AbstractNotebook:
        pass


class AcerFactory(AbstractFactory):
    """Фабрика-производитель"""
    def create_pc(self) -> AbstractPC:
        return AcerPC()

    def create_notebook(self) -> AbstractNotebook:
        return AcerNotebook()


class AbstractPC(ABC):
    """Абстрактный класс ПК"""
    @abstractmethod
    def chars(self) -> str:
        pass


class AbstractNotebook(ABC):
    """Абстрактний класс ноутбуков"""
    @abstractmethod
    def chars(self) -> str:
        pass


class AcerPC(AbstractPC):
    """Класс ПК от конкретного производителя"""
    def chars(self) -> str:
        return "PC made by Acer."


class AcerNotebook(AbstractNotebook):
    """Класс ноутбуков от конкретного производителя"""
    def chars(self) -> str:
        return "Notebook made by Acer."


def main(factory: AbstractFactory) -> None:
    pc_by_factory = factory.create_pc()
    notebook_by_factory = factory.create_notebook()
    print(pc_by_factory.chars())
    print(notebook_by_factory.chars())


if __name__ == '__main__':
    main(AcerFactory())
