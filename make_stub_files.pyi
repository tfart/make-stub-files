import ast
import optparse
Node = ast.Node
from typing import Dict, Optional, Sequence
class AstFormatter:
    def format(self, node: Node) -> str: ...
    def visit(self, node: Node) -> str: ...
    def do_ClassDef(self, node: Node) -> str: ...
    def do_FunctionDef(self, node: Node) -> str: ...
    def do_Interactive(self, node: Node) -> None: ...
    def do_Module(self, node: Node) -> str: ...
    def do_Lambda(self, node: Node) -> str: ...
    def do_Expr(self, node: Node) -> str: ...
    def do_Expression(self, node: Node) -> str: ...
    def do_GeneratorExp(self, node: Node) -> str: ...
    def do_AugLoad(self, node: Node) -> str: ...
    def do_Del(self, node: Node) -> str: ...
    def do_Load(self, node: Node) -> str: ...
    def do_Param(self, node: Node) -> str: ...
    def do_Store(self, node: Node) -> str: ...
    def do_arguments(self, node: Node) -> str: ...
    def do_arg(self, node: Node) -> str: ...
    def do_Attribute(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Call(self, node: Node) -> str: ...
    def do_keyword(self, node: Node) -> str: ...
    def do_comprehension(self, node: Node) -> str: ...
    def do_Dict(self, node: Node) -> str: ...
    def do_Ellipsis(self, node: Node) -> str: ...
    def do_ExtSlice(self, node: Node) -> str: ...
    def do_Index(self, node: Node) -> str: ...
    def do_List(self, node: Node) -> str: ...
    def do_ListComp(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Repr(self, node: Node) -> str: ...
    def do_Slice(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
    def do_Subscript(self, node: Node) -> str: ...
    def do_Tuple(self, node: Node) -> str: ...
    def do_BinOp(self, node: Node) -> str: ...
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Compare(self, node: Node) -> str: ...
    def do_UnaryOp(self, node: Node) -> str: ...
    def do_IfExp(self, node: Node) -> str: ...
    def do_Assert(self, node: Node) -> str: ...
    def do_Assign(self, node: Node) -> str: ...
    def do_AugAssign(self, node: Node) -> str: ...
    def do_Break(self, node: Node) -> str: ...
    def do_Continue(self, node: Node) -> str: ...
    def do_Delete(self, node: Node) -> str: ...
    def do_ExceptHandler(self, node: Node) -> str: ...
    def do_Exec(self, node: Node) -> str: ...
    def do_For(self, node: Node) -> str: ...
    def do_Global(self, node: Node) -> str: ...
    def do_If(self, node: Node) -> str: ...
    def do_Import(self, node: Node) -> str: ...
    def get_import_names(self, node: Node) -> str: ...
    def do_ImportFrom(self, node: Node) -> str: ...
    def do_Pass(self, node: Node) -> str: ...
    def do_Print(self, node: Node) -> str: ...
    def do_Raise(self, node: Node) -> str: ...
    def do_Return(self, node: Node) -> str: ...
    def do_TryExcept(self, node: Node) -> str: ...
    def do_TryFinally(self, node: Node) -> str: ...
    def do_While(self, node: Node) -> str: ...
    def do_With(self, node: Node) -> str: ...
    def do_Yield(self, node: Node) -> str: ...
    def kind(self, node: Node) -> str: ...
    def indent(self, s: str) -> str: ...
    def op_name(self, node: Node, strict: bool=True) -> str: ...
class Pattern:
    def __init__(self, find_s, repl_s, trace=False) -> None: ...
    def __repr__(self) -> str: ...
    def is_balanced(self) -> bool: ...
    def all_matches(self, s: str, trace=False) -> Sequence: ...
    def full_balanced_match(self, s: str, i: int, trace=False) -> Optional[int]: ...
    def match_balanced(self, delim, s: str, i: int) -> int, len(str)+number: ...
    def match_entire_string(self, s: str) -> bool, j is not None: ...
class StandAloneMakeStubFile:
    def __init__(self) -> None: ...
    def finalize(self, fn: str) -> str: ...
    def make_stub_file(self, fn: str) -> None: ...
    def run(self) -> None: ...
    def run_all_unit_tests(self) -> None: ...
    def scan_command_line(self) -> None: ...
    def scan_options(self) -> None: ...
    def scan_patterns(self, section_name) -> Sequence: ...
class StubFormatter(AstFormatter):
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
class StubTraverser(ast.NodeVisitor):
    def __init__(self, controller: StandAloneMakeStubFile) -> None: ...
    def indent(self, s: str) -> str: ...
    def out(self, s: str) -> None: ...
    def run(self, node: Node) -> None: ...
    def visit_ClassDef(self, node: Node) -> None: ...
    def visit_FunctionDef(self, node: Node) -> None: ...
    def format_arguments(self, node: Node) -> str: ...
    def format_returns(self, node: Node) -> str: ...
    def get_def_name(self, node: Node) -> name: ...
    def munge_arg(self, s: str) -> str: ...
    def munge_ret(self, name, s: str) -> str: ...
    def match_patterns(self, name, patterns, s: str) -> (found,str): ...
    def visit_Return(self, node: Node) -> None: ...
def main() -> None: ...
def pdb() -> None: ...
