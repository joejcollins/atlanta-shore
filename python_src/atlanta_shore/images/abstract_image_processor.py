""""""
import abc

import numpy


class AbstractImageProcessor(abc.ABC):
    def __init__(self, image: numpy.array):
        self.image = image
        self.exif_data = ExifData(image_path)

    @abstractmethod
    def process_image(self):
        pass
