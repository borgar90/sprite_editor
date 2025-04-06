# app/interceptor.py
class Interceptor:
    def before_close(self, file_id, file_data) -> bool:
        """
        Called before a file is closed. Return False to cancel the close.
        Override in subclasses.
        """
        return True