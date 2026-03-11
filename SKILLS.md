# Agente 11 - Habilidades

## Capacidades Principales

### 1. Generación de Boilerplate
- Generar plantillas de código listas para producción para **72+ frameworks**
- Creación automática de estructura de proyectos
- Incluir tests, CI/CD y documentación

### 2. Frameworks Soportados (72)

#### Backend Web (23)
| ID | Framework | Descripción |
|----|-----------|-------------|
| nodejs_express | Node.js Express | Servidor Express con MVC |
| nodejs_fastify | Node.js Fastify | Servidor Fastify rápido |
| nodejs_nest | NestJS | Framework Node.js escalable |
| python_fastapi | Python FastAPI | API moderna Python |
| python_flask | Python Flask | Microframework ligero |
| python_django | Python Django | Framework completo |
| python_aiohttp | Python Aiohttp | Async HTTP |
| go_gin | Go Gin | Framework web Go |
| go_fiber | Go Fiber | Framework Go Express-like |
| go_standard | Go Standard | Servidor HTTP estándar |
| dotnet_aspnet | .NET 8 ASP.NET | Framework Microsoft |
| rust_actix | Rust Actix | Framework Actor |
| rust_axum | Rust Axum | Framework ergonomic |
| rust_warp | Rust Warp | Servidor composable |
| scala_akka | Scala Akka | Framework reactivo |
| scala_play | Scala Play | Framework full-stack |
| java_spring | Java Spring Boot | Framework enterprise |
| kotlin_spring | Kotlin Spring | Spring con Kotlin |
| php_laravel | PHP Laravel | Framework elegante |
| php_symfony | PHP Symfony | Framework reutilizable |
| ruby_rails | Ruby on Rails | Framework full-stack |
| ruby_sinatra | Ruby Sinatra | Microframework |

#### Frontend Web (12)
| ID | Framework | Descripción |
|----|-----------|-------------|
| nextjs_app | Next.js 14 App | React con App Router |
| nextjs_pages | Next.js 14 Pages | React con Pages Router |
| react_cra | React CRA | SPA estándar |
| react_vite | React Vite | React con Vite |
| vue_vite | Vue.js 3 Vite | Vue 3 con Vite |
| vue_nuxt | Nuxt.js | Vue meta-framework |
| svelte_vite | Svelte Vite | Svelte con Vite |
| sveltekit | SvelteKit | Framework full-stack |
| angular | Angular | Framework Google |
| solid_vite | SolidJS Vite | SolidJS con Vite |
| alpine | Alpine.js | JS reactivo ligero |
| htmx | HTMX | Hipermedia moderna |

#### Móvil (8)
| ID | Framework | Descripción |
|----|-----------|-------------|
| flutter | Flutter | UI toolkit multiplataforma |
| react_native | React Native | Apps nativas React |
| expo | Expo | React Native simplificado |
| ionic | Ionic | Apps híbridas |
| capacitor | Capacitor | Apps web nativas |
| kotlin_android | Kotlin Android | App Android nativa |
| swift_ios | Swift iOS | App iOS nativa |
| tauri | Tauri | Desktop con web tech |

#### Blockchain (5)
| ID | Framework | Descripción |
|----|-----------|-------------|
| solidity_hardhat | Solidity Hardhat | Smart contracts |
| solidity_truffle | Solidity Truffle | Smart contracts |
| rust_substrate | Rust Substrate | Blockchain Polkadot |
| solana_rust | Solana Rust | Programas Solana |
| near_rust | NEAR Rust | Smart contracts NEAR |

#### DevOps (11)
| ID | Framework | Descripción |
|----|-----------|-------------|
| docker | Docker | Contenedores |
| docker_compose | Docker Compose | Multi-contenedor |
| kubernetes | Kubernetes | Orquestación K8s |
| helm | Helm | Charts K8s |
| ansible | Ansible | Automatización |
| terraform | Terraform AWS | IaC AWS |
| packer | Packer | Imágenes |
| jenkins | Jenkins Pipeline | CI/CD |
| github_actions | GitHub Actions | CI/CD |
| gitlab_ci | GitLab CI | CI/CD |
| argocd | ArgoCD | GitOps K8s |

#### Cloud (8)
| ID | Framework | Descripción |
|----|-----------|-------------|
| aws_cdk | AWS CDK TS | IaC TypeScript |
| aws_cdk_python | AWS CDK Python | IaC Python |
| aws_sam | AWS SAM | Serverless |
| azure_bicep | Azure Bicep | IaC Azure |
| azure_arm | Azure ARM | IaC Azure |
| gcp_terraform | GCP Terraform | IaC GCP |
| gcp_cloudfunctions | GCP Functions | Functions GCP |
| digitalocean | DigitalOcean | Droplets DO |

#### Base de Datos (5)
| ID | Framework | Descripción |
|----|-----------|-------------|
| postgresql | PostgreSQL | Base de datos |
| mongodb | MongoDB | NoSQL |
| redis | Redis | Cache |
| mysql | MySQL | Base de datos |
| dynamodb | DynamoDB | NoSQL AWS |

### 3. Componentes de Plantilla

Cada plantilla generada incluye:
- **Archivos de Configuración** - package.json, requirements.txt, tsconfig
- **Código Fuente** - Estructura de aplicación funcional
- **Tests** - Jest, Pytest o testing nativo
- **CI/CD** - Workflows de GitHub Actions
- **Documentación** - README.md con instrucciones
- **Entorno** - Archivos .env.example
- **Git** - Patrones .gitignore

### 4. Sistema de Carga Dinámica

- Carga de frameworks desde registro centralizado
- Filtrado por categorías
- Mapeo automático de templates
- Soporte para más de 50 frameworks
