# Agente 11 - Habilidades

## Capacidades Principales

### 1. Generación de Boilerplate
- Generar plantillas de código listas para producción para **108 frameworks**
- Creación automática de estructura de proyectos
- Incluir tests, CI/CD y documentación
- Mejores prácticas y arquitecturas modernas

### 2. Frameworks Soportados (108)

#### Backend Web (38)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| nodejs_express | Node.js Express | Servidor Express MVC | MVC | Jest |
| nodejs_fastify | Node.js Fastify | Servidor Fastify rápido | Route-based | Jest |
| nodejs_nest | NestJS | Framework escalable TS | Modular/DDD | Jest |
| nodejs_koa | Node.js Koa | Koa.js moderno | Middleware | Jest |
| nodejs_hapi | Node.js Hapi | Hapi.js configurable | Plugin-based | Jest |
| python_fastapi | Python FastAPI | API moderna Python | Router/DDD | Pytest |
| python_flask | Python Flask | Microframework ligero | Blueprint | Pytest |
| python_django | Python Django | Framework completo | MVT | Pytest |
| python_aiohttp | Python Aiohttp | Async HTTP | Handler-based | Pytest |
| python_tornado | Python Tornado | Framework async | RequestHandler | Pytest |
| python_starlette | Python Starlette | ASGI framework | Path-based | Pytest |
| go_gin | Go Gin | Framework web Go | Router | Go test |
| go_fiber | Go Fiber | Framework Express-like | Middleware | Go test |
| go_standard | Go Standard | Servidor HTTP | Handler | Go test |
| go_echo | Go Echo | Framework minimalista | Router | Go test |
| go_chi | Go Chi | Router lightweight | Router | Go test |
| dotnet_aspnet | .NET 8 ASP.NET Core | Framework Microsoft | MVC/API | xUnit |
| dotnet_fastEndpoints | .NET FastEndpoints | Minimal API | Endpoint-based | xUnit |
| rust_actix | Rust Actix | Framework Actor | Actor | Rust test |
| rust_axum | Rust Axum | Framework ergonomic | Handler | Rust test |
| rust_warp | Rust Warp | Servidor composable | Filter | Rust test |
| rust_rocket | Rust Rocket | Framework simple | Route | Rust test |
| scala_akka | Scala Akka HTTP | Framework reactivo | Actor | ScalaTest |
| scala_play | Scala Play | Framework full-stack | MVC | ScalaTest |
| java_spring | Java Spring Boot | Framework enterprise | MVC | JUnit |
| java_quarkus | Java Quarkus | Java cloud-native | CDI | JUnit |
| kotlin_spring | Kotlin Spring | Spring con Kotlin | MVC | JUnit |
| kotlin_ktor | Kotlin Ktor | Framework async | Route | JUnit |
| php_laravel | PHP Laravel | Framework elegante | MVC | PHPUnit |
| php_symfony | PHP Symfony | Framework reutilizable | MVC | PHPUnit |
| php_slim | PHP Slim | Microframework | Router | PHPUnit |
| ruby_rails | Ruby on Rails | Framework full-stack | MVC | RSpec |
| ruby_sinatra | Ruby Sinatra | Microframework | Route | RSpec |
| elixir_phoenix | Elixir Phoenix | Framework Elixir web | MVC | ExUnit |
| haskell_servant | Haskell Servant | API type-safe | Type-level | Hspec |
| cpp_rest | C++ REST SDK | C++ async HTTP | Async | Catch2 |
| nim_jester | Nim Jester | Framework Nim web | Route | Unittest |
| dart_aqueduct | Dart Aqueduct | Framework Dart server | Router | Test |

#### Frontend Web (15)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| nextjs_app | Next.js 14 App Router | React con App Router | SSR | Jest |
| nextjs_pages | Next.js 14 Pages | React Pages Router | SSR | Jest |
| nextjs_standalone | Next.js Standalone | Output standalone | SSR | Jest |
| react_cra | React CRA | SPA estándar | SPA | Jest |
| react_vite | React Vite | React con Vite | SPA | Vitest |
| react_remix | React Remix | Full-stack React | SSR/Edge | Jest |
| vue_vite | Vue.js 3 Vite | Vue 3 con Vite | SPA | Vitest |
| vue_nuxt | Nuxt.js 3 | Vue meta-framework | SSR/SSG | Vitest |
| svelte_vite | Svelte Vite | Svelte con Vite | SPA | Vitest |
| sveltekit | SvelteKit | Framework full-stack | SSR/SSG | Vitest |
| angular | Angular 17+ | Framework Google | Component | Jasmine |
| solid_vite | SolidJS Vite | SolidJS con Vite | Signal | Vitest |
| alpine | Alpine.js | JS reactivo ligero | Declarative | None |
| htmx | HTMX | HTML moderno | HATEOAS | None |
| qwik | Qwik | Framework resumable | Resumable | Vitest |

#### Móvil (10)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| flutter | Flutter | UI toolkit multiplataforma | Widget | Flutter Test |
| react_native | React Native | Apps nativas React | Component | Jest |
| expo | Expo SDK 50+ | React Native simplificado | Component | Jest |
| ionic | Ionic 7+ | Apps híbridas | Component | Jest |
| capacitor | Capacitor 5+ | Apps web nativas | Web Native | Jest |
| kotlin_android | Kotlin Android | App Android nativa | MVVM | JUnit |
| kotlin_compose | Jetpack Compose | UI Android | Compose | JUnit |
| swift_ios | SwiftUI iOS | App iOS SwiftUI | SwiftUI | XCTest |
| swift_uiKit | UIKit iOS | App iOS UIKit | MVC/MVVM | XCTest |
| tauri | Tauri 2.0 | Apps desktop/móvil | Web Native | Vitest |

