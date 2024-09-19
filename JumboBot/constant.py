from dataclasses import dataclass

@dataclass
class Product:
    CATEGORY: str
    SUBCATEGORY: str
    SUBSUBCATEGORY: str

class Electro:
    AIRE_ACONDICIONADO_Y_VENTILACION: list[Product] = [
        Product("electro", "aire_acondicionado_y_ventilacion", "aire_acondicionado"),
        Product("electro", "aire_acondicionado_y_ventilacion", "ventilacion"),
    ]
    AUDIO: list[Product] = [
        Product("electro", "audio", ""),
    ]
    CALEFACCION_CALEFONES_Y_TERMOTANQUES: list[Product] = [
        Product("electro", "calefaccion_calefones_y_termotanques", "calefaccion"),
        Product("electro", "calefaccion_calefones_y_termotanques", "calefones"),
        Product("electro", "calefaccion_calefones_y_termotanques", "termotanques"),
    ]
    COCINAS_Y_HORNOS: list[Product] = [
        Product("electro", "cocinas_y_hornos", "anafes"),
        Product("electro", "cocinas_y_hornos", "cocinas"),
        Product("electro", "cocinas_y_hornos", "hornos"),
        Product("electro", "cocinas_y_hornos", "microondas"),
        Product("electro", "cocinas_y_hornos", "purificadores"),
    ]
    CONSOLAS_Y_VIDEOJUEGOS: list[Product] = [
        Product("electro", "consolas_y_videojuegos", "consolas"),
        Product("electro", "consolas_y_videojuegos", "videojuegos"),
    ]
    HELADERAS_FREEZERS_Y_CAVAS: list[Product] = [
        Product("electro", "heladeras_freezers_y_cavas", "heladera_no_frost"),
        Product("electro", "heladeras_freezers_y_cavas", "heladera_ciclica"),
        Product("electro", "heladeras_freezers_y_cavas", "freezers"),
        Product("electro", "heladeras_freezers_y_cavas", "heladeras_cavas"),
    ]
    INFORMATICA: list[Product] = [
        Product("electro", "informatica", ""),
    ]
    LAVADO: list[Product] = [
        Product("electro", "lavado", "lavarropas"),
        Product("electro", "lavado", "secarropas"),
        Product("electro", "lavado", "lavavajillas"),
    ]
    PEQUEÑOS_ELECTROS: list[Product] = [
        Product("electro", "pequeños_electros", "procesadoras"),
        Product("electro", "pequeños_electros", "licuadoras"),
        Product("electro", "pequeños_electros", "aspiradoras"),
        Product("electro", "pequeños_electros", "batidoras"),
        Product("electro", "pequeños_electros", "cuidado_personal"),
        Product("electro", "pequeños_electros", "pequeños_electros_de_cocina"),
        Product("electro", "pequeños_electros", "pequeños_electros_de_hogar"),
        Product("electro", "pequeños_electros", "salud"),
        Product("electro", "pequeños_electros", "cafeteras_y_molinillos"),
    ]
    TELEFONOS: list[Product] = [
        Product("electro", "telefonos", ""),
    ]
    TV_Y_VIDEO: list[Product] = [
        Product("electro", "tv_y_video", ""),
    ]

    EVERYTHING = [AIRE_ACONDICIONADO_Y_VENTILACION, AUDIO, CALEFACCION_CALEFONES_Y_TERMOTANQUES, COCINAS_Y_HORNOS, CONSOLAS_Y_VIDEOJUEGOS, HELADERAS_FREEZERS_Y_CAVAS, INFORMATICA, LAVADO, PEQUEÑOS_ELECTROS, TELEFONOS, TV_Y_VIDEO]

class Hogar:
    AUTOMOTOR: list[Product] = [
        Product("hogar_y_textil", "automotor", ""),
    ]
    BAÑO: list[Product] = [
        Product("hogar_y_textil", "baño", ""),
    ]
    COCINA: list[Product] = [
        Product("hogar_y_textil", "cocina", ""),
    ]
    COLCHONES_Y_ALMOHADAS: list[Product] = [
        Product("hogar_y_textil", "colchones_y_almohadas", ""),
    ]
    DECORACION: list[Product] = [
        Product("hogar_y_textil", "decoracion", ""),
    ]
    COTILLON: list[Product] = [
        Product("hogar_y_textil", "cotillon", ""),
    ]
    FERRETERIA: list[Product] = [
        Product("hogar_y_textil", "ferreteria", ""),
    ]
    INDUMENTARIA: list[Product] = [
        Product("hogar_y_textil", "indumentaria", ""),
    ]
    MESA: list[Product] = [
        Product("hogar_y_textil", "mesa", ""),
    ]
    MUEBLES: list[Product] = [
        Product("hogar_y_textil", "muebles", ""),
    ]
    ORGANIZACION: list[Product] = [
        Product("hogar_y_textil", "organizacion", ""),
    ]
    ROPA_DE_CAMA: list[Product] = [
        Product("hogar_y_textil", "ropa_de_cama", ""),
    ]
    EVERYTHING = [
        AUTOMOTOR,
        BAÑO,
        COCINA,
        COLCHONES_Y_ALMOHADAS,
        DECORACION,
        COTILLON,
        INDUMENTARIA,
        FERRETERIA,
        MESA,
        MUEBLES,
        ORGANIZACION,
        ROPA_DE_CAMA,
    ]

