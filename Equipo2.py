

#Equipo 3 
#Proyecto 2 
#Clase IA 

import sys
from collections import deque
  
class subway(): 
      subway = {}
# Linea roja
   subway['el_rosario'] = ['aquiles_serdan', 'tezozomoc']
   subway['tezozomoc'] = ['el_rosario', 'azcapotzalco']
    subway['azcapotzalco'] = ['tezozomoc', 'ferreria']
    subway['ferreria'] = ['azcapotzalco', 'norte_45']
    subway['norte_45'] = ['ferreria', 'vallejo']
    subway['vallejo'] = ['norte_45', 'instituto_del_petroleo']
    subway['instituto_del_petroleo'] = ['politecnico', 'lindavista', 'autobuses_del_norte']
    subway['lindavista'] = ['instituto_del_petroleo', 'deportivo_18_de_marzo']
    subway['deportivo_18_de_marzo'] = ['lindavista', 'la_villa_basilica']
    subway['la_villa_basilica'] = ['deportivo_18_de_marzo', 'martin_carrera']
    subway['martin_carrera'] = ['la_villa_basilica', 'talisman']
# Linea Naranja
    subway['aquiles_serdan'] = ['el_rosario', 'camarones']
    subway['camarones'] = ['aquiles_serdan', 'refineria']
    subway['refineria'] = ['camarones', 'tacuba']
    subway['tacuba'] = ['refineria', 'san_joaquin', 'panteones', 'cuitlahuac']
    subway['san_joaquin'] = ['tacuba', 'polanco']
    subway['polanco'] = ['san_joaquin', 'auditorio']
    subway['auditorio'] = ['polanco', 'constituyentes']
    subway['constituyentes'] = ['auditorio', 'tacubaya']
    subway['tacubaya'] = ['constituyentes', 'san_pedro_de_los_pinos', 'observatorio', 'patriotismo', 'juanacatlan']
    subway['san_pedro_de_los_pinos'] = ['tacubaya', 'san_antonio']
    subway['san_antonio'] = ['san_pedro_de_los_pinos', 'mixcoac']
    subway['mixcoac'] = ['san_antonio', 'insurgentes_sur', 'barranca_del_muerto']
# Linea cafe
    subway['patriotismo'] = ['tacubaya', 'chilpancingo']
    subway['chilpancingo'] = ['patriotismo', 'centro_medico']
    subway['centro_medico'] = ['chilpancingo', 'lazaro_cardenas', 'hospital_general', 'etiopia']
    subway['lazaro_cardenas'] = ['centro_medico', 'chabacano']
    subway['chabacano'] = ['lazaro_cardenas', 'jamaica', 'san_antonio_abad', 'obrera', 'la_viga', 'viaducto']
    subway['jamaica'] = ['chabacano', 'mixiuhca', 'fray_servando', 'santa_anita']
    subway['mixiuhca'] = ['jamaica', 'velodromo']
    subway['velodromo'] = ['mixiuhca', 'ciudad_deportiva']
    subway['ciudad_deportiva'] = ['velodromo', 'puebla']
    subway['puebla'] = ['ciudad_deportiva', 'pantitlan']
    subway['pantitlan'] = ['puebla', 'zaragoza', 'hangares', 'agricola_oriental']
# Linea rosa
    subway['observatorio'] = ['tacubaya']
    subway['juanacatlan'] = ['tacubaya', 'chapultepec']
    subway['chapultepec'] = ['juanacatlan', 'sevilla']
    subway['sevilla'] = ['chapultepec', 'insurgentes']
    subway['insurgentes'] = ['sevilla', 'cuauhtemoc']
    subway['cuauhtemoc'] = ['insurgentes', 'balderas']
    subway['balderas'] = ['cuauhtemoc', 'salto_del_agua', 'juarez', 'ninos_heroes']
    subway['salto_del_agua'] = ['balderas', 'isabel_la_catolica', ' san_juan_de_letran', 'doctores']
    subway['isabel_la_catolica'] = ['salto_del_agua', 'pino_suarez']
    subway['pino_suarez'] = ['isabel_la_catolica', 'merced', 'zocalo', 'san_antonio_abad']
    subway['merced'] = ['pino_suarez', 'candelaria']
    subway['candelaria'] = ['merced', 'san_lazaro', 'morelos', 'fray_servando']
    subway['san_lazaro'] = ['candelaria', 'moctezuma', 'morelos', 'flores_magon']
    subway['moctezuma'] = ['san_lazaro', 'balbuena']
    subway['balbuena'] = ['moctezuma', 'boulevard_puerto_aereo']
    subway['boulevard_puerto_aereo'] = ['balbuena', 'gomez_farias']
    subway['gomez_farias'] = ['boulevard_puerto_aereo', 'zaragoza']
    subway['zaragoza'] = ['gomez_farias', 'pantitlan']
