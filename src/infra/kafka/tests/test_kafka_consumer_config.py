from src.infra.kafka.config.kafka_consumer_config import KafkaConsumerConfig

def test_kafka_consumer_config_valid_config():
    #Arrange
    id = 'group-id'
    config = KafkaConsumerConfig(id=id)
    
    #Act
    valid_kafka_server_config = config.config['bootstrap.servers']
    valid_kafka_group_id = config.config['group.id']
    expected_kafka_server_config = 'localhost:9092'
    expected_kafka_group_id = 'group-id'
    
    #Assert
    assert valid_kafka_server_config == expected_kafka_server_config
    assert valid_kafka_group_id == expected_kafka_group_id 