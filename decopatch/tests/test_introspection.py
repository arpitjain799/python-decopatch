from utils_disambiguation import disambiguate_using_introspection, FirstArgDisambiguation


def test_on_functions():

    def level1():
        return disambiguate_using_introspection(3)

    def my_decorator(arg):
        my_decorator.res = level1()
        if my_decorator.res is FirstArgDisambiguation.is_decorated_target:
            return "replacement"
        elif my_decorator.res is FirstArgDisambiguation.is_normal_arg:
            def _apply(f):
                return "replacement"
            return _apply
        else:
            raise Exception()

    @my_decorator
    def foo():
        pass

    assert my_decorator.res == FirstArgDisambiguation.is_decorated_target

    @my_decorator(foo)
    def foo():
        pass

    assert my_decorator.res == FirstArgDisambiguation.is_normal_arg
