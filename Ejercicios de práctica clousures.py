# Nombre: Guale Orrala Maite
# Curso: Programacion Funcional 5/1
# Docente_ Ingeniero Pachay
# Fecha: 26-Septiembre-2026

import time
import random

# ============================================================
# NIVEL 1: Closures con Inyección de Comportamiento
# ============================================================
print("\n")

# 1.1 Generador de Formateadores con Transformación
def crear_formateador(prefijo, fn_transformacion):
    """Retorna un closure que aplica fn_transformacion y concatena el prefijo."""
    def formateador(texto):
        return f"{prefijo}{fn_transformacion(texto)}"
    return formateador


# 1.2 Multiplicador Paramétrico con Mapeo
def crear_operador(factor, operacion_lambda):
    """Retorna un closure que aplica la operación usando el factor encapsulado."""
    def operador(valor):
        return operacion_lambda(valor, factor)
    return operador


# 1.3 Calculador de Descuentos con Regla Dinámica
def crear_descuento_dinamico(regla_condicional_lambda, porcentaje=0.10):
    """Retorna un closure que evalúa el precio con la lambda y aplica descuento."""
    def calcular(precio):
        if regla_condicional_lambda(precio):
            return precio * (1 - porcentaje)
        return precio
    return calcular


# 1.4 Generador de Seriales / Nombres Únicos
def crear_generador_sufijos(patron_lambda):
    """Retorna un closure que transforma nombres de archivos con la lambda de formato."""
    contador = {"n": 0}
    def generar(nombre):
        contador["n"] += 1
        return patron_lambda(nombre, contador["n"])
    return generar


# 1.5 Conversor de Divisas con Margen
def crear_conversor(tasa, margen_lambda):
    """Retorna una función que convierte montos con comisión dinámica."""
    def convertir(monto):
        comision = margen_lambda(monto)
        return (monto * tasa) - comision
    return convertir


# ==================== PRUEBAS NIVEL 1 ====================
print("=" * 60)
print("NIVEL 1: Closures con Inyección de Comportamiento")
print("=" * 60)
print("\n")

fmt_mayus = crear_formateador(">> ", lambda t: t.upper())
fmt_inv   = crear_formateador("<< ", lambda t: t[::-1])
print(fmt_mayus("hola mundo"))       # >> HOLA MUNDO
print(fmt_inv("python"))             # << nohtyp
print("\n")

duplicar  = crear_operador(2, lambda v, f: v * f)
potenciar = crear_operador(3, lambda v, f: v ** f)
print(duplicar(10))                  # 20
print(potenciar(2))                  # 8
print("\n")

desc_black = crear_descuento_dinamico(lambda p: p > 1000, 0.20)
print(desc_black(1500))              # 1200.0
print(desc_black(500))               # 500
print("\n")

serial = crear_generador_sufijos(lambda n, i: f"{n}_v{i:03d}")
print(serial("reporte"))             # reporte_v001
print(serial("factura"))             # factura_v002
print("\n")

conv = crear_conversor(4000, lambda m: m * 0.02)
print(conv(100))                     # 399998.0


# ============================================================
# NIVEL 2: Estado Encapsulado Avanzado (nonlocal + Lambdas)
# ============================================================
print("\n")

# 2.1 Contador Ponderado
def crear_contador_paso(fn_paso):
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return incrementar


