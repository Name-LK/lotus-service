import pytest
from unittest.mock import patch, MagicMock
from src.infra.kafka.producers.custom_producer import CustomProducer
from src.infra.kafka.config.kafka_producer_config import KafkaProducerConfig

def test_init():
    #Arrange
    config = KafkaProducerConfig().config
    
    #Act & Assert
    with patch('src.infra.kafka.producers.custom_producer.Producer') as MockProducer:
        producer = CustomProducer(config)
        MockProducer.assert_called_once_with(config)
        assert isinstance(producer.producer, MockProducer.return_value.__class__)

def test_producing():
    #Arrange
    config = KafkaProducerConfig().config
    test_message = 'test message'

    #Act & Assert
    with patch('builtins.input', return_value=test_message):
        producer = CustomProducer(config)
        message = producer.message()
        
        assert message == test_message

    