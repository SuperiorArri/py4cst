
class IQuietModeController:
    def store_quiet_mode(self) -> None:
        pass

    def restore_quiet_mode(self) -> None:
        pass

    def store_and_disable_quiet_mode(self) -> None:
        pass

    def store_and_enable_quiet_mode(self) -> None:
        pass

    def set_quiet_mode(self, enabled: bool = True) -> None:
        pass

    def is_in_quiet_mode(self) -> bool:
        pass