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

@domain
Feature: Factorial

Narrative:

I want to be told the factor of a number

Scenario Outline: Factor a number

Given the number <a>
When you execute the factorial
Then the result should be <x>

Examples:
| a |  x             |
| 2 |  2             |
| 3 |  6             |
| 4 | 24             |
|-1 | Input Invalido |
| 15| Input Invalido |