class TiempoLibre:
    AIRE_LIBRE: list[Product] = [
        Product("tiempo_libre", "aire_libre", "")
    ]
    AUTOMOTOR: list[Product] = [
        Product("tiempo_libre", "automotor", "accesorios_para_auto"),
        Product("tiempo_libre", "automotor", "cubiertas"),
        Product("tiempo_libre", "automotor", "limpieza"),
        Product("tiempo_libre", "automotor", "lubricantes_y_refrigerantes"),
        Product("tiempo_libre", "automotor", "repuestos")
    ]
    SUPLEMENTOS: list[Product] = [
        Product("tiempo_libre", "suplementos", "")
    ]
    PARAGUAS: list[Product] = [
        Product("tiempo_libre", "paraguas", "")
    ]
    JUEGUETERIA: list[Product] = [
        Product("tiempo_libre", "juguetería", "ensambles_y_rompecabezas"),
        Product("tiempo_libre", "juguetería", "juegos_de_mesa"),
        Product("tiempo_libre", "juguetería", "juguetes_de_playa_y_agua"),
        Product("tiempo_libre", "juguetería", "juguetes_para_bebes"),
        Product("tiempo_libre", "juguetería", "juguetes"),
        Product("tiempo_libre", "juguetería", "muñecas_y_muñecos"),
        Product("tiempo_libre", "juguetería", "peluches"),
        Product("tiempo_libre", "juguetería", "disfraces"),
        Product("tiempo_libre", "juguetería", "vehículos_y_pistas")
    ]
    VALIJAS_BOLSOS_Y_MOCHILAS: list[Product] = [
        Product("tiempo_libre", "valijas_bolsos_mochilas_y_luncheras", "")
    ]
    LIBRERIA: list[Product] = [
        Product("tiempo_libre", "librería", "")
    ]
    LIBROS: list[Product] = [
        Product("tiempo_libre", "libros", "")
    ]

    EVERYTHING = [
        AIRE_LIBRE,
        AUTOMOTOR,
        SUPLEMENTOS,
        PARAGUAS,
        JUEGUETERIA,
        VALIJAS_BOLSOS_Y_MOCHILAS,
        LIBRERIA,
        LIBROS
    ]

class BebesNiños:
    ALIMENTACION: list[Product] = [
        Product("bebes_y_niños", "alimentación", "")
    ]
    BAÑADERAS_CAMBIADORES_Y_PELELAS: list[Product] = [
        Product("bebes_y_niños", "bañaderas_cambiadores_y_pelelas", "")
    ]
    CUIDADO_DEL_BEBE: list[Product] = [
        Product("bebes_y_niños", "cuidado_del_bebe", "")
    ]
    INDUMENTARIA: list[Product] = [
        Product("bebes_y_niños", "indumentaria", "")
    ]
    JUGUETERIA: list[Product] = [
        Product("bebes_y_niños", "jugueteria", "")
    ]
    MAMADERAS_CHUPETES_Y_BABEROS: list[Product] = [
        Product("bebes_y_niños", "mamaderas_chupetes_y_baberos", "")
    ]
    PAÑALES: list[Product] = [
        Product("bebes_y_niños", "pañales", "")
    ]
    ROPA_DE_CAMA_Y_BAÑO: list[Product] = [
        Product("bebes_y_niños", "ropa_de_cama_y_baño", "")
    ]
    SEGURIDAD: list[Product] = [
        Product("bebes_y_niños", "seguridad", "")
    ]

    EVERYTHING = [
        ALIMENTACION,
        BAÑADERAS_CAMBIADORES_Y_PELELAS,
        CUIDADO_DEL_BEBE,
        INDUMENTARIA,
        JUGUETERIA,
        MAMADERAS_CHUPETES_Y_BABEROS,
        PAÑALES,
        ROPA_DE_CAMA_Y_BAÑO,
        SEGURIDAD
    ]

