# This file is part of gerkin-by-example
#
# Copyright (C) 2021 Rafael Guterres Jeffman
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <https://www.gnu.org/licenses/>.

"""Steps implementation for system level."""


import subprocess

from behave import given, then, when  # pylint: disable=no-name-in-module


@given("the input is")
def _given_input(context):
    context.stdin_data = context.text


@when('the program "{program}" runs')
def _when_program_runs(context, program):
    context.result = subprocess.run(
        ["python", "-m", program],
        capture_output=True,
        check=True,
        input=context.stdin_data.encode("utf-8"),
    )


@then("the output should be")
def _then_output_should_be(context):
    #print(f'1 conteudo: {str(context.text)}')
    #print(f'1 tamanho : {len(str(context.text))}')
    #print(f'1 tipo    : {type(str(context.text))}')
    assertion1 = str(context.text).replace(" ", "")
    assertion1 = assertion1.replace("\n", "")
    #print(f'1 split     : {assertion1}')
    #print(f'1 split size: {len(assertion1)}')
    #print(f'1 split tipo: {type(assertion1)}')
    
    #print(f'2 conteudo: {str(context.result.stdout.decode("utf-8"))}')
    #print(f'2 tamanho : {len(str(context.result.stdout.decode("utf-8")))}')
    #print(f'2 tipo    : {type(str(context.result.stdout.decode("utf-8")))}')
    assertion2 = str(context.result.stdout.decode("utf-8")).replace(" ", "")
    assertion2 = assertion2.replace("\n", "")
    assertion2 = assertion2[:-1]
    #print(f'2 split     : {assertion2}')
    #print(f'2 split size: {len(assertion2)}')
    #print(f'2 split tipo: {type(assertion2)}')
    
    assert assertion1 == assertion2
