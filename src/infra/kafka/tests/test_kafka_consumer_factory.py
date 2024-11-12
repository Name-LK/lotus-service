import pytest
from src import KafkaConsumerFactory
from src.infra.kafka.config.kafka_consumer_config import KafkaConsumerConfig
from src.infra.kafka.consumers.custom_consumer import CustomConsumer

def test_register_configuration():
    #arrange
    id = 'group-id'
    config_name = 'config_1'
    factory = KafkaConsumerFactory()
    config = KafkaConsumerConfig(id=id).config
    
    #Act
    factory.register_configuration(config_name=config_name, config=config)
    
    #Assert
    assert config_name in factory._configurations
    assert factory._configurations[config_name] == config 

def test_register_consumer_class():
    #arrange
    factory = KafkaConsumerFactory()
    
    #Act
    factory.register_consumer_class(CustomConsumer)
    
    #Assert
    assert factory._consumer_class == CustomConsumer

def test_create_consumer_valid_configuration():
    #arrange
    id = 'group-id'
    valid_config_name = 'config-1'
    factory = KafkaConsumerFactory()
    valid_config = KafkaConsumerConfig(id=id).config
    
    #Act
    factory.register_configuration(config_name=valid_config_name, config=valid_config)
    factory.register_consumer_class(CustomConsumer)
    consumer = factory.create_consumer(config_name=valid_config_name)
    
    #Assert
    assert isinstance(consumer, CustomConsumer)

def test_create_consumer_invalid_configuration():
    #Arrange
    invalid_config_name = 'invalid config name'
    factory = KafkaConsumerFactory()
    
    #Act & Assert
    with pytest.raises(ValueError, match=f"Configuration '{invalid_config_name}' not found"):
        factory.create_consumer(invalid_config_name)

def test_create_consumer_no_consumer_class():
    #Arrange
    config = KafkaConsumerConfig(id=id).config
    config_name = 'config_1'
    factory = KafkaConsumerFactory()
    
    #Act
    factory.register_configuration(config_name=config_name, config=config)
    
    #Assert
    with pytest.raises(ValueError, match="Unregistered consumer class"):
        factory.create_consumer(config_name=config_name)