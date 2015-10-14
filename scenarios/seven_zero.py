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
        Un chico y una chica un poco distraidos vigilan la puerta hacia el
        exterior, deben pertenecer al BEHTS, mejor no tentar a la suerte.

        Las aulas informáticas son la 4 y la 5, la 5 está cerrada.
        """

        return text

    def do_action(self, cmd):
        if cmd == 'salir':
            text = """
            Claro, salgamos por la puerta que vigila gente de BEHTS,
            ¿qué podría salir mal?

            Te han pillado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'subir':
            text = """
            Subes a la primera planta.
            """

            texture.tprint(text)
            self.state['time'] -= 10

            return 'load seven_one'

        elif (cmd == 'ir a aula 4' or cmd == 'ir al aula 4'
            or cmd == 'ir aula 4' or cmd == 'aula 4'):

            if not self.state.get('usb_content', []):
                self.state['time'] -= 10
                return 'load seven_computer'

            else:
                text = """
                No tienes nada más que hacer ahí.
                """

        else:
            text = """
            Ya estás muy cerca del aula informática, sólo tienes que conseguir
            el discurso y salir de ahí. No lo estropees.
            """

        texture.tprint(text)
