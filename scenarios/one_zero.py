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
        if self.state['one_zone'] == 'B':
            text = """
            Parece despejado. Puedes salir al exterior o ir a los pasillos E, F
            o C, o subir a la planta de arriba, lo cual te da mala espina.
            """

        elif self.state['one_zone'] == 'C':
            text = """
            Te llama la atención que en la puerta de salida del edificio hacia
            el 7 hay un joven que te mira sospechosamente. Debe ser uno del
            BEHTS, aunque es probable que sea un novato, pues parece que no
            está seguro de si eres un alumno random o un siervo de Zoe.
            Piensas que es mejor no tentar a la suerte.

            Aparte de la puerta que vigila el joven, puedes ir a los pasillos F,
            B o G, o subir las escaleras.
            """

        elif self.state['one_zone'] == 'E':
            text = """
            Estás en la entrada del edificio, todo en orden. Ves las escaleras
            para subir al primer piso, aunque se oye mucho ruido, mejor no ir
            por ahi, el pasillo que comunica con la zona B y la puerta para
            salir del edificio.
            """

        elif self.state['one_zone'] == 'F':
            text = """
            Estás en la entrada del edificio, nada que te llame la atención.
            Ves las escaleras para subir al primer piso y el pasillo que
            comunica con las zonas B o C y la puerta para salir del edificio.
            """

        elif self.state['one_zone'] == 'G':
            text = """
            Estás en la entrada del edificio, nada fuera de lo común. Ves las
            escaleras para subir al primer piso, el pasillo que comunica con
            la zona C y la puerta para salir del edificio.
            """

        return text

    def do_action(self, cmd):
        if self.state['one_zone'] == 'B':
            return self.actions_b(cmd)

        elif self.state['one_zone'] == 'C':
            return self.actions_c(cmd)

        elif self.state['one_zone'] == 'E':
            return self.actions_e(cmd)

        elif self.state['one_zone'] == 'F':
            return self.actions_f(cmd)

        elif self.state['one_zone'] == 'G':
            return self.actions_c(cmd)

        text = """
        No es buena idea quedarse aquí.
        """

        texture.tprint(text)

    def actions_b(self, cmd):
        if cmd == 'ir a C' or cmd == 'ir C':
            self.state['one_zone'] = 'C'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a E' or cmd == 'ir E':
            self.state['one_zone'] = 'E'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a F' or cmd == 'ir F':
            self.state['one_zone'] = 'F'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            text = """
            Subes por las escaleras y tienes la mala suerte de encontrarte
            de frente con alguien del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'salir':
            return 'load exterior_ir'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)

    def actions_c(self, cmd):
        if cmd == 'ir a B' or cmd == 'ir B':
            self.state['one_zone'] = 'B'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a F' or cmd == 'ir F':
            self.state['one_zone'] = 'F'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a G' or cmd == 'ir G':
            self.state['one_zone'] = 'G'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            self.state['time'] -= 10
            return 'load one_one'

        elif cmd == 'salir':
            text = """
            Mira por dónde, has tentado a la suerte y has perdido. El BEHTS
            te ha atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)

    def actions_e(self, cmd):
        if cmd == 'ir a B' or cmd == 'ir B':
            self.state['one_zone'] = 'B'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            text = """
            Subes por las escaleras y tienes la mala suerte de encontrarte
            de frente con alguien del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'salir':
            return 'load exterior_ir'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)

    def actions_f(self, cmd):
        if cmd == 'ir a B' or cmd == 'ir B':
            self.state['one_zone'] = 'B'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a C' or cmd == 'ir C':
            self.state['one_zone'] = 'C'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            self.state['time'] -= 10
            return 'load one_one'

        elif cmd == 'salir':
            return 'load exterior_ir'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)

    def actions_g(self, cmd):
        if cmd == 'ir a C' or cmd == 'ir C':
            self.state['one_zone'] = 'C'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            self.state['time'] -= 10
            return 'load one_one'

        elif cmd == 'salir':
            return 'load exterior_ir'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)
