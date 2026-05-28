# Representational State Transfer (REST) (Fielding, 2000)

## Citation

Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine. https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm

## Source Type

Academic Paper

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

REST defines six architectural constraints for network-based software that enable scalable, reliable, and maintainable distributed systems by treating network communication as stateless operations on resources identified by URLs.

## Core Findings

1. **Six architectural constraints**: Client-Server (separation of concerns), Stateless (each request self-contained), Cacheable (responses declare cacheability), Uniform Interface (standardized resource operations), Layered System (transparent intermediaries), Code-on-Demand (optional client extensions).
2. **Uniform Interface supremacy**: The constraint that differentiates REST from other distributed architectures - resources identified by URIs, manipulated via standard methods (GET, POST, PUT, DELETE), with hypermedia driving application state (HATEOAS).
3. **Statelessness benefits**: Each request contains all needed information, improving reliability (any server can handle any request) and scalability (no server-side session state management).
4. **Cacheability advantages**: Explicit cache control reduces latency and server load while maintaining data consistency.
5. **Layered system flexibility**: Intermediaries (caches, proxies, load balancers) can be inserted without affecting client or server design.
6. **Web architecture alignment**: REST explains why the Web scales - it codifies the architectural principles that made the WWW successful.

## Mechanism

REST works because the Uniform Interface constraint reduces coupling between client and server to a minimum: clients only need to understand media types and standard methods, not server implementation details. Statelessness improves reliability and scalability. For API design, REST implies contracts should be expressed as resource shapes (data structure) and media types (data format), not procedure calls. The contract becomes the resource schema and allowed transitions, not method signatures.

## Relevance

Foundational architecture for web services, APIs, and distributed systems. Essential for understanding modern web architecture, microservices design, and HTTP-based APIs. Critical for system architects designing scalable, maintainable distributed systems. Directly applicable to API design, web service architecture, and system integration patterns.

## Related Research

- (Conway, 1968): Organizational structure implications for REST service boundaries
- (Fowler, 2014): Microservices architecture patterns building on REST principles
