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
        Entras en el aula. No hay nada del otro mundo, sólo están los
        ordenadores de los alumnos y el del profesor. Parece que alguien ha
        estado aquí hace poco.
        """

        return text

    def do_action(self, cmd):
        if cmd == 'salir':
            text = """
            Vuelves al pasillo.
            """

            texture.tprint(text)

            self.state['time'] -= 10
            return 'load seven_zero'

        elif (cmd == 'usar ordenador' or cmd == 'usar pc'
                and not self.state.get('usb_content', [])):
            self.use_pc()

        elif (cmd == 'buscar' or cmd == 'buscar pincho' or cmd == 'buscar usb'
                and self.state.get('can_search', False)):
            text = """
            Buscas en el aula y... ¡Oh! ¡Alguien se ha dejado un pincho de
            Peppa pig! Lo coges.
            """

            self.state['has_usb'] = True
            self.state['can_search'] = False
            self.state['time'] -= 5

            texture.tprint(text)

        elif (cmd == 'usar pincho' and self.state.get('has_usb', False)
                and not self.state.get('usb_content', [])):
            text = """
            Enchufas el pincho de Peppa pig en el ordenador.

            Parece que funciona, sin embargo cuando intentas copiar el archivo
            "DiscursoZoe.mp3" aparece en mensaje de error en el que dice que
            la memoria extraible "PeppaPincho" esta llena.
            """

            texture.tprint(text)
            return 'load file_select'

        else:
            text = """
            El tiempo apremia.
            """

            texture.tprint(text)

    @texture.printer
    def use_pc(self):
        if self.state.get('has_bag', False):
            # Mochila mochila
            text = """
            Enciendes el ordenador, usas tu chuleta para iniciar sesión
            y tras buscar un poco encuentras el archivo "DiscursoZoe.mp3",
            sin embargo te das cuenta de que no tienes un USB para
            guardarlo. Reza porque alguien se haya dejado el pincho.
            """

            self.state['can_search'] = True
            self.state['time'] -= 5

        else:
            text = """
            Enciendes el ordenador principal en el que supuestamente debes
            recoger el discurso de Zoe. En la pantalla aparece un cuadro
            de inicio de sesión.

            Como no te sabes tu contraseña la tienes apuntada en un papel
            que está en tu mochila... recuerdas que te has dejado la
            mochila en el aula informática de la bilioteca.

            "¡Mierda!"
            """

            self.state['time'] -= 20

        return text
