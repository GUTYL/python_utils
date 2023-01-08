# python file operations
import logging
import os

from chardet.universaldetector import UniversalDetector


def get_encoding_type(file):
    """get file encoding type

    :param file:
    :return: file encoding
    """
    detector = UniversalDetector()
    detector.reset()
    with open(file, 'rb') as f:
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    return detector.result["encoding"]


def file_to_utf8(file_dir, to_encoding='utf8'):
    """dir txt encoding to utf8

    :param to_encoding:
    :param file_dir:
    :return:
    """
    for src_file in os.listdir(file_dir):
        logging.info(src_file)
        tmp_path = os.path.join(file_dir, src_file + '.swp')
        src_path = os.path.join(file_dir, src_file)
        from_codec = get_encoding_type(src_path)
        try:
            with open(src_path, encoding=from_codec) as f:
                with open(tmp_path, 'w', encoding=to_encoding) as e:
                    text = f.read()
                    e.write(text)
            os.remove(src_path)
            os.rename(tmp_path, src_path)
        except Exception as error:
            logging.error(error)
    return os.listdir(file_dir)[0]
