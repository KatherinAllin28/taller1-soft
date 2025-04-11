from abc import ABC, abstractmethod

class IAuthService(ABC):
    @abstractmethod
    def authenticate(self, request, username: str, password: str):
        pass
