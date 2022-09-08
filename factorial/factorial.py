# This file is part of gerkin-by-example
#
# Copyright (C) 2021 Guilherme Cavalheiro
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

"""Implement the domain."""

import math

class Factorial:
    """A helper for factorial."""

    def __init__(self):
        """Initialize factorial object."""
        self.N = 0

    def add_input(self, value):
        """Add a new input to the factorial."""
        if 0 >= value or value >= 13:
            self.N = -1
        else:
            self.N = value

    def do_factorial(self):
        """Factorial of N."""
        if self.N == -1:
            return 'Input Invalido'
        else:
            return math.factorial(self.N)