# 2.2 Acumulador con Filtro de Aceptación
def crear_acumulador_validado(criterio_lambda):
    total = 0
    def agregar(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return agregar


# 2.3 Promediador con Eliminación de Valores Extremos
def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []
    def agregar(valor):
        if not filtro_ruido_lambda(valor):
            datos.append(valor)
        return sum(datos) / len(datos) if datos else 0
    return agregar


# 2.4 Limitador de Tasa Inteligente
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True
    return ejecutar


# 2.5 Interruptor Múltiple
def crear_conmutador(lista_estados):
    idx = 0
    def siguiente():
        nonlocal idx
        estado = lista_estados[idx]
        idx = (idx + 1) % len(lista_estados)
        return estado
    return siguiente


# ==================== PRUEBAS NIVEL 2 ====================
print("\n" + "=" * 60)
print("NIVEL 2: Estado Encapsulado Avanzado")
print("=" * 60)
print("\n")

contador = crear_contador_paso(lambda c: c + 5 if c < 20 else c)
print([contador() for _ in range(6)])   # [5, 10, 15, 20, 20, 20]
print("\n")

acum = crear_acumulador_validado(lambda v: v > 0)
print([acum(v) for v in [10, -5, 20, -3, 5]])   # [10, 10, 30, 30, 35]
print("\n")

prom = crear_promediador_filtrado(lambda v: v > 1000)
print([prom(v) for v in [10, 20, 2000, 30, 40]])  # 10, 15, 15, 20, 25
print("\n")

alerta = lambda n: print(f"⚠️  Límite superado: {n} intentos")
limit = crear_limitador_avanzado(3, alerta)
for i in range(5):
    print(f"Intento {i+1}: {'OK' if limit() else 'BLOQUEADO'}")
print("\n")

sw = crear_conmutador(["ON", "OFF", "STANDBY"])
print([sw() for _ in range(7)])   # ON OFF STANDBY ON OFF STANDBY ON


# ============================================================
# NIVEL 3: HOFs Complejas combinadas con Closures y Lambdas
# ============================================================
print("\n")

# 3.1 Pipeline de Mapeo y Filtrado Combinado
def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


# 3.2 Reductor / Agrupador Personalizado
def agrupar_por(lista, fn_clave):
    resultado = {}
    for item in lista:
        k = fn_clave(item)
        resultado.setdefault(k, []).append(item)
    return resultado


# 3.3 Ejecutor Repetitivo con Estado Accesible
def ejecutar_y_rastrear(fn_tarea, n):
    historial = []
    def ejecutar():
        for _ in range(n):
            historial.append(fn_tarea())
        return historial.copy()
    return ejecutar


# 3.4 Compositor de Cadenas de Operaciones
def componer_dos(f, g):
    return lambda x: f(g(x))


# 3.5 Decorador / HOF de Profiling y Auditoría
def auditar_ejecucion(fn_objetivo, fn_logger):
    """Mide el tiempo de ejecución y envía el informe al logger pasado por parámetro."""
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger(f"Función '{fn_objetivo.__name__}' | "
                  f"args={args} | tiempo={duracion:.6f}s | resultado={resultado}")
        return resultado
    return wrapper


# ==================== PRUEBAS NIVEL 3 ====================
print("\n" + "=" * 60)
print("NIVEL 3: HOFs Complejas")
print("=" * 60)
print("\n")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(procesar_coleccion(nums, lambda x: x % 2 == 0, lambda x: x ** 2))
# [4, 16, 36, 64, 100]
print("\n")

personas = [
    {"nombre": "Ana",  "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Eva",  "edad": 25},
    {"nombre": "Max",  "edad": 30},
]
print(agrupar_por(personas, lambda p: p["edad"]))
# {25: [...], 30: [...]}
print("\n")

tarea = lambda: random.randint(1, 100)
trazar = ejecutar_y_rastrear(tarea, 5)
print(trazar())
print("Historial acumulado en 2da llamada:", trazar())
print("\n")

sumar_uno = lambda x: x + 1
duplicar  = lambda x: x * 2
compuesta = componer_dos(sumar_uno, duplicar)   # f(g(x)) → (x*2)+1
print(compuesta(10))   # 21

compuesta2 = componer_dos(lambda x: x ** 2, compuesta)
print(compuesta2(3))   # ((3*2)+1)^2 = 49
print("\n")

# 3.5 (forma funcional)
logger = lambda msg: print(f"[AUDIT] {msg}")

def operacion_lenta(n):
    total = 0
    for i in range(n):
        total += i
    return total

op_auditada = auditar_ejecucion(operacion_lenta, logger)
op_auditada(100000)


# ============================================================
# NIVEL 4: Patrones Avanzados de Arquitectura Funcional
# ============================================================
print("\n")

# 4.1 Validador Compuesto de Reglas de Negocio
def crear_validador_multiple(*lambdas_criterios):
    def validar(obj):
        return all(criterio(obj) for criterio in lambdas_criterios)
    return validar


# 4.2 Caché con Expiración o Tamaño Máximo (Memoización)
def memoizar_avanzado(fn_costosa, max_items):
    cache = {}
    orden = []   # FIFO para desalojo
    def wrapper(*args):
        if args in cache:
            return cache[args]
        resultado = fn_costosa(*args)
        if len(cache) >= max_items:
            viejo = orden.pop(0)
            cache.pop(viejo, None)
        cache[args] = resultado
        orden.append(args)
        return resultado
    return wrapper


# 4.3 Motor de Pipeline Secuencial (Currying / Middleware)
def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato_inicial):
        resultado = dato_inicial
        for fn in funciones_transformacion:
            resultado = fn(resultado)
        return resultado
    return ejecutar


