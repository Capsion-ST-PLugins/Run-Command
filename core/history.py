# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-04-25 09:18:42.957356
# @Last Modified by: CPS
# @Last Modified time: 2022-04-25 09:18:42.958260
# @file_path "W:\CPS\IDE\SublimeText\JS_SublmieText\Data\Packages\cps_run_commands\core"
# @Filename "historyManager.py"
# @Description: 功能描述
#
import os

from typing import *
from dataclasses import *
from os import path


class History:
    def __init__(self, file_path: str, max_count: int = 500, repeat=False):
        """
        @Description {description}

        - param file_path :{str}  {description}
        - param max_count :{int}  {description}
        - param repeat    :{bool} 是否记录重复命令

        returns `{type}` {description}

        """
        self.file_path = file_path
        self.max_count = max_count - 1
        self.repeat = repeat
        self.data = []  # list[str]

        self.check_file_path()
        # print('init History: ', self.data)

    def delete_by_index(self, index: int):
        if index > len(self.data):
            return

        self.data.remove(self.data[index])
        self.dump()

    def check_file_path(self):
        try:
            if not os.path.exists(self.file_path):
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.write("")
            else:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = f.read().split("\n")
                    self.data = list(set(data))

            return self

        except Exception as err:
            print(err)
            raise FileExistsError

    def add(self, histroy: str):
        if not self.repeat:
            if histroy in self.data:
                return self

        while len(self.data) > self.max_count:
            self.data.pop()

        self.data.insert(0, histroy)
        self.dump()
        return self

    def dump(self):
        self.data = list(set(self.data))
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(self.data))
        return self

    def __str__(self):
        return ",".join(self.data)

    # def __getitem__(self, target):
    #     if isinstance(target, int) and target -1 <= self.max_count:
    #         return self.data[target - 1]


if __name__ == "__main__":
    import sys

    print(sys.path)
