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

Feature: URI1001 CLI

Narrative:

I want to be told the factor of a number

Scenario: Run program with 2 (pos)

Given the input is
"""
2
"""
When the program "factorial" runs
Then the output should be
"""
factor = 2

"""

Scenario: Run program with 3 (pos)

Given the input is
"""
3
"""
When the program "factorial" runs
Then the output should be
"""
factor = 6

"""

Scenario: Run program with 4 (pos)

Given the input is
"""
4
"""
When the program "factorial" runs
Then the output should be
"""
factor = 24

"""

Scenario: Run program with -1 (neg)

Given the input is
"""
-1
"""
When the program "factorial" runs
Then the output should be
"""
factor = Input Invalido

"""

Scenario: Run program with 15 (pos)

Given the input is
"""
15
"""
When the program "factorial" runs
Then the output should be
"""
factor = Input Invalido

"""
