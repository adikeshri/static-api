from abc import ABC, abstractmethod


class IGithubFiles(ABC):
    @abstractmethod
    async def getGithubReposData(self):
        pass

    @abstractmethod
    async def getGithubContributorsData(self):
        pass

    @abstractmethod
    async def injectIntoReposDB(self, data):
        pass

    @abstractmethod
    async def injectIntoContributorsDB(self, data):
        pass