#### Blockchain (8)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| solidity_hardhat | Solidity Hardhat | Smart contracts | Contract | Hardhat Test |
| solidity_truffle | Solidity Truffle | Smart contracts | Contract | Mocha |
| solidity_foundry | Solidity Foundry | Smart contracts | Contract | Forge |
| rust_substrate | Rust Substrate | Blockchain Polkadot | Runtime | Substrate Test |
| solana_rust | Solana Rust | Programas Solana | Program | Solana Test |
| near_rust | NEAR Rust | Smart contracts NEAR | Contract | Near Test |
| algorand_teal | Algorand TEAL | Smart contracts Algorand | TEAL | PyTEAL |
| cardano_smart | Cardano Plutus | Smart contracts Cardano | Plutus | Plutus Test |

#### DevOps / Infra (15)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| docker | Docker | Contenedores | Container | None |
| docker_compose | Docker Compose | Multi-contenedor | Orchestration | None |
| kubernetes | Kubernetes | Orquestación K8s | Declarative | None |
| helm | Helm 3 | Charts Kubernetes | Package | None |
| kustomize | Kustomize | K8s customization | Overlay | None |
| ansible | Ansible | Automatización | Idempotent | Molecule |
| terraform | Terraform AWS | IaC AWS | Declarative | Terratest |
| terragrunt | Terragrunt | Terraform DRY | DRY | Terratest |
| packer | Packer | Imágenes | Immutable | None |
| vault | HashiCorp Vault | Secrets management | Secret Store | None |
| jenkins | Jenkins Pipeline | CI/CD Jenkins | Pipeline | None |
| github_actions | GitHub Actions | CI/CD GitHub | Workflow | None |
| gitlab_ci | GitLab CI | CI/CD GitLab | Pipeline | None |
| argocd | ArgoCD | GitOps Kubernetes | GitOps | None |
| crossplane | Crossplane | Control plane K8s | Control Plane | None |

#### Cloud / IaaS (12)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| aws_cdk | AWS CDK TypeScript | IaC AWS CDK | IaC | CDK Asserts |
| aws_cdk_python | AWS CDK Python | IaC CDK Python | IaC | CDK Asserts |
| aws_cdk_go | AWS CDK Go | IaC CDK Go | IaC | CDK Asserts |
| aws_sam | AWS SAM | Serverless SAM | Serverless | SAM Test |
| aws_cdk_v2 | AWS CDK v2 | CDK v2 stable | IaC | CDK Asserts |
| azure_bicep | Azure Bicep | IaC Azure | IaC | Bicep Test |
| azure_arm | Azure ARM | IaC Azure ARM | IaC | None |
| azure_cd | Azure Developer CLI | Azure Dev CLI | IaC | None |
| gcp_terraform | GCP Terraform | IaC GCP | IaC | Terratest |
| gcp_cloudfunctions | GCP Cloud Functions | Functions 2nd gen | Serverless | GC Test |
| gcp_cloudrun | GCP Cloud Run | Container serverless | Serverless | None |
| digitalocean | DigitalOcean | Droplets DO | IaC | Terratest |

#### Base de Datos (8)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| postgresql | PostgreSQL | Base de datos | RDBMS | None |
| postgresql_timescale | TimescaleDB | Time-series | Time-series | None |
| mongodb | MongoDB | Base de datos | Document | None |
| mongodb_atlas | MongoDB Atlas | MongoDB cloud | Document | None |
| redis | Redis | Cache/Message broker | In-memory | None |
| mysql | MySQL | Base de datos | RDBMS | None |
| dynamodb | DynamoDB | NoSQL AWS | NoSQL | None |
| cockroachdb | CockroachDB | Distributed SQL | Distributed | None |

#### Data / ML (7)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| python_pandas | Python Pandas | Data analysis | Data Frame | Pytest |
| python_pytorch | Python PyTorch | Deep learning | Neural Net | Pytest |
| python_tensorflow | Python TensorFlow | ML TensorFlow | Neural Net | Pytest |
| python_scikit | Scikit-learn | ML clásico | ML | Pytest |
| python_jupyter | Jupyter Notebook | Notebooks | Notebook | None |
| python_mlflow | MLflow | ML lifecycle | MLOps | None |
| python_kafka | Apache Kafka | Event streaming | Event Stream | None |

#### Microservicios / Mesh (5)
| ID | Framework | Descripción | Arquitectura | Testing |
|----|-----------|-------------|--------------|---------|
| grpc | gRPC | RPC framework | IDL-based | Go test |
| graphql | GraphQL Apollo | API GraphQL | Schema-first | Jest |
| istio | Istio | Service mesh K8s | Service Mesh | None |
| envoy | Envoy | Proxy/service mesh | Proxy | None |
| nats | NATS | Messaging system | Pub/Sub | None |

### 3. Componentes de Plantilla

Cada plantilla generada incluye:
- **Archivos de Configuración** - package.json, requirements.txt, tsconfig, pom.xml, etc.
- **Código Fuente** - Estructura de aplicación funcional
- **Tests** - Jest, Pytest, JUnit, Vitest, etc.
- **CI/CD** - GitHub Actions, GitLab CI, Jenkins
- **Documentación** - README.md con instrucciones
- **Entorno** - Archivos .env.example
- **Git** - Patrones .gitignore
- **Docker** - Dockerfile y docker-compose.yml
- **Kubernetes** - Manifiestos K8s cuando aplica

### 4. Arquitecturas Incluidas
- MVC (Model-View-Controller)
- DDD (Domain-Driven Design)
- Modular
- Clean Architecture
- Server-Side Rendering (SSR)
- Static Site Generation (SSG)
- Single Page Application (SPA)
- Microservices
- Event-Driven
- GitOps
- IaC (Infrastructure as Code)
