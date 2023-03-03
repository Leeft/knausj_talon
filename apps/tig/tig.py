import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
mod.tag("tig", desc="For a terminal that provides the tig command")
ctx = Context()

mod.list("tig_command", desc="Tig commands.")
mod.list("tig_argument", desc="Command-line tig options and arguments.")

dirpath = Path(__file__).parent
arguments_csv_path = str(dirpath / "tig_arguments.csv")
commands_csv_path = str(dirpath / "tig_commands.csv")

def make_list(path):
    with resource.open(path, "r") as f:
        rows = list(csv.reader(f))
    mapping = {}
    # ignore header row
    for row in rows[1:]:
        if len(row) == 0:
            continue
        if len(row) == 1:
            row = row[0], row[0]
        if len(row) > 2:
            print("{path!r}: More than two values in row: {row}. Ignoring the extras.")
        output, spoken_form = row[:2]
        spoken_form = spoken_form.strip()
        mapping[spoken_form] = output
    return mapping


ctx.lists["self.tig_argument"] = make_list(arguments_csv_path)
ctx.lists["self.tig_command"] = make_list(commands_csv_path)

@mod.capture(rule="{user.tig_argument}+")
def tig_arguments(m) -> str:
    """A non-empty sequence of tig command arguments, preceded by a space."""
    return " " + " ".join(m.tig_argument_list)
