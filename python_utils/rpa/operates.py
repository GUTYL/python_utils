from enum import IntEnum, unique
from typing import NamedTuple


@unique
class OperateType(IntEnum):
    LEFT_CLICK = 1
    LEFT_DOUBLE_CLICK = 2
    RIGHT_CLICK = 3
    RIGHT_DOUBLE_CLICK = 4
    WAIT = 5
    SCROLL = 6


ALL_OPERATE = [op.value for op in list(OperateType)]


class Operate(NamedTuple):
    operate_type: OperateType
    content: str
    re_try: int


class OperateBasic:

    def __init__(self, operate: Operate):
        self.operate = operate

    def _check_operate(self):
        if self.operate.operate_type not in ALL_OPERATE:
            raise Exception("Unsupported operate type.")

    def _check_input(self):
        raise Exception("Must inherit the implementation function.")

    def _define_operate(self):
        raise Exception("Must inherit the implementation function.")

    def do_operate(self):
        self._check_operate()
        self._check_input()
        self._define_operate()


class LeftClick(OperateBasic):
    def __init__(self, operate: Operate):
        super().__init__(operate)

    def _check_operate(self):
        super()._check_operate()
        if self.operate.operate_type != OperateType.LEFT_CLICK:
            return Exception("Operate code error.")

    def _check_input(self):
        pass

    def _define_operate(self):
        pass
