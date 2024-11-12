import pytest
from unittest.mock import patch, MagicMock
from src.infra.kafka.consumers.custom_consumer import CustomConsumer
from src.infra.kafka.config.kafka_consumer_config import KafkaConsumerConfig
from confluent_kafka import KafkaError

def test_init():
    #Arrange
    id = 'group-id'
    config = KafkaConsumerConfig(id=id).config
    
    #Act & #Assert
    with patch('src.infra.kafka.consumers.custom_consumer.Consumer') as MockConsumer:
        consumer = CustomConsumer(config)
        
        MockConsumer.assert_called_once_with(config)
        assert consumer.consumer == MockConsumer.return_value

def test_subscribe():
    #Arrange
    id = 'group-id'
    config = KafkaConsumerConfig(id=id)
    topics = ['test-topic']
    
    #Act & Assert
    with patch('src.infra.kafka.consumers.custom_consumer.Consumer') as MockConsumer:
        mock_consumer_instance = MockConsumer.return_value
        consumer = CustomConsumer(config)
        consumer.subscribe(topics)
        mock_consumer_instance.subscribe.assert_called_once_with(topics)
    
def test_close():
    #Arrange
    id = 'group-id'
    config = KafkaConsumerConfig(id=id)
    
    #Act & Assert
    with patch('src.infra.kafka.consumers.custom_consumer.Consumer') as MockConsumer:
        mock_consumer_instance = MockConsumer.return_value
        consumer = CustomConsumer(config)
        
        consumer.close()
        
        mock_consumer_instance.close.assert_called_once()
        
def test_poll_valid_message():
    id = 'group-id'
    config = KafkaConsumerConfig(id=id).config
    msg_mock = MagicMock()
    msg_mock.error.return_value = None
    msg_mock.value.return_value = b'valid message'
    
    with patch('src.infra.kafka.consumers.custom_consumer.Consumer') as MockConsumer:
        mock_consumer_instance = MockConsumer.return_value
        mock_consumer_instance.poll.return_value = msg_mock
        
        consumer = CustomConsumer(config=config)
        
        with patch('src.infra.kafka.consumers.custom_consumer.logger') as mock_logger:
            consumer.poll(timeout=1)
            mock_logger.info.assert_called_with('valid message')

def test_poll_invalid_message():
    id = 'group-id'
    config = KafkaConsumerConfig(id=id).config
    msg_mock = MagicMock()
    msg_mock.error.return_value.code.return_value = KafkaError._PARTITION_EOF
    
    with patch('src.infra.kafka.consumers.custom_consumer.Consumer') as MockConsumer:
        mock_consumer_instance = MockConsumer.return_value
        mock_consumer_instance.poll.return_value = msg_mock
        
        consumer = CustomConsumer(config=config)
        
        with patch('src.infra.kafka.consumers.custom_consumer.logger') as mock_logger:
            consumer.poll(timeout=1.0)
            mock_logger.warning.assert_called()