# Linea azul
    subway['cuatro_caminos'] = ['panteones']
    subway['panteones'] = ['cuatro_caminos', 'tacuba']
    subway['cuitlahuac'] = ['tacuba', 'popotla']
    subway['popotla'] = ['cuitlahuac', 'colegio_militar']
    subway['colegio_militar'] = ['popotla', 'normal']
    subway['normal'] = ['colegio_militar', 'san_cosme']
    subway['san_cosme'] = ['normal', 'revolucion']
    subway['revolucion'] = ['san_cosme', 'hidalgo']
    subway['hidalgo'] = ['revolucion', 'bellas_artes', 'guerrero', 'juarez']
    subway['bellas_artes'] = ['hidalgo', 'allende', 'garibaldi', 'san_juan_de_letran']
    subway['allende'] = ['bellas_artes', 'zocalo']
    subway['zocalo'] = ['allende', 'pino_suarez']
    subway['san_antonio_abad'] = ['pino_suarez', 'chabacano']
    subway['viaducto'] = ['chabacano', 'xola']
    subway['xola'] = ['viaducto', 'villa_de_cortes']
    subway['villa_de_cortes'] = ['xola', 'nativitas']
    subway['nativitas'] = ['villa_de_cortes', 'portales']
    subway['portales'] = ['nativitas', 'ermita']
    subway['ermita'] = ['portales', 'general_anaya', 'eje_central', 'mexicaltzingo']
    subway['general_anaya'] = ['ermita', 'tasquena']
    subway['tasquena'] = ['general_anaya']

# Linea verde-gris
    subway['buenavista'] = ['guerrero']
    subway['guerrero'] = ['buenavista', 'garibaldi', 'tlatelolco', 'hidalgo']
    subway['garibaldi'] = ['guerrero', 'lagunilla', 'bellas_artes']
    subway['lagunilla'] = ['garibaldi', 'tepito']
    subway['tepito'] = ['lagunilla', 'morelos']
    subway['morelos'] = ['tepito', 'san_lazaro', 'canal_del_norte', 'candelaria']
    subway['flores_magon'] = ['san_lazaro', 'romero_rubio']
    subway['romero_rubio'] = ['flores_magon', 'ocenania']
    subway['oceania'] = ['romero_rubio', 'deportivo_oceania', 'aragon', 'terminal_aerea']
    subway['deportivo_oceania'] = ['oceania', 'bosque_de_aragon']
    subway['bosque_de_aragon'] = ['deportivo_oceania', 'villa_de_aragon']
    subway['villa_de_aragon'] = ['bosque_de_aragon', 'nezahualcoyotl']
    subway['nezahualcoyotl'] = ['villa_de_aragon', 'impulsora']
    subway['impulsora'] = ['nezahualcoyotl', 'rio_de_los_remedios']
    subway['rio_de_los_remedios'] = ['impulsora', 'muzquiz']
    subway['muzquiz'] = ['rio_de_los_remedios', 'ecatepec']
    subway['ecatepec'] = ['muzquiz', 'olimpica']
    subway['olimpica'] = ['ecatepec', 'plaza_aragon']
    subway['plaza_aragon'] = ['olimpica', 'ciudad_azteca']
    subway['ciudad_azteca'] = ['plaza_aragon']

# Linea amarilla
    subway['politecnico'] = ['instituto_del_petroleo']
    subway['autobuses_del_norte'] = ['instituto_del_petroleo', 'la_raza']
    subway['la_raza'] = ['autobuses_del_norte', 'misterios', 'potrero', 'tlatelolco']
    subway['misterios'] = ['la_raza', 'valle_gomez']
    subway['valle_gomez'] = ['misterios', 'consulado']
    subway['consulado'] = ['valle_gomez', 'eduardo_molina', 'bondojito', 'canal_del_norte']
    subway['eduardo_molina'] = ['consulado', 'aragon']
    subway['aragon'] = ['eduardo_molina', 'oceania']
    subway['terminal_area']  = ['oceania', 'hangares']
    subway['hangares'] = ['terminal_area', 'pantitlan']

# Linea CU
    subway['indios_verdes'] = ['deportivo_18_de_marzo']
    subway['potrero'] = ['deportivo_18_de_marzo', 'la_raza']
    subway['tlatelolco'] = ['la_raza', 'guerrero']
    subway['juarez'] = ['hidalgo', 'balderas']
    subway['ninos_heroes'] = ['balderas', 'hospital_general']
    subway['hospital_general'] = ['ninos_heroes', 'centro_medico']
    subway['etiopia'] = ['centro_medico', 'eugenia']
    subway['eugenia'] = ['etiopia', 'division_del_norte']
    subway['division_del_norte'] = ['eugenia', 'zapata']
    subway['zapata'] = ['division_del_norte', 'coyoacan']
    subway['coyoacan'] = ['zapata', 'viveros']
    subway['viveros'] = ['coyoacan', 'miguel_angel_de_quevedo']
    subway['miguel_angel_de_quevedo'] = ['viveros', 'copilco']
    subway['copilco'] = ['miguel_angel_de_quevedo', 'universidad']
    subway['universidad'] = ['copilco']

