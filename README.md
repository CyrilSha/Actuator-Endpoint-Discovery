Actuator Endpoint Discovery Tool
Spring Boot Actuator is a sub-project of Spring Boot that provides several endpoints for monitoring and managing a Spring Boot application. These endpoints allow developers to check the health of the application, gather metrics, and view configuration information. Actuator also provides features for working with log files and managing the application's runtime environment. It is designed to be easy to use, and can be enabled with minimal configuration. 

Exposing Actuator endpoints can potentially expose sensitive information about your application and its environment, and could also allow unauthorized users to make changes to the application's configuration or runtime environment.
It is generally recommended to expose Actuator endpoints only to trusted parties, such as developers and system administrators, rather than to the general public.

This project is built to discover available and unauthenticated Spring Boot Actuator endpoints on already deployed applications which may be used on apps directly or as part of CI/CD when you need to on-duty check that apps/services were not deployed with unauthenticated actuator and by some reason you cannot do that through config.
