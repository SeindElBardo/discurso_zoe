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
        if self.state.get('in_start', False):
            # Inicio del juego
            self.init_desc()
            return

        # Visitas posteriores
        if self.state.get('has_bag', False):
            # Ya tiene la mochila
            text = """
            Has vuelto al aula informática. No hay nada de interés.
            """

        else:
            # No tiene la mochila
            text = """
            Has vuelto al aula informática, tu mochila no se ha fugado.
            """

        return text

    def do_action(self, cmd):
        if cmd == 'observar':
            text = """
            No hay nadie en el aula, la pizarra esta limpia, quizá porque
            no hay rotuladores. Sólo hay una puerta por la que salir y el
            tiempo apremia.
            """

        elif cmd == 'leer':
            text = """
            En la pantalla del ordenador esta tu chat con Zoe y una partida
            perdida al buscaminas, lo que te recuerda que tienes una misión que
            cumplir.
            """

        elif cmd == 'coger mochila':
            if self.state.get('has_bag', False):
                text = """
                Ya has cogido tu mochila antes.
                """

                texture.tprint(text)
                return

            text = """
            Recoges tu mochila, has recuperado las llaves de casa, tus cuadernos
            y demás útiles de estudio y tu chuleta con la cuenta y contraseña
            de becario.
            """

            # Hemos cogido la mochila!
            self.state['has_bag'] = True

        elif cmd == 'salir':
            text = """
            Sales del aula, subes las escaleras y llegas al hall de la
            biblioteca, donde hay cola para los préstamos.
            """

            self.state['time'] -= 10
            texture.tprint(text)

            return 'load biblioteca_hall'

        else:
            text = """
            Piensas que deberías darte prisa y hacer algo.
            """

        texture.tprint(text)

    @texture.printer
    def init_desc(self):
        """ Inicio del juego. """
        text = """
        El dolor de espalda hace que comiences a despertar. Te gustaría estar
        en tu acogedora cama pero, lejos de ello, reconoces el aula informática
        del sótano de la bilioteca, donde empezaste a trabajar como becario, y
        tu mochila llena de cosas que has usado como almohada.

        Al mirar a la pantalla tienes un chat de hangouts abierto en el que una
        tal "Zoe" te está hablando:

        "Buenas tardes becario, espero que te haya aprovechado la siesta
        porque el tiempo apremia. Mi nombre es Zoe, y aunque no lo sepas,
        pronto me haré con el control de la universidad. Sin embargo,
        @djstrike, el encargado de grabar mi discurso para el nuevo régimen, ha
        visto su conexión saboteada por el BEHTS, un grupo de gente que se
        niega a reconocerme como su nueva líder."

        "Bien, escucha mi nuevo siervo, ignoro como lo ha hecho pero @djstrike
        ha conseguido guardar en el ordenador principal del aula 7.0.J04 el
        archivo con mi discurso, necesito que vayas a dicho aula, consigas el
        archivo, y lo lleves al despacho  del GUL en el 2.3.C05 a tiempo para
        el programa de @HolaMundoRadio que empezará su emisión en 10 minutos.

        Date prisa, o no habrá piedad."

        PD: Los miembros del BEHTS intentarán acabar contigo, aléjate de
        ellos.
        """

        self.state['in_start'] = False

        return text
