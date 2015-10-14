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
import random
import texture

class Scenario(texture.BaseScenario):

    @texture.printer
    def load(self):
        text = """
        Para llegar al edificio 7, puedes elegir las entradas F, G o E. También
        puedes ir hacia el edificio Sabatini o a la biblioteca.
        """

        return text

    def do_action(self, cmd):
        if (cmd == 'ir a E' or cmd == 'ir a entrada E'
            or cmd == 'E' or cmd == 'ir E'):

            self.open_bank()

            self.state['one_zone'] = 'E'
            self.state['time'] -= 30

            return 'load one_zero'

        if (cmd == 'ir a F' or cmd == 'ir a entrada F'
            or cmd == 'F' or cmd == 'ir F'):

            self.open_bank()

            self.state['one_zone'] = 'F'
            self.state['time'] -= 30

            return 'load one_zero'

        elif (cmd == 'ir Sabatini' or cmd == 'ir al Sabatini'
            or cmd == 'Sabatini' or cmd == 'ir 2' or cmd == 'ir al 2'):

            self.open_bank()

            self.state['sabatini_floor'] = 1
            self.state['sabatini_corner'] = 'C-D'
            self.state['time'] -= 30

            return 'load sabatini'

        elif (cmd == 'ir a G' or cmd == 'ir a entrada G'
            or cmd == 'G' or cmd == 'ir G'):

            self.state['one_zone'] = 'G'
            self.state['time'] -= 30

            return 'load one_zero'

        elif (cmd == 'ir a biblioteca' or cmd == 'ir a la biblioteca'
            or cmd == 'biblioteca' or cmd == 'ir biblioteca'):

            text = """
            Vas a la biblioteca.
            """

            texture.tprint(text)
            self.state['time'] -= 30

            return 'load biblioteca_hall'

        text = """
        El tiempo es oro, ¿a dónde vas a ir?
        """

        texture.tprint(text)

    @texture.printer
    def open_bank(self):
        # Time lost in minutes
        time_lost = random.randrange(2, 5)

        text = """
        De camino a la entrada aparece una muchacha con una carpeta entre los
        brazos. "Hola, ¿tienes un momentito? Vengo a ofrecerte una cuenta
        open-bank..."

        Saben los dioses el tiempo que te retuvo la muchaca. Entras en el
        edificio, miras tu teléfono, has perdido %d minutos.
        """ % time_lost

        self.state['time'] -= time_lost * 60

        return text
