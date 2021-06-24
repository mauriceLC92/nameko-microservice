from nameko.rpc import rpc


class UtilitiesService:
    name = "utilities_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
