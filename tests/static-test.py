from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.lint import PyLinter


class MyAstroidChecker(BaseChecker):
    name = "b_akhmadkhan-checker"
    msgs = {
        "W0042": (
            "Variable name not equal to 'b_akhmadkhan'",
            "wrong-var-name",
            "Search for variable with name akhmadkhan",
        )
    }

    def visit_assignname(self, node: nodes.AssignName) -> None:
        if node.name != "b_akhmadkhan":
            self.add_message("wrong-var-name", node=node)


def register(linter: PyLinter) -> None:
    linter.register_checker(MyAstroidChecker(linter))
