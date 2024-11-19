import hashlib
import uuid


class IDGenerator:

    @classmethod
    def generate_id(cls, *args) -> int:
        if not args:
            return cls.generate_unique_id()
        return int(hashlib.sha256("-".join(args).encode("UTF-8")).hexdigest(), 16)

    @classmethod
    def generate_unique_id(cls) -> int:
        return uuid.uuid4().int >> 65
