# Interview Guide

## Architecture
- Why Kafka? It decouples producers and consumers and supports durable, scalable event delivery.
- Why Spark Structured Streaming? It provides distributed processing, event-time windows, watermarks, and checkpointing.

## Reliability
- How are duplicates handled? Events use event_id and are deduplicated before aggregation.
- How would you handle failures? Use Spark checkpoints, Kafka consumer offsets, retries, and a dead-letter topic for invalid events.

## Scaling
- Increase Kafka partitions based on throughput.
- Parallelize Spark processing and tune state retention.
- Batch database writes and use connection pooling.

## Monitoring
Track consumer lag, throughput, processing latency, rejected events, checkpoint failures, and database write failures.
