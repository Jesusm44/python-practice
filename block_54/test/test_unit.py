
import unittest


class RecursoTemporal:
    def __init__(self):
        self.activo = False
        self.liberado = False

    def __enter__(self):
        self.activo = True
        print("[ENTER] Recurso adquirido")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.activo:
            self.activo = False
            self.liberado = True
            print("[EXIT] Cleanup ejecutado")

        return False


def reproducir():
    print("\n--- REPRODUCCIÓN ---")

    recurso = RecursoTemporal()

    try:
        with recurso as r:
            print(f"Recurso activo: {r.activo}")
            raise RuntimeError("Error durante la operación")

    except RuntimeError as error:
        print(f"Excepción propagada: {error}")

    else:
        print("El bloque terminó sin propagar una excepción")

    finally:
        print(f"Recurso liberado: {recurso.liberado}")


class TestRecursoTemporal(unittest.TestCase):

    def test_cleanup_tras_excepcion(self):
        recurso = RecursoTemporal()

        try:
            with recurso:
                raise RuntimeError("Error interno")
        except RuntimeError:
            pass

        self.assertFalse(recurso.activo)
        self.assertTrue(recurso.liberado)

    def test_excepcion_debe_propagarse(self):
        recurso = RecursoTemporal()

        with self.assertRaisesRegex(RuntimeError, "Error interno"):
            with recurso:
                raise RuntimeError("Error interno")


if __name__ == "__main__":
    reproducir()
    unittest.main(verbosity=2)