class Almacen:
    ACEITES_Y_VINAGRES: list[Product] = [
        Product("almacen", "aceites_y_vinagres", "aceites_comunes"),
        Product("almacen", "aceites_y_vinagres", "aceites_especiales"),
        Product("almacen", "aceites_y_vinagres", "acetos"),
        Product("almacen", "aceites_y_vinagres", "jugos_de_limon"),
        Product("almacen", "aceites_y_vinagres", "vinagres")
    ]
    ADEREZOS: list[Product] = [
        Product("almacen", "aderezos", "mayonesas"),
        Product("almacen", "aderezos", "ketchup"),
        Product("almacen", "aderezos", "mostazas"),
        Product("almacen", "aderezos", "salsas_golf"),
        Product("almacen", "aderezos", "salsas_frias"),
        Product("almacen", "aderezos", "otros_condimentos")
    ]
    ARROZ_Y_LEGUMBRES: list[Product] = [
        Product("almacen", "arroz_y_legumbres", "arroz"),
        Product("almacen", "arroz_y_legumbres", "arroz_listos"),
        Product("almacen", "arroz_y_legumbres", "legumbres")
    ]
    SAL_PIMIENTA_Y_ESPECIAS: list[Product] = [
        Product("almacen", "sal_pimienta_y_especias", "sal"),
        Product("almacen", "sal_pimienta_y_especias", "especias")
    ]
    CONSERVAS: list[Product] = [
        Product("almacen", "conservas", "conservas_de_carne"),
        Product("almacen", "conservas", "conservas_de_frutas"),
        Product("almacen", "conservas", "conservas_de_pescado"),
        Product("almacen", "conservas", "conservas_de_verduras_y_legumbres")
    ]
    DESAYUNO_Y_MERIENDA: list[Product] = [
        Product("almacen", "desayuno_y_merienda", "azucar_y_edulcorantes"),
        Product("almacen", "desayuno_y_merienda", "bizcochuelos_budines_y_magdalenas"),
        Product("almacen", "desayuno_y_merienda", "cacao_y_saborizantes"),
        Product("almacen", "desayuno_y_merienda", "cafes"),
        Product("almacen", "desayuno_y_merienda", "cereales"),
        Product("almacen", "desayuno_y_merienda", "galletitas_dulces"),
        Product("almacen", "desayuno_y_merienda", "galletitas_saladas"),
        Product("almacen", "desayuno_y_merienda", "leches"),
        Product("almacen", "desayuno_y_merienda", "mermeladas_y_jaleas"),
        Product("almacen", "desayuno_y_merienda", "piononos"),
        Product("almacen", "desayuno_y_merienda", "tes"),
        Product("almacen", "desayuno_y_merienda", "yerbas")
    ]
    GOLOSINAS_Y_CHOCOLATES: list[Product] = [
        Product("almacen", "golosinas_y_chocolates", "alfajores"),
        Product("almacen", "golosinas_y_chocolates", "bocaditos_y_postres"),
        Product("almacen", "golosinas_y_chocolates", "bombones"),
        Product("almacen", "golosinas_y_chocolates", "caramelos_y_chicles"),
        Product("almacen", "golosinas_y_chocolates", "chocolates"),
        Product("almacen", "golosinas_y_chocolates", "turrones_y_grageas")
    ]
    HARINAS: list[Product] = [
        Product("almacen", "harinas", "harinas"),
        Product("almacen", "harinas", "avenas_y_semolas")
    ]
    LIBRE_DE_GLUTEN = [
        Product("almacen", "libre_de_gluten", "bizcochuelos_brownies_y_tortas"),
        Product("almacen", "libre_de_gluten", "galletitas_saladas")
    ]
    PANIFICADOS: list[Product] = [
        Product("almacen", "panificados", "lacteados"),
        Product("almacen", "panificados", "pan_para_hamburguesas_y_panchos"),
        Product("almacen", "panificados", "tostadas_y_grisines"),
        Product("almacen", "panificados", "pan_rallado_y_rebozador"),
        Product("almacen", "panificados", "integral_y_salvado")
    ]
    CALDOS_SOPAS_PURE_Y_BOLSAS_PARA_HORNO: list[Product] = [
        Product("almacen", "caldos_sopas_pure_y_bolsas_para_horno", "pure"),
        Product("almacen", "caldos_sopas_pure_y_bolsas_para_horno", "sopas"),
        Product("almacen", "caldos_sopas_pure_y_bolsas_para_horno", "caldos")
    ]
    PARA_PREPARAR: list[Product] = [
        Product("almacen", "para_preparar", "bizcochuelos_brownies_y_tortas"),
        Product("almacen", "para_preparar", "comidas"),
        Product("almacen", "para_preparar", "flanes"),
        Product("almacen", "para_preparar", "gelatinas"),
        Product("almacen", "para_preparar", "helados"),
        Product("almacen", "para_preparar", "mousse"),
        Product("almacen", "para_preparar", "pasteleria"),
        Product("almacen", "para_preparar", "postres")
    ]
    PASTAS_SECAS_Y_SALSAS: list[Product] = [
        Product("almacen", "pastas_secas_y_salsas", "pastas_secas_guiseras"),
        Product("almacen", "pastas_secas_y_salsas", "pastas_secas_largas"),
        Product("almacen", "pastas_secas_y_salsas", "pastas_listas"),
        Product("almacen", "pastas_secas_y_salsas", "salsas")
    ]
    SNACKS: list[Product] = [
        Product("almacen", "snacks", "frutas_secas_y_disecadas"),
        Product("almacen", "snacks", "mani"),
        Product("almacen", "snacks", "nachos"),
        Product("almacen", "snacks", "palitos_de_maiz"),
        Product("almacen", "snacks", "palitos_salados"),
        Product("almacen", "snacks", "papas_fritas"),
        Product("almacen", "snacks", "pochoclos"),
        Product("almacen", "snacks", "snacks")
    ]

    EVERYTHING = [ACEITES_Y_VINAGRES, ADEREZOS, ARROZ_Y_LEGUMBRES, CALDOS_SOPAS_PURE_Y_BOLSAS_PARA_HORNO, CONSERVAS, DESAYUNO_Y_MERIENDA, GOLOSINAS_Y_CHOCOLATES, HARINAS, LIBRE_DE_GLUTEN, PANIFICADOS, PARA_PREPARAR, PASTAS_SECAS_Y_SALSAS, SAL_PIMIENTA_Y_ESPECIAS, SNACKS]

