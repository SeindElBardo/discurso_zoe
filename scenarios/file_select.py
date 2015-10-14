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
        Examinas el pincho. Hay 3 archivos:

        - Matrix.mkv
        - liveDebian.iso
        - liveWindows7.iso

        Tienes que borrar uno a la fuerza. ¿Cuál será?
        """

        return text

    def do_action(self, cmd):
        if cmd == 'Matrix.mkv':
            self.state['usb_content'] = ['debian', 'windows', 'zoe']

            text = """
            Decides borrar la película de Matrix. Como friky que eres, te duele
            un poco cuando pulsas enter.

            ...

            El archivo ha terminado de copiarse, así que decides marcharte del
            aula.
            """

            texture.tprint(text)

            return 'load seven_zero'

        elif cmd == 'liveDebian.iso':
            self.state['usb_content'] = ['windows', 'matrix', 'zoe']

            text = """
            Decides borrar la distribución de Debian, porque es lo que menos
            ocupa y tampoco necesitas tanto espacio.

            ...

            El archivo ha terminado de copiarse, así que decides marcharte del
            aula.
            """

            texture.tprint(text)

            return 'load seven_zero'

        elif cmd == 'liveWindows7.iso':
            self.state['usb_content'] = ['debian', 'matrix', 'zoe']

            text = """
            Decides borrar la iso de Windows 7, a fin de cuentas... ¿quién la
            iba a necesitar?

            ...

            El archivo ha terminado de copiarse, así que decides marcharte del
            aula.
            """

            texture.tprint(text)

            return 'load seven_zero'

        text = """
        Parece que ese nombre de archivo no existe. Quizá te hayas equivocado
        al escribirlo por la tensión.
        """

        texture.tprint(text)
