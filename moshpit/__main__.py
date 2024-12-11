# ----------------------------------------------------------------------------
# Copyright (c) 2016-2024, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click
import q2cli.commands


ROOT_COMMAND_HELP = """\
MOSHPIT command-line interface (q2cli)
--------------------------------------

To get help with MOSHPIT, visit:

    https://bokulich-lab.github.io/moshpit-docs/intro.html

To enable tab completion in Bash, run the following command or add it to your \
.bashrc/.bash_profile:

    source tab-mosh

To enable tab completion in ZSH, run the following commands or add them to \
your .zshrc:

\b
    autoload -Uz compinit && compinit
    autoload bashcompinit && bashcompinit
    source tab-mosh

"""


# Entry point for CLI
@click.command(cls=q2cli.commands.RootCommand, invoke_without_command=True,
               no_args_is_help=True, help=ROOT_COMMAND_HELP)
@click.version_option(prog_name='mosh',
                      message='%(prog)s version %(version)s\nRun `mosh info` '
                              'for more version details.')
def mosh():
    pass


if __name__ == '__main__':
    mosh()
