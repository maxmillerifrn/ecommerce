from models.models import Papel
from abc import ABC, abstractmethod


class PapelService(ABC):

    @abstractmethod
    def create_papel(self, papel: Papel):
        pass

    @abstractmethod
    def list_papel(self)->list[Papel]:
        pass



