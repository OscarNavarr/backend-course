from abc import ABC, abstractmethod



class Repository(ABC):
    @abstractmethod
    def get_planning(self, id: int):
        raise NotImplementedError


class RepositoryPostgres(Repository):
    def get_planning(self, id: int):
        return f"Postgres: {id}"


def main(repository: Repository):
    print(repository.get_planning(1))


if __name__ == "__main__":  # Condition correcte
    try:
        main(RepositoryPostgres())
    exœcept:
        print("error")