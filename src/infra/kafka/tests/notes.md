## Testes concluidos

- [x] test_kafka_consumer_factory.py
- [x] test_kafka_producer_factory.py
- [+-] test_custom_consumer.py
- [+-] test_custom_producer.py
- [x] test_kafka_consumer_config.py
- [x] test_kafka_producer_config

## OBS
## Testes incompletos

### test_custom_producer.py
- def delivery_callback()

### test_custom_consumer.py
- def poll()

Os testes tiveram um travamento devido ao loop interno da função do consumer e do producer