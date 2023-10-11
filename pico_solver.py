from abc import ABC, abstractmethod
from tempfile import NamedTemporaryFile
import os

import requests


class PicoSolver(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def solve(self) -> str:
        pass

    @staticmethod
    def download_file(url: str) -> NamedTemporaryFile:
        tf = NamedTemporaryFile("w+")
        tf.write(requests.get(url).text)
        tf.seek(0, os.SEEK_SET)
        return tf
