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

class Scenario(texture.BaseScenario):

    @texture.printer
    def load(self):
        text = """
        Sales al exterior, todo parece normal salvo por un grupo de
        universitarios bebiendo sangría en el cesped, te invitan a unirte a
        ellos.
        """

        return text

    def do_action(self, cmd):
        if cmd == 'aceptar' or cmd == 'acepto':
            text = """
            Te unes a ellos, te montas tal juerga que se te hace tarde y
            fracasas en tu misión.
            """

            texture.tprint(text)
            return 'load game_over'

        elif cmd == 'rechazar' or cmd == 'rechazo':
            text = """
            Te llaman soso, pero tienes que continuar con tu misión.
            """

            texture.tprint(text)
            return 'load exterior_ir'

        text = """
        No es momento de tonterías, ¿aceptas o rechazas su invitación?
        """

        texture.tprint(text)
