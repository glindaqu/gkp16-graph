from enum import Enum


class GraphBuilderReturnCode(Enum):
    OK = 0
    PERMISSION_DENIED = -1
    FILE_DOES_NOT_EXISTS = -2
    OUTPUT_FILE_PATH_EMPTY = -3