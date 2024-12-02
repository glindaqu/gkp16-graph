import enum


class GraphBuilderException(enum.Enum):
    FILE_DOES_NOT_EXISTS = Exception(" * Specified file doesn't exists.")
    PERMISSION_DENIED = Exception(" * Can't read file by provided path. Permission denied.")
    