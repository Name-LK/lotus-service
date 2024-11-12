from src.infra.kafka.config.kafka_producer_config import KafkaProducerConfig

def test_kafka_consumer_config_valid_config():
    #Arrange
    config = KafkaProducerConfig()
    
    #Act
    valid_kafka_server_config = config.config['bootstrap.servers']
    expected_kafka_server_config = 'localhost:9092'
    
    #Assert
    assert valid_kafka_server_config == expected_kafka_server_config