class Bebidas:
    A_BASE_DE_HIERBAS: list[Product] = [
        Product("bebidas", "a_base_de_hierbas", ""),
    ]
    AGUAS: list[Product] = [
        Product("bebidas", "aguas", "aguas_sin_gas"),
        Product("bebidas", "aguas", "aguas_con_gas"),
        Product("bebidas", "aguas", "aguas_saborizadas")
    ]
    APERITIVOS: list[Product] = [
        Product("bebidas", "aperitivos", "")
    ]
    BEBIDAS_BLANCAS: list[Product] = [
        Product("bebidas", "bebidas_blancas", "")
    ]
    CERVEZAS: list[Product] = [
        Product("bebidas", "cervezas", "")
    ]
    CHAMPAGNES: list[Product] = [
        Product("bebidas", "champagnes", "")
    ]
    ENERGIZANTES: list[Product] = [
        Product("bebidas", "energizantes", "")
    ]
    GASEOSAS: list[Product] = [
        Product("bebidas", "gaseosas", "cola"),
        Product("bebidas", "gaseosas", "lima_limon"),
        Product("bebidas", "gaseosas", "naranja"),
        Product("bebidas", "gaseosas", "pomelo"),
        Product("bebidas", "gaseosas", "tonica"),
        Product("bebidas", "gaseosas", "guarana")
    ]
    GENEROSOS: list[Product] = [
        Product("bebidas", "generosos", "")
    ]
    HIELO: list[Product] = [
        Product("bebidas", "hielo", "")
    ]
    ISOTONICAS: list[Product] = [
        Product("bebidas", "isotonicas", "")
    ]
    JUGOS: list[Product] = [
        Product("bebidas", "jugos", "en_polvo"),
        Product("bebidas", "jugos", "listos"),
        Product("bebidas", "jugos", "granadina"),
        Product("bebidas", "jugos", "frescos")
    ]
    LICORES: list[Product] = [
        Product("bebidas", "licores", "")
    ]
    SIDRAS: list[Product] = [
        Product("bebidas", "sidras", "")
    ]
    VINOS: list[Product] = [
        Product("bebidas", "vinos", "vinos_blancos"),
        Product("bebidas", "vinos", "vinos-tintos"),
        Product("bebidas", "vinos", "vinos_rosados"),
        Product("bebidas", "vinos", "vinos_frizantes")
    ]
    WHISKYS: list[Product] = [
        Product("bebidas", "whiskys", "")
    ]
    
    EVERYTHING = [A_BASE_DE_HIERBAS, AGUAS, APERITIVOS, BEBIDAS_BLANCAS, CERVEZAS, CHAMPAGNES, ENERGIZANTES, GASEOSAS, GENEROSOS, HIELO, ISOTONICAS, JUGOS, LICORES, SIDRAS, VINOS, WHISKYS]

