from src.shared.env import env

class KafkaProducerConfig:
    def __init__(self):
        self.config = {
            'bootstrap.servers': f"{env._kafka_variables._server_address}:{env._kafka_variables._server_port}"
        }