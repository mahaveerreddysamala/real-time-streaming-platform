# Real-Time Streaming Platform

Production-style event streaming pipeline for ingesting, validating, aggregating, and serving near-real-time business events.

## Stack
Python · Apache Kafka · Spark Structured Streaming · PostgreSQL · Docker · SQL

## Flow
Event producer → Kafka topic → streaming validation → windowed aggregation → PostgreSQL analytics store.

## Features
- Event-driven architecture
- JSON schema validation
- Duplicate-event handling
- Windowed aggregations
- Consumer/producer separation
- Containerized local development
