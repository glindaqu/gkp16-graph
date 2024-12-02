import yaml
import os
from yaml_parser.YamlParserReturnCode import YamlParserReturnCode


class YamlParser:
    def build(self, path: str) -> int:
        if not os.path.isfile(path):
            return YamlParserReturnCode.FILE_DOES_NOT_EXISTS
        if not os.access(path, os.R_OK):
            return YamlParserReturnCode.PERMISSION_DENIED
        with open(path, "r") as file:
            self.contents = yaml.safe_load(file)
        return YamlParserReturnCode.OK

    def get_contents(self):
        return self.contents
