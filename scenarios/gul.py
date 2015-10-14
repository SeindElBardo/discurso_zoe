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

    def load(self):
        if self.state['time'] <= 0:
            # TARDE
            end_text = """
            No has llegado a tiempo para el programa de radio...
            """

            texture.tprint(end_text)
            return 'load game_over'

        text = """
        Abres la puerta un poco preocupado por la hora y te encuentras a 5
        personas. Dos de ellas, un chico y una chica, parecen buscar algo
        en los armarios y en cajas de cartón. Un segundo muchacho está
        terminando de colocar los cables de los micrófonos a una mesa de
        mezclas. Mientras, un tercer hombre sentado entre dos mesas y la pared,
        en una silla que ni siquiera va a poder separar de la mesa para poder
        salir, intenta relajar el tenso hambiente cantando y tocando con un
        ukelele "Over the Rainbow". Por último, una chica presidiendo la mesa,
        con unos cuantos folios de lo que parece el guión del programa, se gira
        hacia a ti y te pregunta:

        - ¿Eres el siervo que Zoe dijo que enviaría para traernos su discurso?

        Asientes sin mucha confianza. Ella mira la hora y suspira.

        - Has hecho un buen trabajo llegando a tiempo, sin embargo creo que no
        va a servir de nada. El BEHTS se ha llevado nuestro ordenador.

        - Estamos intentando usar uno viejo de los que hay por aqui -añade el
        que estaba configurando la mesa de mezclas-, pero no tienen el sistema
        operativo instalado.

        -¡Si es que ya os vale! -comenta la chica que buscaba en los armarios-,
        tenemos el despacho lleno de cosas que deberiamos tirar u organizar desde
        hace meses, pero los discos de instalación están todos en una única caja
        con un rótulo "CDs de instalación".

        - Pues porque no estabas aquí hace años -objeta el de las cajas-, dos
        viajes en coche al punto limpio que hicimos.

        - Oye novato -se suma dirigiendose a tí el quinto gulero que había
        terminado su interpretación-, ¿No tendrás por casualidad un CD o
        un pincho con un sistema operativo?
        """

        texture.tprint(text)

    def do_action(self, cmd):
        if cmd == 'no':
            text = """
            Me lo imaginaba. ¡Muy mal! ¡Siempre hay que ir con un cd de
            instalación en la mochila! A partir de ahora el que no lleve un cd
            de GNU/Linux encima, paga la cena.

            No se puede realizar el programa y el mensaje de Zoe no llega al
            resto del mundo.
            """

            texture.tprint(text)
            return 'load game_over'

        elif cmd == 'sí':
            if 'windows' not in self.state['usb_content']:
                text = """
                Te mirán asombrados mientras les entregas el pincho de
                Peppa pig que encontraste en el aula informática, argumentas
                que el pincho no es tuyo, que te lo encontraste. Parece que no
                te creen pero hoy no te van a juzgar.

                Preparan un ordenador y se disponen a intalar el SO desde tu
                PeppaPincho. En poco tiempo consiguen iniciar en Debian,
                se preparan para el programa de radio y cuando al ir a por el
                "DiscursoZoe.mp3" ven que en el pincho tienes la pélicula
                de "Matrix" en HD, te miran orgullosos y te felicitan por tu
                trabajo. Prefieres no recordar a nadie que el pincho no
                es tuyo.

                El programa de Radio se emite exitosamente y te hacen una
                mención para agradecer tus esfuerzos e invitarte a participar
                en futuras actividades del GUL.
                """

                self.state['final'] = 'hacker'

            elif 'matrix' not in self.state['usb_content']:
                text = """
                Te mirán asombrados mientras les entregas el pincho de
                Peppa pig que encontraste en el aula informática, argumentas
                que el pincho no es tuyo, que te lo encontraste. Parece que no
                te creen pero hoy no te van a juzgar.

                Preparan un ordenador y se disponen a intalar el SO desde
                tu PeppaPincho. En poco tiempo consiguen iniciar en Debian,
                se preparan para el programa de radio y cuando al ir a por el
                "DiscursoZoe.mp3" ven que en el pincho tienes una iso de
                Windows7, te miran con desaprobación. Les recuerdas que el
                pincho no es tuyo, pero siguen sin creerte.

                El programa de Radio se emite exitosamente y te agradecen que
                les trajeras el archivo.
                """

                self.state['final'] = 'lame'

            elif 'debian' not in self.state['usb_content']:
                text = """
                Te mirán asombrados mientras les entregas el pincho de
                Peppa pig que encontraste en el aula informática, argumentas
                que el pincho no es tuyo, que te lo encontraste. Parece que no
                te creen pero hoy no te van a juzgar.

                Preparan un ordenador y se disponen a intalar el SO desde
                tu PeppaPincho. Cuando ven el instalador de Windows se llevan
                las manos a la cabeza y preguntan a Zoe qué han hecho para tener
                tan mala suerte en este gran día.

                Al menos el programa de Radio se emite exitosamente. La chica
                que presidía la mesa tiene el detalle de agradecerte que hayas
                traído el discurso de Zoe y algo para arrancar el ordenador.
                También te pide que disculpes al resto de guleros, explicandote
                que aunque están agradecidos por tus esfuerzos, ahora mismo
                están demasiado furiosos con el BEHTS, que no sólo ha intentado
                sabotear el plan por todos los medios posibles, sino que además,
                junto con el ordenador y los discos, se han llevado el peluche
                de Tux más bonito que había en el despacho.
                """

                self.state['final'] = 'noob'

        else:
            text = """
            ¿Hola? ¿Tienes un sistema operativo sí o no?
            """

            texture.tprint(text)
            return

        texture.tprint(text)
        return 'load end_game'
