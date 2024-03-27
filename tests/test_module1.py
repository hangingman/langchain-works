from mini_qa import module1


class TestModule1:
    def test_some_function(self) -> None:
        assert module1.some_function("foo") == "hello, foo"
