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
import math
import random
import texture


class Scenario(texture.BaseScenario):

    @texture.printer
    def load(self):
        text = """
        Acabas de entrar en el edifio 2, el Sabatini. Tienes que
        encontrar el despacho del GUL y llevar el discurso de Zoe para el
        programa de radio en directo a tiempo.

        Un escalofrio recorre tu espalda, sabes que da igual el tiempo que
        lleves en esta universidad, siempre que busques un aula en este
        edificio te vas a perder.

        Respiras hondo y te preparas para encontrar el despacho, subes las
        esclaras, pues fijate que oportuno, ningún ascensor funciona.

        Te encuentras en la esquina C-D de la planta 1. Puedes ir al pasillo
        de la derecha, al de la izquierda, subir o bajar las escaleras.
        """

        return text

    def do_action(self, cmd):
        if self.state.get('sabatini_flee', False):
            return self.must_flee(cmd)

        if (cmd == 'ir izquierda' or cmd == 'ir a la izquierda'
                or cmd == 'izquierda'):
            self.go_somewhere('l')

        elif (cmd == 'ir derecha' or cmd == 'ir a la derecha'
                or cmd == 'derecha'):
            self.go_somewhere('r')

        elif cmd == 'subir':
            self.go_up()

        elif cmd == 'bajar':
            down =  self.go_down()
            if down: return down

        elif (self.state['sabatini_floor'] == 3
                and (cmd == 'despacho' or cmd == 'comprobar despacho'
                or cmd == 'ir al despacho' or cmd == 'ir a despacho'
                or cmd == 'ir despacho')):

            if self.state['sabatini_corner'] != 'B-C':

                text = """
                Ninguno de los 2 despachos que hay en esta esquina es el del
                GUL, además según te ven empiezan a pegar voces, se ve que los
                del BEHTS les han prometido una bolsa de chuches si les
                avisaban al verte. Deberias huir.
                """

                texture.tprint(text)

                self.state['sabatini_flee'] = True
                self.state['time'] -= 10
                return

            # Despacho del GUL
            if not self.state.get('usb_content', []):
                text = """
                Has llegado al despacho del GUL, pero no traes lo que se te
                ha pedido. Al acercarte a la puerta puedes oír a gente
                hablando muy rápido. Parecen estar nerviosos.

                Decides que no puedes entrar así como así sin el discurso de
                Zoe y te alejas.
                """

                texture.tprint(text)
                return

            text = """
            ¡Has llegado al despacho del GUL!
            """

            texture.tprint(text)
            return 'load gul'

        else:
            text = """
            Sólo un poco más...
            """

            texture.tprint(text)
            return

        self.random_encounter()

    def go_down(self):
        if self.state['sabatini_floor'] == 1:
            text = """
            Sales del edificio.
            """

            texture.tprint(text)

            return 'load exterior_ir'

        self.state['sabatini_floor'] -= 1
        text = """
        Bajas una planta.

        Estás en la planta """ + str(self.state['sabatini_floor'])

        texture.tprint(text)

        self.state['time'] -= 10

    @texture.printer
    def go_up(self):
        if self.state['sabatini_floor'] == 3:
            text = """
            No puedes subir más.
            """

        else:
            self.state['sabatini_floor'] += 1
            text = """
            Subes una planta.

            Estás en la planta """ + str(self.state['sabatini_floor'])

            if self.state['sabatini_floor'] == 3:
                text += """

                Esta es la planta donde están los despachos de las
                asociaciones, puedes intentar ir al despacho.
                """

            self.state['time'] -= 10

        return text

    def must_flee(self, cmd):
        if cmd != 'huir':
            text = """
            Debiste huir cuando tuviste la ocasión. Te han pillado.
            """

            texture.tprint(text)

            return 'load game_over'

        self.flee()
        self.state['time'] -= 30

        text = """
        Has conseguido despistar al BEHTS.

        Estás en la esquina %s y te quedan %d minutos %d segundos""" % (
                self.state['sabatini_corner'],
                math.floor(self.state['time'] / 60),
                self.state['time'] % 60)

        self.state['sabatini_flee'] = False

        texture.tprint(text)

    @texture.printer
    def go_somewhere(self, direction):
        text = """
        Avanzas por el pasillo rezando por que te lleve al lugar que deseas,
        quizá tu memoria o el historial de la consola te esté jugando una mala
        pasada, pero para bien o para mal llegas a la esquina """

        if self.state['sabatini_corner'] == 'A-B':
            if direction == 'l':
                self.state['sabatini_corner'] = 'B-C'

            else:
                self.state['sabatini_corner'] = 'D-A'

        elif self.state['sabatini_corner'] == 'B-C':
            if direction == 'l':
                self.state['sabatini_corner'] = 'C-D'

            else:
                self.state['sabatini_corner'] = 'A-B'

        elif self.state['sabatini_corner'] == 'C-D':
            if direction == 'l':
                self.state['sabatini_corner'] = 'D-A'

            else:
                self.state['sabatini_corner'] = 'B-C'

        elif self.state['sabatini_corner'] == 'D-A':
            if direction == 'l':
                self.state['sabatini_corner'] = 'A-B'

            else:
                self.state['sabatini_corner'] = 'C-D'

        self.state['time'] -= 10

        return text + self.state['sabatini_corner']

    def flee(self):
        corners = ['A-B', 'B-C', 'C-D', 'D-A']

        corners.remove(self.state['sabatini_corner'])

        self.state['sabatini_corner'] = random.choice(corners)

    @texture.printer
    def random_encounter(self):
        perc = random.randrange(0, 100)

        text = """
        Al avanzar te topas con un miembro del BEHTS, te ha visto y va a ir
        a por ti. ¡Debes huir!
        """

        if perc >= 0 and perc < 40:
            # BEHTS
            self.state['sabatini_flee'] = True
            return text

        elif perc >= 40 and perc < 50:
            # No BETHS
            self.state['sabatini_flee'] = False

        elif perc >= 50 and perc < 90:
            # BEHTS
            self.state['sabatini_flee'] = True
            return text

        elif perc >= 90 and perc <= 100:
            # No BEHTS
            self.state['sabatini_flee'] = False