class FrutasYVerduras:
    FRUTAS: list[Product] = [
        Product("frutas_y_verduras", "frutas", "frutas_empaquetadas"),
        Product("frutas_y_verduras", "frutas", "frutas_secas_y_desecadas"),
        Product("frutas_y_verduras", "frutas", "frutas_sueltas"),
        Product("frutas_y_verduras", "frutas", "frutas_congeladas"),
        Product("frutas_y_verduras", "frutas", "huevos")
    ]

    HIERBAS_AROMATICAS_Y_PLANTINES: list[Product] = [
    Product("frutas_y_verduras", "hierbas_aromaticas_y_plantines", "")
    ]

    HUEVOS: list[Product] = [
    Product("frutas_y_verduras", "huevos", "")
    ]

    LEGUMBRES_GRANOS_Y_SEMILLAS: list[Product] = [
    Product("frutas_y_verduras", "legumbres_granos_y_semillas", "")
    ]

    ORGANICOS: list[Product] = [
    Product("frutas_y_verduras", "orgánicos", "")
    ]

    VERDURAS: list[Product] = [
        Product("frutas_y_verduras", "verduras", "hierbas_aromaticas_y_plantines"),
        Product("frutas_y_verduras", "verduras", "hortalizas_livianas"),
        Product("frutas_y_verduras", "verduras", "hortalizas_pesadas"),
        Product("frutas_y_verduras", "verduras", "legumbres_granos_y_semillas"),
        Product("frutas_y_verduras", "verduras", "organicos"),
        Product("frutas_y_verduras", "verduras", "verduras_empaquetadas"),
        Product("frutas_y_verduras", "verduras", "verduras_frescas_de_hoja"),
        Product("frutas_y_verduras", "verduras", "verduras_procesadas_y_ensaladas_listas"),
        Product("frutas_y_verduras", "verduras", "verduras_secas_y_desecadas")
    ]

    EVERYTHING = [
        FRUTAS,
        HIERBAS_AROMATICAS_Y_PLANTINES,
        HUEVOS,
        LEGUMBRES_GRANOS_Y_SEMILLAS,
        ORGANICOS,
        VERDURAS
    ]

class Carnes:
    CARNE_VACUNA: list[Product] = [
        Product("carnes", "carne_vacuna", "")
    ]
    EMBUTIDOS: list[Product] = [
        Product("carnes", "embutidos", "chorizos"),
        Product("carnes", "embutidos", "morcilla"),
        Product("carnes", "embutidos", "salchichas")
    ]
    POLLOS: list[Product] = [
        Product("carnes", "pollos", "")
    ]
    MENUDENCIAS: list[Product] = [
        Product("carnes", "menudencias", "")
    ]
    CARNE_DE_CERDO: list[Product] = [
        Product("carnes", "carne_de_cerdo", "")
    ]
    CORDERO_LECHON_CHIVITO_CONEJO: list[Product] = [
        Product("carnes", "cordero_lechón_chivito_y_conejo", "")
    ]
    CARBON_Y_LEÑA: list[Product] = [
        Product("carnes", "carbon_y_leña", "")
    ]
    LISTOS_PARA_COCINAR: list[Product] = [
        Product("carnes", "listos_para_cocinar", "")
    ]


    EVERYTHING = [
        CARNE_VACUNA,
        EMBUTIDOS,
        POLLOS,
        MENUDENCIAS,
        CARNE_DE_CERDO,
        CORDERO_LECHON_CHIVITO_CONEJO,
        CARBON_Y_LEÑA,
        LISTOS_PARA_COCINAR
    ]

class PescadosMariscos:
    PESCADOS: list[Product] = [
            Product("pescados_y_mariscos", "pescados", "")
    ]
    MARISCOS: list[Product] = [
            Product("pescados_y_mariscos", "mariscos", "")
    ]

    EVERYTHING = [
        PESCADOS,
        MARISCOS
    ]

class QuesosYFiambres:
    QUESOS: list[Product] = [
        Product("quesos_y_fiambres", "quesos", "quesos_untables"),
        Product("quesos_y_fiambres", "quesos", "queso_muzzarella"),
        Product("quesos_y_fiambres", "quesos", "quesos_port_salut_y_cremosos"),
        Product("quesos_y_fiambres", "quesos", "quesos_semiblandos"),
        Product("quesos_y_fiambres", "quesos", "quesos_duros"),
        Product("quesos_y_fiambres", "quesos", "quesos_especiales_e_importados"),
        Product("quesos_y_fiambres", "quesos", "quesos_rallados"),
        Product("quesos_y_fiambres", "quesos", "ricota")
    ]
    FIAMBRES: list[Product] = [
        Product("quesos_y_fiambres", "fiambres", "jamon_cocido_y_crudo"),
        Product("quesos_y_fiambres", "fiambres", "fiambres")
    ]
    DULCES: list[Product] = [
        Product("quesos_y_fiambres", "dulces", "")
    ]
    ENCURTIDOS_ACEITUNAS_Y_PICKLES: list[Product] = [
        Product("quesos_y_fiambres", "encurtidos_aceitunas_y_pickles", "")
    ]
    SALCHICAS: list[Product] = [
        Product("quesos_y_fiambres", "salchichas", "")
    ]

    EVERYTHING = [
        QUESOS,
        FIAMBRES,
        DULCES,
        ENCURTIDOS_ACEITUNAS_Y_PICKLES,
        SALCHICAS
    ]

