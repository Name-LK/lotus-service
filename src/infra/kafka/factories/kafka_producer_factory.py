class KafkaProducerFactory:
    def __init__(self):
        self._configurations = {}
        self._producer_class = None

    def register_configuration(self, config_name, config):
        self._configurations[config_name] = config

    def register_producer_class(self, producer_class):
        self._producer_class = producer_class

    def create_producer(self, config_name): 
        config = self._configurations.get(config_name)
        if not config:
            raise ValueError(f"Configuration '{config_name}' not found")
        if not self._producer_class:
            raise ValueError("Unregistered consumer class")
        return self._producer_class(config)