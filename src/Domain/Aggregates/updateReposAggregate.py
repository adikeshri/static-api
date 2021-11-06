from Domain.Entities.GetReposItem import GetReposItem
from Infrastructure.Models.getReposResponse import GetReposResponse
class UpdateReposAggregate:
    def __init__(self, data: GetReposResponse) -> None:
        self.reposItemObject = self.__GetDomainObject(data)

    def __GetDomainObject(self,  data: GetReposResponse) -> GetReposItem:
        totalStars = 0
        for d in data:
            totalStars += d.stargazers_count

        domainObject: GetReposItem = GetReposItem(len(data), totalStars)

        return domainObject
