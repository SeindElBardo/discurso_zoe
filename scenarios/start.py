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

LOGO = """
 -/++++++++++++++/++++++++++++++++++++++++++++++++++++++++++++/-
/++++++++++++++++//+++++++++++++++++++++++++++++++++++++++++++++/
++++++++++++++++++.-+++++++++++++++++++++++++++++++++++++++++++++
+++++++++/++++++++:  ./++++++++++++++++++++++++++++++++++++++++++
+++++++++/-+++++++-    ./++++++++++++++++++++++++++++++++++++++++
++++++++++-`/+++++`      -+++++++++++++++++++++++++++++++++++++++
+++++++++++ `:++/`        `/+++++++++++++++++++++++++++++++++++++
+++++++++++`  `.:-.         -/+++++++++++++++++++++++++++++++++++
++++++++++/      `.--.        `.--::://++++++++++++++++++++++++++
++++++++++.          `..`              `.-:++++++++++++++++++++++
++++++++++:             `                  `-++++++++++++++++++++
++++++++++/:                          `..-`  -+++++++++++++++++++
++++++++:. .:                      `.:/+++/`  .:/++++++++++++++++
++++++:`    .:`                  `--````.://     `-:/++++++++++++
++++:`       `.                  ``       ``        `./++++++++++
+/-`                                                  :++++++++++
.`                                                    /++++++++++
                                                   `.-+++++++++++
                                          ```.://:.++++++++++++++
                    `                   -/++/+++++/++++++++++++++
                    .                  /+++++++++++++++++++++++++
                    -                  -+++++++++++++++++++++++++
                    `.     `            `-+++++++++++++++++++++++
                     .    `/`      .`     .:++++:++++++++++++++++
                      -   :/`     `:        `.-`-++++++++++++++++
                      `-  :-.     :`           `+++++++++++++++++
                       `:`:.:    `/          `./+++++++++++++++++
                        `/: /    ./.....--://++++++++++++++++++++
                            --   .+++++++++++++++++++++++++++++++
                          `.-+-   +++++++++++++++++++++++++++++++
                        -++++++/. -++++++++++++++++++++++++++++++
                      .+++++++++++:/++++++++++++++++++++++++++++/
                    `:++++++++++++++++++++++++++++++++++++++++/-
"""

TITLE = """
 ___ _     __  _   __   ____  _ ___   __   __    __  ___   ___ __  ___
| __| |   | _\| |/' _/ / _/ || | _ \/' _/ /__\  | _\| __| |_  /__\| __|
| _|| |_  | v | |`._`.| \_| \/ | v /`._`.| \/ | | v | _|   / / \/ | _|
|___|___| |__/|_||___/ \__/\__/|_|_\|___/ \__/  |__/|___| |___\__/|___|
"""

class Scenario(texture.BaseScenario):

    def load(self):
        texture.tclear()
        texture.tprint(LOGO, False)

        texture.tnewline()
        texture.tprint(TITLE, False)

        texture.tnewline()
        texture.tprint('Guión: Adrián Borja')
        texture.tprint('Motor: Rafael Medina')

        texture.tnewline()
        texture.tprint('Escribe "comenzar" para iniciar la partida')

        # Set initial states
        self.state = {}
        self.state['time'] = 850
        self.state['in_start'] = True

    def do_action(self, cmd):
        if cmd == 'comenzar':
            return 'load biblioteca_ai'

        else:
            texture.tprint('Escribe "comenzar" para iniciar la partida')
