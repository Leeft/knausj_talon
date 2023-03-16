import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.perl
"""

ctx.lists["user.code_common_function"] = {
    "params": "params",
    "undef": "undef",
    "perl": "perl",
    "diag": "diag",
    "note": "note",
    "validate": "validate",
    "deeply": "cmp_deeply",
    "superhashof": "superhashof",
}

mod.list("moose_type", "Commonly used Moose types")

ctx.lists["user.moose_type"] = {
    "boolean": "Bool",
    "integer": "Int",
    "positive integer": "PositiveInt",
    "positive or zero integer": "PositiveOrZeroInt",
    "string": "Str",
    "none": "None",
    "dick": "Dict",
    "float": "Num",
    "any": "Any",
    "tuple": "Tuple",
    "list": "ArrayOf",
    "list of": "ArrayOf",
    "list ref": "ArrayRef",
    "hash": "HashRef",
    "hash ref": "HashRef",
}

ctx.lists["user.logging_levels"] = {
    "debug": "debug",
    "info": "info",
    "notice": "notice",
    "warn": "warn",
    "warning": "warn",
    "error": "error",
    "critical": "critical",
    "alert": "alert",
    "emergency": "emergency",
}

@ctx.action_class("user")
class UserActions:
    def code_operator_object_accessor():
        actions.auto_insert("->")

    def code_self():
        actions.auto_insert("$this")

    def code_define_class():
        actions.insert("package ")

    def code_operator_address_of():
        actions.auto_insert("&")

    def code_operator_structure_dereference():
        actions.auto_insert("->")

    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    # def code_operator_string_equal():
    #     actions.auto_insert(" eq ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    # def code_operator_string_not_equal():
    #     actions.auto_insert(" ne ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" and ")

    def code_operator_or():
        actions.auto_insert(" or ")

    def code_insert_null():
        actions.auto_insert("undef")

    def code_insert_is_null():
        actions.auto_insert(" not defined ")

    def code_insert_is_not_null():
        actions.auto_insert(" defined ")

    def code_state_if():
        actions.insert("if (  ) {}")
        actions.key("left enter up right")

    def code_state_else_if():
        actions.insert("elsif () {\n}\n")
        actions.key("up:2 left:3")

    def code_state_else():
        actions.insert("else\n{\n}\n")
        actions.key("up:2")

    def code_state_for():
        actions.auto_insert("for ")

    def code_state_for_each():
        actions.auto_insert("foreach ")

    def code_state_while():
        actions.insert("while ()")
        actions.edit.left()

    def code_state_return():
        actions.auto_insert("return ")

    # def code_last():
    #     actions.auto_insert("last;")

    # def code_next():
    #     actions.auto_insert("next;")

    def code_insert_true():
        actions.auto_insert("JSON::XS::true")

    def code_insert_false():
        actions.auto_insert("JSON::XS::false")

    def code_comment_line_prefix():
        actions.auto_insert("#")

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    # TODO - it would be nice that you integrate that types from c_cast
    # instead of defaulting to void
    # def code_private_function(text: str):
    #     """Inserts private function declaration"""
    #     result = "void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    # def code_private_static_function(text: str):
    #     """Inserts private static function"""
    #     result = "static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_insert_library(text: str, selection: str):
        actions.user.paste(f"use {text};")

    def code_block():
        actions.user.insert_between("{", "}")
        actions.key("enter")

    def code_operator_in():
        """code_operator_in"""

    def code_operator_not_in():
        """code_operator_not_in"""
