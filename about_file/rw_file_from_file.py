# -*- coding:utf-8 -*-
# __author__ = xuejun
import os


def write_from_file(read_file_path, write_file_path):
    """
    Read the string from the file and get some values from the string to store in another file.
    The format of these strings just like this:
    "buckets": [
        {
            "key": "Seoul","doc_count": 10584235},{
            "key": "Mexico City","doc_count": 4935912},{
            "key": "Ashburn","doc_count": 4560792},{
            "key": "Beijing","doc_count": 4237792}]
    :param read_file_path:
    :param write_file_path:
    :return:None
    """

    file_list = os.listdir(read_file_path)

    for file_item in file_list:
        with open(read_file_path + '/' + file_item, 'r') as fi:
            fi_str = fi.read().strip().replace('\n', '')
            fi_str_tuple = fi_str.partition(":")
            fi_str_lst = eval(fi_str_tuple[2].strip()[1:-1]) # This is an effective method to  handle these problems.

            key_value_lst = [item['key'] for item in fi_str_lst if item['key'] and item['key'] not in ['none', '']]

            with open(write_file_path + '/' + file_item, 'w') as fw:
                fw.write(str(key_value_lst))