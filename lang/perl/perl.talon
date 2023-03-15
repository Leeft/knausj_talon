tag: user.perl
-
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_comment_line
#tag(): user.code_comment_block_c_like
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
#tag(): user.code_operators_bitwise
#tag(): user.code_operators_lambda
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_variable_formatter = "PRIVATE_CAMEL_CASE"

(perl | op) (equal | equals | eek): " == "
(perl | op) not (equal | equals | eek): " != "
(perl | op) string (equal | equals | eek): " eq "
(perl | op) string not (equal | equals | eek): " ne "

perl hash bang: "#!/usr/bin/env perl\n"
see pan (m | em | minus): "cpanm "
(warren | worn | warn): "warn "
use pragmas: "use utf8;\nuse Modern::Perl;\n"
use moose: "use utf8;\nuse Moose;\n"
use printer: "use Data::Printer;\n"
perl use: "use "
perl require: "require "
perl local: "local "
perl my: "my "
perl keys: "keys "
perl scalar: "scalar "
perl sub: "sub "
perl like: "like "
perl shift: "shift "
perl defuse: "defuse_exception( $_ );"
perl (exists | exist): "exists "
perl (defined | define): "defined "
(op|perl) defined or: "//= "
perl [auto] increment: " += 1"
perl [auto] decrement: " -= 1"
perl match: " =~ "
op [perl] match: " =~ "
(perl|op) (no | negated) match: " !~ "
(perl|op) compare: " cmp "
perl (lowercase | lower): " lc "
perl (uppercase | upcase | upper): " uc "
perl map: "map "
op [perl] (diamond | input): "<q "
perl times: " x "

make immutable: "__PACKAGE__->meta->make_immutable;\n"

#state const: "const "

#state let: "let "

#state var: "var "

#state export: "export "

#state async: "async "

#state await: "await "

#dot {user.code_common_member_function}:
#    user.insert_between(".{code_common_member_function}(", ")")

#state map: app.notify('ERROR: Command deprecated; please use "dot map"')
#state filter: app.notify('ERROR: Command deprecated; please use "dot filter"')
#state reduce: app.notify('ERROR: Command deprecated; please use "dot reduce"')

yada yada: "..."

from import: user.insert_between(' from  "', '"')
