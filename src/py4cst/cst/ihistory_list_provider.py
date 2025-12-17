from typing import Protocol

class IHistoryListProvider(Protocol):
    def add_to_history(self, header: str, vba_code: str) -> None: ...
