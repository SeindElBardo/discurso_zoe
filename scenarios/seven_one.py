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
        Hay aulas numeradas de la 1 a la 7, un baño y una máquina de
        café en la que hay un muchacho.
        """

        return text

    def do_action(self, cmd):
        if cmd == 'ir al baño' or cmd == 'ir a baño' or cmd == 'baño':
            text = """
            ¡Oh, qué alivio!

            Vuelves al pasillo.
            """

            self.state['time'] -= 50

        elif cmd == 'ir a 1' or cmd == 'ir al 1' or cmd == 'ir 1':
            text = """
            Cruzas el pasillo y llegas al edificio 1.
            """

            texture.tprint(text)

            self.state['time'] -= 30
            self.state['one_zone'] = 'C'

            return 'load one_one'

        elif cmd == 'hablar':
            self.state['time'] -= 15
            self.random_quote()
            return

        elif cmd == 'bajar':
            text = """
            Bajas a la planta baja.
            """

            texture.tprint(text)

            self.state['time'] -= 10
            return 'load seven_zero'

        elif cmd.startswith('ir a aula') or cmd.startswith('ir al aula'):
            text = """
            Parece que todas las aulas están cerradas o hay gente dando clase.
            """
            self.state['time'] -= 10

        else:
            text = """
            Las aulas informáticas están abajo, aunque parece que el muchacho
            de la máquina de café tiene cosas interesantes que decir.
            """

        texture.tprint(text)

    @texture.printer
    def random_quote(self):
        quotes = [
            'Yo uso Xubuntu, que es la versión ligera de Ubuntu',
            'Vim es un editor de textos ligero',
            'Yo uso gedit',
            '¿Crees que puedo virtualizar cosas con un Pentium 2?',
            '¿Es eso un virtualizador por consola?',
            '¿A qué te refieres con "hablar"?',
            '¿En qué lenguaje está hecho supertuxkart?',
        ]

        text = """
        En cuanto te acercas al muchacho, empieza a hablarte:

        "%s"

        Decides alejarte.
        """ % random.choice(quotes)

        return text
