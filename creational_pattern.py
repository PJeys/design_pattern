# prototype design pattern
import copy


class RefEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent


class Shape:
    def __init__(self, color: str, area: float, ref_ent, params: list):
        self.color = color
        self.area = area
        self.ref_ent = ref_ent
        self.params = params

    def __copy__(self):
        ref_ent = copy.copy(self.ref_ent)
        params = copy.copy(self.params)

        new_copy = self.__class__(
            self.color, self.area, ref_ent, params
        )
        new_copy.__dict__.update(self.__dict__)
        return new_copy

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}

        ref_ent = copy.copy(self.ref_ent)
        params = copy.copy(self.params)

        new_copy = self.__class__(
            self.color, self.area, ref_ent, params
        )
        new_copy.__dict__ = copy.deepcopy(self.__dict__, memodict)
        return new_copy


def main():
    ref_ent = RefEntity()
    rect = Shape('green', 123, ref_ent, [1, 123])
    print(rect.__dict__)
    copied = copy.copy(rect)
    print(copied.__dict__)
    copied.params.append(2)
    print(rect.__dict__, copied.__dict__)


if __name__ == '__main__':
    main()
