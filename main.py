from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self) -> None:
        print("RealSubject: Solicitud de tramitacion.")


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Revisando la prioridad de acceso para enviar una respuesta real.")
        return True

    def log_access(self) -> None:
        print("Proxy: Cargando el tiempo de respuesta.", end="")


def client_code(subject: Subject) -> None:
    """
    El código del cliente se supone que trabaja con todos los objetos (ambos sujetos y proxies). Utiliza la interfaz en orden de soporte y proxies. En la vida real, también, los clientes más utilizados trabajan con los sujetos directamente. En este caso, para implementar el patrón más facilmente, se puede extender el proxy desde el objeto de la clase real
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Cliente: Ejecutanto el codigo con el sujeto real:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Cliente:Ejecutando el mismo codigo, pero utilizando el proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)