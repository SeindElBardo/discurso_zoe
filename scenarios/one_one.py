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
        if self.state['one_zone'] == 'C':
            text = """
            No parece que haya nadie en los pasillos F y G. Puedes ver que la
            puerta hacia el edificio 7, también está despejada. En el pasillo B
            hay un cartel que dice "¡Sexo Gratis!".
            """

        elif self.state['one_zone'] == 'F':
            text = """
            No hay nadie en este pasillo, aunque 2 chicas del BEHTS hablan en
            la escalera hacia el segundo piso sobre una fiesta en Getafe después
            de capturar al siervo de Zoe. Por suerte no han reparado en tu belleza
            interior como estudiante de ingeniería.

            Puedes ir a los pasillos B o C o bajar a la planta baja.
            """

        elif self.state['one_zone'] == 'G':
            text = """
            Reconoces a alguien sospechoso sentado en el último escalón del
            tramo que sigue hacia la segunda planta mirando su móvil.
            Parece que no te ha visto, pero crees que puede ser un
            miembro del BEHTS.

            Puedes ir al pasillo C o bajar. Mejor no subir.
            """

        return text

    def do_action(self, cmd):
        if self.state['one_zone'] == 'C':
            return self.actions_c(cmd)

        elif self.state['one_zone'] == 'F':
            return self.actions_f(cmd)

        elif self.state['one_zone'] == 'G':
            return self.actions_c(cmd)

        text = """
        No es buena idea quedarse aquí.
        """

        texture.tprint(text)

    def actions_c(self, cmd):
        if cmd == 'ir a B' or cmd == 'ir B':
            text = """
            Das la vuelta a la esquina y tienes la mala suerte de encontrarte
            de frente con alguien del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'ir a F' or cmd == 'ir F':
            self.state['one_zone'] = 'F'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a G' or cmd == 'ir G':
            self.state['one_zone'] = 'G'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'ir a 7' or cmd == 'ir al 7' or cmd == 'ir 7':
            text = """
            Cruzas el pasillo y llegas al edificio 7.
            """

            self.state['time'] -= 30
            texture.tprint(text)

            return 'load seven_one'

        elif cmd == 'subir':
            text = """
            Por alguna razón desconocida sientes la imperiosa necesidad de
            subir a la segunda planta. Es una lástima que esta planta esté
            llena de miembros del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'bajar':
            self.state['time'] -= 10
            return 'load one_zero'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)

    def actions_f(self, cmd):
        if cmd == 'ir a B' or cmd == 'ir B':
            text = """
            Das la vuelta a la esquina y tienes la mala suerte de encontrarte
            de frente con alguien del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'ir a C' or cmd == 'ir C':
            self.state['one_zone'] = 'C'
            self.state['time'] -= 10

            self.load()

        elif cmd == 'subir':
            text = """
            Por alguna razón desconocida sientes la imperiosa necesidad de
            subir a la segunda planta. Es una lástima que esta planta esté
            llena de miembros del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'bajar':
            self.state['time'] -= 10
            return 'load one_zero'

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
            text = """
            Por alguna razón desconocida sientes la imperiosa necesidad de
            subir a la segunda planta. Es una lástima que esta planta esté
            llena de miembros del BEHTS. Te han atrapado.
            """

            texture.tprint(text)

            return 'load game_over'

        elif cmd == 'bajar':
            self.state['time'] -= 10
            return 'load one_zero'

        else:
            text = """
            No es buena idea quedarse aquí.
            """

            texture.tprint(text)
