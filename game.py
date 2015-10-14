# -*- coding: utf-8 -*-
#
# El discurso de Zoe
#
# Copyright (C) 2015  GUL UC3M
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import texture
import scenarios
import math
import sys

def game_restart(state):
    """ Restart the game. """
    state = {}

    return 'load start'

def game_exit(state):
    """ End the game. """
    sys.exit('¡Gracias por jugar!')

def game_time(state):
    """ Show time. """
    mins = math.floor(state['time'] / 60)
    secs = state['time'] % 60

    texture.tprint('Te quedan %d minutos %d segundos.' % (
        mins, secs))

    return 'continue'


if __name__ == '__main__':
    gm = texture.GameMaster()

    # Register special commands
    gm.register_command('RESTART', game_restart)
    gm.register_command('EXIT', game_exit)
    gm.register_command('tiempo', game_time)

    gm.start_game()
