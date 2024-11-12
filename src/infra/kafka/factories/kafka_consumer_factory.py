class KafkaConsumerFactory:
    def __init__(self):
        self._configurations = {}
        self._consumer_class = None

    def register_configuration(self, config_name, config):
        """Register the consumer config params

        Args:
            config_name (_str_): config key
            config (_kafkaConsumerConfig_): __
        """
        self._configurations[config_name] = config

    def register_consumer_class(self, consumer_class):
        """Register the consumer class module

        Args:
            consumer_class (_type_): _description_
        """
        self._consumer_class = consumer_class

    def create_consumer(self, config_name): 
        config = self._configurations.get(config_name)
        if not config:
            raise ValueError(f"Configuration '{config_name}' not found")
        if not self._consumer_class:
            raise ValueError("Unregistered consumer class")
        return self._consumer_class(config)