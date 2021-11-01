from abc import ABC, abstractmethod


class IGithubService(ABC):
    @abstractmethod
    async def getRepos(self):
        pass

    @abstractmethod
    async def getContributorsOnRepo(self, repoName: str):
        pass