# Linea verdecita
    subway['talisman'] = ['martin_carrera', 'bondojito']
    subway['bondojito'] = ['talisman', 'consulado']
    subway['canal_del_norte'] = ['consulado', 'morelos']
    subway['fray_servando'] = ['candelaria', 'jamaica']
    subway['santa_anita'] = ['jamaica']

# Linea dorada
    subway['insurgentes_sur'] = ['mixcoac', 'hospital_20_de_noviembre']
    subway['hospital_20_de_noviembre'] = ['insurgentes_sur', 'zapata']
    subway['parque_de_los_venados'] = ['zapata', 'eje_central']
    subway['eje_central'] = ['parque_de_los_venados', 'ermita']
    subway['mexicaltzingo'] = ['ermita', 'atlalilco']
    subway['atlalilco'] = ['mexicaltzingo', 'culhuacan', 'escuadron_201', 'iztapalapa']
    subway['culhuacan'] = ['atlalilco', 'san_andres_tomatlan']
    subway['san_andres_tomatlan'] = ['culhuacan', 'lomas_estrella']
    subway['lomas_estrella'] = ['san_andres_tomatlan', 'calle_11']
    subway['calle_11'] = ['lomas_estrella', 'periferico_oriente']
    subway['periferico_oriente'] = ['calle_11', 'tezonco']
    subway['tezonco'] = ['periferico_oriente', 'olivos']
    subway['olivos'] = ['tezonco', 'nopalera']
    subway['nopalera'] = ['olivos', 'zapotitlan']
    subway['zapotitlan'] = ['nopalera', 'tlaltenco']
    subway['tlaltenco'] = ['zapotitlan', 'tlahuac']
    subway['tlahuac'] = ['tlaltenco']

# Linea verde
    subway['doctores'] = ['salto_del_agua', 'obrera']
    subway['obrera'] = ['doctores', 'chabacano']
    subway['la_viga'] = ['chabacano', 'santa_anita']
    subway['coyuya'] = ['santa_anita', 'iztacalco']
    subway['iztacalco'] = ['coyuya', 'apatlaco']
    subway['apatlaco'] = ['iztacalco', 'aculco']
    subway['aculco'] = ['apatlaco', 'escuadron_201']
    subway['escuadron_201'] = ['aculco', 'atlalilco']
    subway['iztapalapa'] = ['atlalilco', 'cerro_de_la_estrella']
    subway['cerro_de_la_estrella'] = ['iztapalapa', 'uam']
    subway['uam'] = ['cerro_de_la_estrella', 'constitucion_de_1917']
    subway['constitucion_de_1917'] = ['uam']

# Linea fiusha
    subway['agricola_oriental'] = ['pantitlan', 'canal_de_san_juan']
    subway['canal_de_san_juan'] = ['agricola_oriental', 'tepalcates']
    subway['tepalcates'] = ['canal_de_san_juan', 'guelatao']
    subway['guelatao'] = ['tepalcates', 'penon_viejo']
    subway['penon_viejo'] = ['guelatao', 'acatitla']
    subway['acatitla'] = ['penon_viejo', 'santa_marta']
    subway['santa_marta'] = ['acatitla', 'los_reyes'] 
    subway['los_reyes'] = ['santa_marta', 'la_paz']
    subway['la_paz'] = ['los_reyes']
  
  def bfs(origin, destination, subway_graph):
    search_queue = deque()
    search_queue.append(origin)

    seen_station = [origin]

    parent = {}
    parent[origin] = None

    while search_queue:
        current_station = search_queue.popleft()
        if current_station == destination:
            return True, parent

        if current_station in subway_graph:
            for v in subway_graph[current_station]:
                if v not in seen_station:
                    seen_station.append(v)
                    search_queue.append(v)
                    parent[v] = current_station

    return False, None

if __name__ == '__main__':

    subway = subway()
    
    origin=str(input('Dime desde qué estación inicias: \t '))
    destination=str(input('Dime a qué estación vas:\t '))
    rc, parents = bfs(origin, destination, subway)
    if rc:
        print ('Follow this route:')

        route = []
        current = destination
        while current is not None:
            route.append(current)
            current = parents[current]

        route.reverse()
        print (route)
    else:
        print ('Did not find route')