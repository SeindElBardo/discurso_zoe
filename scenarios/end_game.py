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

LOGO = """


   _              _                         _                         
  /_\   __      _(_)_ __  _ __   ___ _ __  (_)___   _   _  ___  _   _ 
 //_\\  \ \ /\ / / | '_ \| '_ \ / _ \ '__| | / __| | | | |/ _ \| | | |
/  _  \  \ V  V /| | | | | | | |  __/ |    | \__ \ | |_| | (_) | |_| |
\_/ \_/   \_/\_/ |_|_| |_|_| |_|\___|_|    |_|___/  \__, |\___/ \__,_|
                                                    |___/             


"""

class Scenario(texture.BaseScenario):

    @texture.printer
    def load(self):
        texture.tprint(LOGO, False)

        texture.tnewline()
        texture.tprint('Has completado tu misión!\n')

        if self.state['final'] == 'hacker':
            text = """
            Has llevado a cabo tu misión con éxito y con notables resultados.
            No sólo has ayudado a Zoe a dominar el campus, sino que además has
            sido fiel al software libre y has salvado la situación.

            ¡El GUL está orgulloso!
            """

        elif self.state['final'] == 'lame':
            text = """
            Has llevado a cabo tu misión con éxito y con notables resultados.
            Has ayudado a Zoe a dominar el campus y salvado la situación con
            tu imagen de Debian. Aunque igual podrías haber destruido la imagen
            de Windows ya que estabas...

            Esa decisión pesará sobre tu cabeza por el resto de tus días.
            """

        elif self.state['final'] == 'noob':
            text = """
            Has llevado a cabo tu misión con éxito y has ayudado a Zoe a
            dominar el campus. Sin embargo, has obligado al GUL a usar software
            no libre.

            Esa decisión pesará sobre tu cabeza por el resto de tus días.
            """

        return text

    @texture.printer
    def do_action(self, cmd):
        return 'Escribe "RESTART" para reiniciar el juego'