class Lacteos:
    ALIMENTOS_VEGETALES: list[Product] = [
        Product("lacteos", "alimentos-vegetales", ""),
    ]
    CREMAS: list[Product] = [
        Product("lacteos", "cremas", ""),
    ]
    DULCE_DE_LECHE: list[Product] = [
        Product("lacteos", "dulce_de_leche", ""),
    ]
    LECHES: list[Product] = [
        Product("lacteos", "leches", "leches_larga_vida"),
        Product("lacteos", "leches", "leches_refrigeradas"),
        Product("lacteos", "leches", "leches_saborizadas"),
        Product("lacteos", "leches", "bebidas_vegetales"),
    ]
    MANTECAS_Y_MARGARINAS: list[Product] = [
        Product("lacteos", "mantecas_y_margarinas", "manteca"),
        Product("lacteos", "mantecas_y_margarinas", "margarinas"),
    ]
    PASTAS_FRESCAS_Y_TAPAS: list[Product] = [
        Product("lacteos", "pastas_frescas_y_tapas", "fideos_y_ñoquis"),
        Product("lacteos", "pastas_frescas_y_tapas", "grasas"),
        Product("lacteos", "pastas_frescas_y_tapas", "masas_y_lavaduras"),
        Product("lacteos", "pastas_frescas_y_tapas", "pastas_rellenas"),
        Product("lacteos", "pastas_frescas_y_tapas", "tapas"),
    ]
    POSTRES: list[Product] = [
        Product("lacteos", "postres", ""),
    ]
    YOGURES: list[Product] = [
        Product("lacteos", "yogures", "yogures_descremados"),
        Product("lacteos", "yogures", "yogures_enteros"),
    ]

    EVERYTHING = [
        ALIMENTOS_VEGETALES,
        CREMAS,
        DULCE_DE_LECHE,
        LECHES,
        MANTECAS_Y_MARGARINAS,
        PASTAS_FRESCAS_Y_TAPAS,
        POSTRES,
        YOGURES
    ]

class Congelados:
    COMIDAS_CONGELADAS: list[Product] = [
        Product("congelados", "comidas_congeladas", "pizzas"),
        Product("congelados", "comidas_congeladas", "empanadas_y_tartas"),
        Product("congelados", "comidas_congeladas", "comidas_congeladas")
    ]
    FRUTAS: list[Product] =[
        Product("congelados", "frutas", "")
    ]   
    HAMBURGUESAS_Y_MILANESAS: list[Product] = [
        Product("congelados", "hamburguesas_y_milanesas", "")
    ]
    HELADOS_Y_POSTRES: list[Product] = [
        Product("congelados", "helados_y_postres", "")
    ]
    PAPAS: list[Product] = [
        Product("congelados", "papas", "")
    ]
    PESCADOS_Y_MARISCOS: list[Product] = [
        Product("congelados", "pescados_y_mariscos", ""),
    ]
    POLLOS_Y_CARNES: list[Product] =[
        Product("congelados", "pollo_y_carnes", "")
    ]   
    VEGETALES: list[Product] =[
        Product("congelados", "vegetales", "")
    ]

    EVERYTHING = [
        COMIDAS_CONGELADAS,
        FRUTAS,
        HAMBURGUESAS_Y_MILANESAS,
        HELADOS_Y_POSTRES,
        PAPAS,
        PESCADOS_Y_MARISCOS,
        POLLOS_Y_CARNES,
        VEGETALES
    ]

class PanaderiaYReposteria:
    PANADERIA: list[Product] =[
        Product("panadería_y_repostería", "panadería", "pizzas_y_prepizzas"),
        Product("panadería_y_repostería", "panadería", "sándwiches"),
        Product("panadería_y_repostería", "panadería", "panificados")
    ]
    REPOSTERIA: list[Product] =[
        Product("panadería_y_repostería", "repostería", "")
    ]

    EVERYTHING = [
        PANADERIA,
        REPOSTERIA
    ]

class ComidasPreparadas:
    MENU_FRIO: list[Product] =[
        Product("comidas_preparadas", "menú_frío", "")
    ]
    MENU_CALIENTE: list[Product] =[
        Product("comidas_preparadas", "menú_caliente", "")
    ]
    POSTRES: list[Product] =[
        Product("comidas_preparadas", "postres", "")
    ]

    EVERYTHING = [
        MENU_CALIENTE,
        MENU_FRIO,
        POSTRES
    ]
    
