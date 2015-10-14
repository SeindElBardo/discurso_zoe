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
        En la máquina de café no hay cola, cosa bastante rara. Las únicas
        puertas útiles son las del baño y la de salida, pues consideras que en
        la planta superior no tienes nada que hacer y en las salas de estudio
        menos, aunque siempre puedes volver a bajar al aula de informática.
        """

        return text

    def do_action(self, cmd):
        if (cmd == 'ir al baño' or cmd == 'ir a baño'
            or cmd == 'baño' or cmd == 'ir baño'):

            text = """
            ¡Oh, qué alivio!

            Vuelves al hall
            """

            self.state['time'] -= 50

        elif cmd == 'bajar':
            self.state['time'] -= 10
            return 'load biblioteca_ai'

        elif cmd == 'comprar café' or cmd == 'tomar café' or cmd == 'café':
            self.state['time'] -= 20
            text = """
            No llevas dinero encima, te jodes.
            """

        elif cmd == 'salir':
            return 'load exterior_bo'

        else:
            text = """
            Si haces algo raro, los bibliotecarios te echarán la bronca.
            """

        texture.tprint(text)
