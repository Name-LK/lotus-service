from src.infra.kafka.factories.kafka_consumer_factory import KafkaConsumerFactory
from src.infra.kafka.config.kafka_consumer_config import KafkaConsumerConfig
from src.infra.kafka.consumers.custom_consumer import CustomConsumer 

def main():
    config_name = 'config_1'
    group_id = 'g_01'
    
    config = KafkaConsumerConfig(id=group_id)
    config = config.config
    
    topic = 'mensagem'
    
    consumer_factory = KafkaConsumerFactory()
    consumer_factory.register_configuration(config=config, config_name=config_name)
    consumer_factory.register_consumer_class(CustomConsumer) 
    consumer = consumer_factory.create_consumer(config_name)
    consumer.subscribe([topic])
    consumer.poll(timeout=1.0)
        
if __name__ == "__main__":
    main()