class perfumeria:
    CUIDADO_CAPILAR = [
        Product("perfumeria", 'cuidado_capilar', 'coloración'),
        Product("perfumeria", 'cuidado_capilar', 'acondicionador'),
        Product("perfumeria", 'cuidado_capilar', 'fijación'),
        Product("perfumeria", 'cuidado_capilar', 'cepillos_para_pelo'),
        Product("perfumeria", 'cuidado_capilar', 'reparación_y_tratamientos'),
        Product("perfumeria", 'cuidado_capilar', 'shampoo'),
    ]
    CUIDADO_DE_LA_PIEL = [
            Product("perfumeria", 'cuidado_de_la_piel', 'cremas_corporales'),
            Product("perfumeria", 'cuidado_de_la_piel', 'cremas_desmaquillantes'),
            Product("perfumeria", 'cuidado_de_la_piel', 'cremas_faciales'),
            Product("perfumeria", 'cuidado_de_la_piel', 'solares_y_post-solares'),
        ]
    CUIDADO_PERSONAL = [
        Product("perfumeria", 'cuidado_personal', 'cepillos_y_Esponjas'),
        Product("perfumeria", 'cuidado_personal', 'depilación'),
        Product("perfumeria", 'cuidado_personal', 'desodorantes_de_hombres'),
        Product("perfumeria", 'cuidado_personal', 'desodorantes_de_mujer'),
        Product("perfumeria", 'cuidado_personal', 'desodorantes_y_polvos_pedicos'),
        Product("perfumeria", 'cuidado_personal', 'geles_de_Ducha'),
        Product("perfumeria", 'cuidado_personal', 'jabones'),
        Product("perfumeria", 'cuidado_personal', 'protección_adultos'),
        Product("perfumeria", 'cuidado_personal', 'protección_femenina'),
        Product("perfumeria", 'cuidado_personal', 'productos_para_afeitarse'),
        Product("perfumeria", 'cuidado_personal', 'quitaesmaltes'),
        Product("perfumeria", 'cuidado_personal', 'higiene_preventiva')
    ]

    CUIDADO_ORAL = [
        Product("perfumeria", 'cuidado_oral', 'pastas_dentales'),
        Product("perfumeria", 'cuidado_oral', 'cepillos_dentales'),
        Product("perfumeria", 'cuidado_oral', 'enjuagues_bucales'),
        Product("perfumeria", 'cuidado_oral', 'accesorios_dentales')
    ]

    FARMACIA = [
        Product("perfumeria", 'farmacia', 'algodón'),
        Product("perfumeria", 'farmacia', 'alcohol'),
        Product("perfumeria", 'farmacia', 'apósitos'),
        Product("perfumeria", 'farmacia', 'preservativos'),
        Product("perfumeria", 'farmacia', 'otros')
    ]
    MAQUILLAJE = [
        Product("perfumeria", 'maquillaje', ''),
    ]


    EVERYTHING = [
        CUIDADO_CAPILAR,
        CUIDADO_DE_LA_PIEL,
        CUIDADO_PERSONAL,
        CUIDADO_ORAL,
        FARMACIA,
        MAQUILLAJE
    ]
    
