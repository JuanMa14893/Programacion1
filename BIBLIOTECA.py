from _future_ import annotations
from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import Dict, List, Optional


# =========================
#   ABSTRACCIÓN (ABC)
# =========================
class MaterialBiblioteca(ABC):
    """
    Clase abstracta que define la interfaz común para todos los materiales.
    """

    def _init_(self, id_material: str, titulo: str, autor: str, anio: int):
        # =========================
        #   ENCAPSULAMIENTO
        # =========================
        self.__id_material = id_material
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = True

    # ------- Getters / Setters con validaciones (encapsulamiento) -------
    @property
    def id_material(self) -> str:
        return self.__id_material

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, value: str) -> None:
        if not value:
            raise ValueError("El título no puede estar vacío.")
        self.__titulo = value

    @property
    def autor(self) -> str:
        return self.__autor

    @autor.setter
    def autor(self, value: str) -> None:
        if not value:
            raise ValueError("El autor no puede estar vacío.")
        self.__autor = value

    @property
    def anio(self) -> int:
        return self.__anio

    @anio.setter
    def anio(self, value: int) -> None:
        if value < 0:
            raise ValueError("El año no puede ser negativo.")
        self.__anio = value

    @property
    def disponible(self) -> bool:
        return self.__disponible

    def _marcar_disponible(self, disponible: bool) -> None:
        self.__disponible = disponible

    # ------- Métodos abstractos (abstracción / polimorfismo) -------
    @abstractmethod
    def calcular_fecha_devolucion(self, fecha_prestamo: date) -> date:
        ...

    @abstractmethod
    def obtener_tipo(self) -> str:
        ...

    @abstractmethod
    def obtener_detalles(self) -> str:
        ...

    # Representación común
    def _str_(self) -> str:
        return f"[{self.obtener_tipo()}] {self.titulo} — {self.autor} ({self.anio}) | ID: {self.id_material} | {'Disponible' if self.disponible else 'Prestado'}"


# =========================
#   HERENCIA + POLIMORFISMO
# =========================
class Libro(MaterialBiblioteca):
    def _init_(self, id_material: str, titulo: str, autor: str, anio: int, isbn: str, paginas: int):
        super()._init_(id_material, titulo, autor, anio)
        self.__isbn = isbn
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def paginas(self) -> int:
        return self.__paginas

    # POLIMORFISMO
    def calcular_fecha_devolucion(self, fecha_prestamo: date) -> date:
        return fecha_prestamo + timedelta(days=15)

    def obtener_tipo(self) -> str:
        return "Libro"

    def obtener_detalles(self) -> str:
        return f"ISBN: {self.isbn}, páginas: {self.paginas}"


class Revista(MaterialBiblioteca):
    def _init_(self, id_material: str, titulo: str, autor: str, anio: int, numero: int, periodicidad: str):
        super()._init_(id_material, titulo, autor, anio)
        self.__numero = numero
        self.__periodicidad = periodicidad

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def periodicidad(self) -> str:
        return self.__periodicidad

    # POLIMORFISMO
    def calcular_fecha_devolucion(self, fecha_prestamo: date) -> date:
        return fecha_prestamo + timedelta(days=7)

    def obtener_tipo(self) -> str:
        return "Revista"

    def obtener_detalles(self) -> str:
        return f"Número: {self.numero}, periodicidad: {self.periodicidad}"


class MaterialAudiovisual(MaterialBiblioteca):
    def _init_(self, id_material: str, titulo: str, autor: str, anio: int, formato: str, duracion_min: int):
        super()._init_(id_material, titulo, autor, anio)
        self.__formato = formato            # p.ej., "DVD", "Blu-ray", "MP4"
        self.__duracion_min = duracion_min  # duración en minutos

    @property
    def formato(self) -> str:
        return self.__formato

    @property
    def duracion_min(self) -> int:
        return self.__duracion_min

    # POLIMORFISMO
    def calcular_fecha_devolucion(self, fecha_prestamo: date) -> date:
        return fecha_prestamo + timedelta(days=3)

    def obtener_tipo(self) -> str:
        return "Material Audiovisual"

    def obtener_detalles(self) -> str:
        return f"Formato: {self.formato}, duración: {self.duracion_min} min"


# =========================
#   USUARIOS Y PRÉSTAMOS
# =========================
class Usuario:
    def _init_(self, id_usuario: str, nombre: str, tipo: str = "estudiante", max_prestamos: int = 5):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__tipo = tipo  # estudiante, docente, externo…
        self.__max_prestamos = max_prestamos

    @property
    def id_usuario(self) -> str:
        return self.__id_usuario

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def max_prestamos(self) -> int:
        return self.__max_prestamos

    def _str_(self) -> str:
        return f"{self.nombre} (#{self.id_usuario}, {self.tipo})"


class Prestamo:
    def _init_(self, usuario: Usuario, material: MaterialBiblioteca, fecha_prestamo: date):
        self.__usuario = usuario
        self.__material = material
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion_estimada = material.calcular_fecha_devolucion(fecha_prestamo)
        self.__devuelto = False

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def material(self) -> MaterialBiblioteca:
        return self.__material

    @property
    def fecha_prestamo(self) -> date:
        return self.__fecha_prestamo

    @property
    def fecha_devolucion_estimada(self) -> date:
        return self.__fecha_devolucion_estimada

    @property
    def devuelto(self) -> bool:
        return self.__devuelto

    def marcar_devuelto(self) -> None:
        self.__devuelto = True
        self.__material._marcar_disponible(True)

    def _str_(self) -> str:
        estado = "Devuelto" if self.devuelto else "En préstamo"
        return f"{self.material.titulo} → {self.usuario.nombre} | {estado} | F.Prest: {self.fecha_prestamo} | F.Devol (est.): {self.fecha_devolucion_estimada}"


