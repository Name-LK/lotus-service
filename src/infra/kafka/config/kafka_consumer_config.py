from src.shared.env import env

class KafkaConsumerConfig:
    def __init__(self, id: str):
        self.config = {
            'bootstrap.servers': f"{env._kafka_variables._server_address}:{env._kafka_variables._server_port}",
            'group.id' : id
        }