class Limpieza:
    ACCESORIOS_DE_LIMPIEZA: list[Product] = [
        Product("limpieza", "accesorios_de_limpieza", "bales_y_mopas"),
        Product("limpieza", "accesorios_de_limpieza", "bolsas"),
        Product("limpieza", "accesorios_de_limpieza", "broches_y_ganchos"),
        Product("limpieza", "accesorios_de_limpieza", "escobas_y_escobillones"),
        Product("limpieza", "accesorios_de_limpieza", "escobillas"),
        Product("limpieza", "accesorios_de_limpieza", "esponjas_y_guantes"),
        Product("limpieza", "accesorios_de_limpieza", "palas_y_cabos"),
        Product("limpieza", "accesorios_de_limpieza", "paños_multiusos"),
        Product("limpieza", "accesorios_de_limpieza", "secadores_y_cepillos"),
        Product("limpieza", "accesorios_de_limpieza", "trapos_de_piso"),
    ]
    
    CALZADO: list[Product] = [
        Product("limpieza", "calzado", "brillos_y_revividores"),
        Product("limpieza", "calzado", "limpiadores"),
        Product("limpieza", "calzado", "pomadas_para_calzado"),
    ]
    
    DESODORANTES_DE_AMBIENTE: list[Product] = [
        Product("limpieza", "desodorantes_de_ambiente", "absorbe_humedad"),
        Product("limpieza", "desodorantes_de_ambiente", "aromatizantes"),
        Product("limpieza", "desodorantes_de_ambiente", "desodorantes_y_desinfectantes"),
    ]
    
    INSECTICIDAS: list[Product] = [
        Product("limpieza", "insecticidas", "aerosoles"),
        Product("limpieza", "insecticidas", "aparatos"),
        Product("limpieza", "insecticidas", "cebos_bolillas_y_pastillas"),
        Product("limpieza", "insecticidas", "escobas_y_escobillones"),
        Product("limpieza", "insecticidas", "repelentes"),
        Product("limpieza", "insecticidas", "tabletas_y_difusores"),
    ]
    
    LAVANDINA: list[Product] = [
        Product("limpieza", "lavandina", ""),
    ]
    
    LIMPIEZA_DE_BAÑO: list[Product] = [
        Product("limpieza", "limpieza_de_baño", "desinfectantes"),
        Product("limpieza", "limpieza_de_baño", "destapa_cañerías"),
        Product("limpieza", "limpieza_de_baño", "pastillas_y_bloques"),
    ]
    
    CUIDADO_PARA_LA_ROPA: list[Product] = [
        Product("limpieza", "cuidado_para_la_ropa", "aprestos_y_blanqueadores"),
        Product("limpieza", "cuidado_para_la_ropa", "cepillo_para_ropa"),
        Product("limpieza", "cuidado_para_la_ropa", "jabón_en_pan"),
        Product("limpieza", "cuidado_para_la_ropa", "detergente_para_ropa"),
        Product("limpieza", "cuidado_para_la_ropa", "quitamanchas"),
        Product("limpieza", "cuidado_para_la_ropa", "suavizantes"),
        Product("limpieza", "cuidado_para_la_ropa", "perfumantes"),
    ]
    
    LIMPIEZA_DE_COCINA: list[Product] = [
        Product("limpieza", "limpieza_de_cocina", "detergentes"),
        Product("limpieza", "limpieza_de_cocina", "escarrabadientes"),
        Product("limpieza", "limpieza_de_cocina", "fosforos"),
        Product("limpieza", "limpieza_de_cocina", "limpiadores"),
        Product("limpieza", "limpieza_de_cocina", "limpiavidrios"),
        Product("limpieza", "limpieza_de_cocina", "productos_para_lavavajillas"),
    ]
    
    LIMPIEZA_DE_PISOS_Y_MUEBLES: list[Product] = [
        Product("limpieza", "limpieza_de_pisos_y_muebles", "ceras_y_autobrillos"),
        Product("limpieza", "limpieza_de_pisos_y_muebles", "limpiadores_de_pisos"),
        Product("limpieza", "limpieza_de_pisos_y_muebles", "lustramuebles"),
    ]
    
    PAPELES: list[Product] = [
        Product("limpieza", "papeles", "pañuelos"),
        Product("limpieza", "papeles", "papel_higiénico"),
        Product("limpieza", "papeles", "rollos_de_cocina"),
        Product("limpieza", "papeles", "servilletas"),
    ]
    
    EVERYTHNG = [
        ACCESORIOS_DE_LIMPIEZA,
        CALZADO,
        DESODORANTES_DE_AMBIENTE,
        INSECTICIDAS,
        LAVANDINA,
        LIMPIEZA_DE_BAÑO,
        CUIDADO_PARA_LA_ROPA,
        LIMPIEZA_DE_COCINA,
        LIMPIEZA_DE_PISOS_Y_MUEBLES,
        PAPELES
    ]

CONS_ELECTRO = Electro()
CONS_HOGAR = Hogar()
CONS_TIEMPO_LIBRE = TiempoLibre()
CONS_BEBES_NINOS = BebesNiños()
CONS_ALMACEN = Almacen()
CONS_BEBIDAS = Bebidas()
CONS_FRUTAS_VERDURAS = FrutasYVerduras()
CONS_CARNES = Carnes()
CONS_PESCADOS_MARISCOS = PescadosMariscos()
CONS_QUESOS_FIAMBRES = QuesosYFiambres()
CONS_LACTEOS = Lacteos()
CONS_CONGELADOS = Congelados()
CONS_PANADERIA_REPOSTERIA = PanaderiaYReposteria()
CONS_COMIDAS_PREPARADAS = ComidasPreparadas()
CONS_perfumeria = perfumeria()
CONS_LIMPIEZA = Limpieza()

CONS_CATEGORIES = ["electro", "hogar_y_textil", "tiempo_libre", "bebes_y_niños", "almacen", "bebidas", "frutas_y_verduras", "carnes", "pescados_y_mariscos", "quesos_y_fiambres", "lacteos", "congelados", "panadería_y_repostería", "comidas_preparadas", "perfumeria", "limpieza"]
CONS_EVERYTHING = CONS_ELECTRO.EVERYTHING + CONS_HOGAR.EVERYTHING + CONS_TIEMPO_LIBRE.EVERYTHING + CONS_BEBES_NINOS.EVERYTHING + CONS_ALMACEN.EVERYTHING + CONS_BEBIDAS.EVERYTHING + CONS_FRUTAS_VERDURAS.EVERYTHING + CONS_CARNES.EVERYTHING + CONS_PESCADOS_MARISCOS.EVERYTHING + CONS_QUESOS_FIAMBRES.EVERYTHING + CONS_LACTEOS.EVERYTHING + CONS_CONGELADOS.EVERYTHING + CONS_PANADERIA_REPOSTERIA.EVERYTHING + CONS_COMIDAS_PREPARADAS.EVERYTHING + CONS_perfumeria.EVERYTHING + CONS_LIMPIEZA.EVERYTHNG