# =========================
#   BIBLIOTECA (ORQUESTADOR)
# =========================
class Biblioteca:
    def _init_(self, nombre: str):
        self.__nombre = nombre
        self.__materiales: Dict[str, MaterialBiblioteca] = {}
        self.__usuarios: Dict[str, Usuario] = {}
        self.__prestamos_activos: List[Prestamo] = []
        self.__historial_prestamos: List[Prestamo] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    # ---- Gestión de materiales ----
    def agregar_material(self, material: MaterialBiblioteca) -> None:
        if material.id_material in self.__materiales:
            raise ValueError("Ya existe un material con ese ID.")
        self.__materiales[material.id_material] = material

    def buscar_material(self, texto: str) -> List[MaterialBiblioteca]:
        t = texto.lower()
        return [
            m for m in self.__materiales.values()
            if t in m.titulo.lower() or t in m.autor.lower() or t in m.obtener_tipo().lower()
        ]

    def obtener_material(self, id_material: str) -> Optional[MaterialBiblioteca]:
        return self.__materiales.get(id_material)

    # ---- Gestión de usuarios ----
    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.id_usuario in self.__usuarios:
            raise ValueError("Ya existe un usuario con ese ID.")
        self.__usuarios[usuario.id_usuario] = usuario

    def obtener_usuario(self, id_usuario: str) -> Optional[Usuario]:
        return self.__usuarios.get(id_usuario)

    # ---- Préstamos ----
    def prestamos_de_usuario(self, id_usuario: str) -> List[Prestamo]:
        return [p for p in self.__prestamos_activos if p.usuario.id_usuario == id_usuario and not p.devuelto]

    def prestar(self, id_usuario: str, id_material: str, fecha_prestamo: Optional[date] = None) -> Prestamo:
        usuario = self.obtener_usuario(id_usuario)
        material = self.obtener_material(id_material)
        if usuario is None:
            raise ValueError("Usuario no encontrado.")
        if material is None:
            raise ValueError("Material no encontrado.")
        if not material.disponible:
            raise ValueError("El material no está disponible.")
        if len(self.prestamos_de_usuario(id_usuario)) >= usuario.max_prestamos:
            raise ValueError("El usuario alcanzó el máximo de préstamos.")

        fecha_prestamo = fecha_prestamo or date.today()
        prestamo = Prestamo(usuario, material, fecha_prestamo)
        material._marcar_disponible(False)
        self.__prestamos_activos.append(prestamo)
        return prestamo

    def devolver(self, id_material: str) -> None:
        # buscar préstamo activo por material
        for p in self.__prestamos_activos:
            if p.material.id_material == id_material and not p.devuelto:
                p.marcar_devuelto()
                # mover al historial
                self.__historial_prestamos.append(p)
                self.__prestamos_activos.remove(p)
                return
        raise ValueError("No se encontró un préstamo activo para ese material.")

    # ---- Reportes / utilidades ----
    def listar_materiales(self) -> List[MaterialBiblioteca]:
        return list(self.__materiales.values())

    def listar_prestamos_activos(self) -> List[Prestamo]:
        return list(self.__prestamos_activos)

    def _str_(self) -> str:
        return f"Biblioteca «{self.nombre}» | Materiales: {len(self._materiales)} | Usuarios: {len(self.usuarios)} | Préstamos activos: {len(self._prestamos_activos)}"


# =========================
#   EJEMPLO DE USO
# =========================
if _name_ == "_main_":
    biblio = Biblioteca("Municipal")

    # Materiales (herencia + polimorfismo en calcular fecha)
    m1 = Libro("L-001", "El Quijote", "Cervantes", 1605, isbn="978-3-16-148410-0", paginas=863)
    m2 = Revista("R-010", "Science Today", "AA.VV.", 2025, numero=128, periodicidad="Mensual")
    m3 = MaterialAudiovisual("A-777", "Planeta Tierra", "BBC", 2016, formato="Blu-ray", duracion_min=120)

    biblio.agregar_material(m1)
    biblio.agregar_material(m2)
    biblio.agregar_material(m3)

    # Usuarios
    u1 = Usuario("U-001", "Ana Gómez", "estudiante", max_prestamos=3)
    u2 = Usuario("U-002", "Luis Pérez", "docente", max_prestamos=10)

    biblio.registrar_usuario(u1)
    biblio.registrar_usuario(u2)

    # Préstamos
    p1 = biblio.prestar("U-001", "L-001", date(2025, 9, 5))
    p2 = biblio.prestar("U-001", "R-010", date(2025, 9, 5))

    print(biblio)
    for m in biblio.listar_materiales():
        print(m, "→", m.obtener_detalles())
    print("\nPréstamos activos:")
    for p in biblio.listar_prestamos_activos():
        print("  ", p)

    # Devolución
    biblio.devolver("L-001")
    print("\nTras devolver L-001:")
    for p in biblio.listar_prestamos_activos():
        print("  ", p)