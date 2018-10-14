# Benchmarking Modern AMQP Message Brokers

Message broker systems have become a popular architectural choice in distributed systems, providing greater network scalability and flexibility than the traditional client-server model. This recent rise in popularity has caused countless options of broker system configurations to emerge. Broker systems vary on dimensions such as message passing scheme, broker setup, and protocols used. Most brokers claim to be robust, fast and reliable, but sometimes these claims are unsubstantiated. In addition, it is difficult to figure out the right broker that satis es an application's requirements, thus, it becomes necessary to paint a more vivid picture of the many options available. 

This project and the resultant paper aims to give a clear view on the myriad of message broker system options available through a survey and also by benchmarking two popular systems, __ActiveMQ and RabbitMQ__ under various workloads. These two brokers are investigated on their quality of service features such as _tail latency and scalability_.

### Graphs

[RabbitMQ Tail Latency with 1 million 1000 byte messages](graphs/rabbit_mq_1000.png)

[ActiveMQ Tail Latency with 1 million 1000 bytes messages](graphs/active_1000.png)

[RabbitMQ throughput with 1 million 1000 byte messages](graphs/rabbit_thru_1000.png)

[ActiveMQ throughput with 1 million 1000 bytes messages](graphs/active_thru_1000.png)
