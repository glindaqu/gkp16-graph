import enum


class YamlParserReturnCode(enum.Enum):
    OK = 0
    PERMISSION_DENIED = -1
    FILE_DOES_NOT_EXISTS = -2