# 4.4 Sistema Pub/Sub
def crear_sistema_eventos():
    suscriptores = {}
    def gestor(accion, evento=None, callback=None, data=None):
        if accion == "suscribir":
            suscriptores.setdefault(evento, []).append(callback)
            return f"Suscrito a '{evento}'"
        elif accion == "emitir":
            for cb in suscriptores.get(evento, []):
                cb(data)
            return f"Emitido '{evento}' a {len(suscriptores.get(evento, []))} suscriptores"
        elif accion == "desuscribir":
            if evento in suscriptores and callback in suscriptores[evento]:
                suscriptores[evento].remove(callback)
            return f"Desuscrito de '{evento}'"
    return gestor


# 4.5 Mini-Query Engine sobre Listas de Objetos
def crear_consultor(campo):
    def constructor_filtro(operacion_lambda):
        def aplicar(lista):
            return [obj for obj in lista if operacion_lambda(obj.get(campo))]
        return aplicar
    return constructor_filtro


# ==================== PRUEBAS NIVEL 4 ====================
print("\n" + "=" * 60)
print("NIVEL 4: Patrones Avanzados")
print("=" * 60)
print("\n")

# 4.1
validador = crear_validador_multiple(
    lambda u: "email" in u and "@" in u["email"],
    lambda u: len(u.get("password", "")) >= 8,
    lambda u: u.get("edad", 0) >= 18
)
print(validador({"email": "a@b.com", "password": "12345678", "edad": 20}))  # True
print(validador({"email": "a@b.com", "password": "123",      "edad": 20}))  # False
print("\n")

# 4.2
def lenta(x):
    time.sleep(0.05)
    return x ** 2

memo = memoizar_avanzado(lenta, max_items=3)
inicio = time.perf_counter()
for i in [1, 2, 3, 1, 2, 4, 5]:   # 1,2,3 → 1,2 (hit), 4 (desaloja 3), 5 (desaloja 1)
    memo(i)
print(f"Tiempo total: {time.perf_counter() - inicio:.3f}s")
print("\n")

# 4.3
pipeline = crear_pipeline(
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x ** 2
)
print(pipeline(5))   # ((5+10)*2)^2 = 900
print("\n")

# 4.4
bus = crear_sistema_eventos()
bus("suscribir", evento="login", callback=lambda d: print(f"  → Login: {d}"))
bus("suscribir", evento="login", callback=lambda d: print(f"  → Auditoría: {d['user']}"))
print(bus("emitir", evento="login", data={"user": "ana", "ip": "1.2.3.4"}))
print(bus("emitir", evento="logout"))
print("\n")

# 4.5
productos = [
    {"nombre": "Laptop",  "precio": 1200, "stock": 5},
    {"nombre": "Mouse",   "precio": 25,   "stock": 0},
    {"nombre": "Monitor", "precio": 300,  "stock": 8},
    {"nombre": "Teclado", "precio": 80,   "stock": 0},
]
consultor_precio = crear_consultor("precio")
caros = consultor_precio(lambda p: p > 100)(productos)

consultor_stock = crear_consultor("stock")
en_stock = consultor_stock(lambda s: s > 0)(productos)

print("Caros:", [p["nombre"] for p in caros])         # ['Laptop', 'Monitor']
print("En stock:", [p["nombre"] for p in en_stock])   # ['Laptop', 'Monitor']