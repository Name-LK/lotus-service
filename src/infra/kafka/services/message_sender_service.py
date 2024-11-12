from src.infra.kafka.factories.kafka_producer_factory import KafkaProducerFactory
from src.infra.kafka.config.kafka_producer_config import KafkaProducerConfig
from src.infra.kafka.producers.custom_producer import CustomProducer

def main():
    config_name = 'config_1'
    
    config = KafkaProducerConfig()
    config = config.config
    
    topic = 'mensagem'
        
    producer_factory = KafkaProducerFactory()
    producer_factory.register_configuration(config=config, config_name=config_name)
    producer_factory.register_producer_class(CustomProducer)
    producer = producer_factory.create_producer(config_name)
    
    producer.producing(topic)
    
if __name__ == "__main__":
    main()