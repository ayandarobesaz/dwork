import abc
from typing import Any
from .types import Type


def binary_op(op, left, right):
    if not isinstance(left, Expression):
        left = to_expression(left)
    if not isinstance(right, Expression):
        right = to_expression(right)
    return op(left, right)


class Expression(abc.ABC):
    def __add__(self, right: Any) -> "Expression":
        from .operators import Add

        return binary_op(Add, self, right)

    def __sub__(self, right: Any) -> "Expression":
        from .operators import Sub

        return binary_op(Sub, self, right)

    def __mul__(self, right: Any) -> "Expression":
        from .operators import Mul

        return binary_op(Mul, self, right)

    def __truediv__(self, right: "Expression") -> "Expression":
        from .operators import TrueDiv

        return binary_op(TrueDiv, self, right)

    def __floordiv__(self, right: "Expression") -> "Expression":
        from .operators import FloorDiv

        return binary_op(FloorDiv, self, right)

    @abc.abstractproperty
    def type(self) -> Type:
        raise NotImplementedError

    def is_dp(self) -> bool:
        """
        Returns `True` if the value of this expression already fulfills
        the DP property.
        """
        return False

    def sum(self) -> "Expression":
        """
        Returns the sum of an expression. Assumes that the expression is indexable.
        """
        from .functions import Sum

        return Sum(self)

    @abc.abstractmethod
    def true(self) -> Any:
        raise NotImplementedError

    @abc.abstractmethod
    def sensitivity(self) -> Any:
        raise NotImplementedError

    @abc.abstractmethod
    def dp(self, epsilon: float) -> Any:
        raise NotImplementedError
