from src import KafkaProducerFactory
from src.infra.kafka.config.kafka_producer_config import KafkaProducerConfig
from src.infra.kafka.producers.custom_producer import CustomProducer
import pytest

def test_register_configuration():
    #Arrange
    config_name = 'config_1'
    config = KafkaProducerConfig()
    factory = KafkaProducerFactory()
    
    #Act
    factory.register_configuration(config_name=config_name, config=config)
    
    #Assert
    assert factory._configurations[config_name] == config

def test_register_producer_class():
    #Arrange
    config = KafkaProducerConfig()
    config_name = 'config_1'
    factory = KafkaProducerFactory()
        
    #Act
    factory.register_configuration(config_name=config_name, config=config)
    factory.register_producer_class(producer_class=CustomProducer)
    
    #Assert
    assert factory._producer_class ==  CustomProducer

def test_create_producer_valid_configuration():
    #Arrange
    valid_config = KafkaProducerConfig().config
    valid_config_name = 'config_1'
    factory = KafkaProducerFactory()
    
    #Act
    factory.register_configuration(config_name=valid_config_name, config=valid_config)
    factory.register_producer_class(producer_class=CustomProducer)
    producer = factory.create_producer(config_name=valid_config_name)
    
    #Assert
    assert isinstance(producer, CustomProducer)

def test_create_producer_invalid_configuration():
    #Arrange
    invalid_config_name = 'invalid configuration'
    factory = KafkaProducerFactory()
    
    #Act & Assert
    with pytest.raises(ValueError, match=f"Configuration '{invalid_config_name}' not found"):
        factory.create_producer(config_name=invalid_config_name)