from typing import Dict


def generate_nodejs_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    options = options or {}
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "description": "Node.js project generated with Boilerplate Agent",
  "main": "src/index.js",
  "scripts": {{
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "lint": "eslint src/"
  }},
  "keywords": [],
  "author": "",
  "license": "MIT",
  "dependencies": {{
    "express": "^4.18.2",
    "dotenv": "^16.3.1",
    "cors": "^2.8.5"
  }},
  "devDependencies": {{
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "eslint": "^8.50.0"
  }}
}}''',
        "src/index.js": """const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {{
  res.json({ message: "Welcome to {0}".format(project_name) });
}});

app.get("/health", (req, res) => {{
  res.json({ status: "ok" });
}});

app.listen(PORT, () => {{
  console.log(`Server running on port ${{PORT}}`);
}});

module.exports = app;
""".format(project_name=project_name),
        "src/routes/example.js": """const router = require("express").Router();

router.get("/", (req, res) => {{
  res.json({{ message: "Example endpoint" }});
}});

module.exports = router;
""",
        "src/controllers/exampleController.js": """const exampleService = require("../services/exampleService");

const getExample = async (req, res) => {{
  try {{
    const data = await exampleService.getData();
    res.json(data);
  }} catch (error) {{
    res.status(500).json({{ error: error.message }});
  }}
}};

module.exports = {{ getExample }};
""",
        "src/services/exampleService.js": """const getData = async () => {{
  return {{ message: "Hello World" }};
}};

module.exports = {{ getData }};
""",
        "tests/example.test.js": """describe("Example Tests", () => {{
  test("should pass", () => {{
    expect(true).toBe(true);
  }});
}});
""",
        ".env.example": """PORT=3000
NODE_ENV=development
""",
        ".gitignore": """node_modules/
.env
.env.local
dist/
build/
*.log
npm-debug.log*
""",
        "README.md": f"""# {project_name}

Node.js project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm run dev
```

## Available Scripts

- `npm start` - Start production server
- `npm run dev` - Start development server
- `npm test` - Run tests
- `npm run lint` - Run ESLint
""",
        "jest.config.js": """module.exports = {{
  testEnvironment: "node",
  testMatch: ["**/tests/**/*.test.js"],
  coverageDirectory: "coverage",
  collectCoverageFrom: ["src/**/*.js"]
}};
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npm ci
      - run: npm test
      - run: npm run lint
""",
    }


def generate_nextjs_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    options = options or {}
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "private": true,
  "scripts": {{
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest"
  }},
  "dependencies": {{
    "next": "14.2.3",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  }},
  "devDependencies": {{
    "typescript": "^5.4.5",
    "@types/node": "^20.12.12",
    "@types/react": "^18.3.2",
    "@types/react-dom": "^18.3.0",
    "eslint": "^8.57.0",
    "eslint-config-next": "14.2.3",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.2.2"
  }}
}}''',
        "next.config.js": """/** @type {import("next").NextConfig} */
const nextConfig = {{
  reactStrictMode: true,
}};

module.exports = nextConfig;
""",
        "tsconfig.json": """{{
  "compilerOptions": {{
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{{ "name": "next" }}],
    "paths": {{ "@/*": ["./src/*"] }}
  }},
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}}""",
        "src/app/layout.tsx": """import type {{ Metadata }} from "next";

export const metadata: Metadata = {{
  title: "{0}",
  description: "Generated with Boilerplate Agent",
}};

export default function RootLayout({{
  children,
}}: {{
  children: React.ReactNode;
}}) {{
  return (
    <html lang="en">
      <body>{{children}}</body>
    </html>
  );
}}
""".format(project_name),
        "src/app/page.tsx": """export default function Home() {{
  return (
    <main>
      <h1>Welcome to {0}</h1>
      <p>Generated with Boilerplate Agent</p>
    </main>
  );
}}
""".format(project_name),
        "src/app/globals.css": """* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}};

body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}};
""",
        ".env.example": """NEXT_PUBLIC_API_URL=http://localhost:3000/api
""",
        ".gitignore": """node_modules/
.next/
out/
.env*.local
*.log
""",
        "README.md": f"""# {project_name}

Next.js project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm run dev
```

## Stack

- Next.js 14 (App Router)
- TypeScript
- Jest for testing
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npm ci
      - run: npm run build
      - run: npm run lint
""",
        "jest.config.js": """import type {{ Config }} from "jest";
import nextJest from "next/jest";

const createJestConfig = nextJest({{ dir: "./" }});

const config: Config = {{
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
  testEnvironment: "jest-environment-jsdom",
}};

export default createJestConfig(config);
""",
        "jest.setup.js": """import "@testing-library/jest-dom";
""",
    }


def generate_python_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    options = options or {}
    return {
        "requirements.txt": """fastapi==0.110.0
uvicorn==0.29.0
python-dotenv==1.0.0
pydantic==2.6.0
pytest==8.1.1
httpx==0.27.0
""",
        "src/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="{0}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {{"message": "Welcome to {0}"}}

@app.get("/health")
def health_check():
    return {{"status": "ok"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
""".format(project_name),
        "src/routes/example.py": """from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["example"])

@router.get("/")
def get_example():
    return {{"message": "Example endpoint"}}
""",
        "src/models/schemas.py": """from pydantic import BaseModel

class Example(BaseModel):
    id: int
    name: str
    description: str | None = None
""",
        "src/services/example_service.py": """async def get_data():
    return {{"message": "Hello World"}}
""",
        "tests/test_main.py": """import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
""",
        ".env.example": """PORT=8000
DEBUG=true
""",
        ".gitignore": """__pycache__/
*.py[cod]
*$py.class
.env
.venv
venv/
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
htmlcov/
""",
        "pytest.ini": """[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
""",
        "README.md": f"""# {project_name}

FastAPI project generated with Boilerplate Agent.

## Getting Started

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Testing

```bash
pytest
```
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest
""",
    }


def generate_go_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "go.mod": f"""module {project_name}

go 1.21
""",
        "main.go": f"""package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func main() {{
    port := os.Getenv("PORT")
    if port == "" {{
        port = "8080"
    }}

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {{
        fmt.Fprintf(w, "Welcome to {0}")
    }})

    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {{
        w.Header().Set("Content-Type", "application/json")
        fmt.Fprintf(w, `{{"status": "ok"}}`)
    }})

    log.Printf("Server starting on port %s", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}}
""".format(project_name=project_name),
        "handlers/example.go": """package handlers

import (
    "encoding/json"
    "net/http"
)

func ExampleHandler(w http.ResponseWriter, r *http.Request) {{
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{{
        "message": "Hello World",
    }})
}}
""",
        ".env.example": """PORT=8080
""",
        ".gitignore": """*.exe
*.exe~
*.dll
*.so
*.dylib
*.test
*.out
go.work
.env
""",
        "README.md": f"""# {project_name}

Go project generated with Boilerplate Agent.

## Getting Started

```bash
go run main.go
```

## Build

```bash
go build -o {project_name} main.go
```
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.21"
      - name: Build
        run: go build -o main .
      - name: Test
        run: go test ./...
""",
    }


def generate_typescript_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "main": "dist/index.js",
  "scripts": {{
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node src/index.ts",
    "test": "jest",
    "lint": "eslint src/**/*.ts"
  }},
  "dependencies": {{}},
  "devDependencies": {{
    "typescript": "^5.4.5",
    "@types/node": "^20.12.12",
    "ts-node": "^10.9.2",
    "jest": "^29.7.0",
    "@types/jest": "^29.5.12",
    "ts-jest": "^29.1.2",
    "eslint": "^8.57.0",
    "@typescript-eslint/parser": "^7.10.0",
    "@typescript-eslint/eslint-plugin": "^7.10.0"
  }}
}}''',
        "tsconfig.json": """{{
  "compilerOptions": {{
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true
  }},
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}}""",
        "src/index.ts": f"""console.log("Welcome to {0}");

export function example(): string {{
  return "Hello World";
}}
""".format(project_name),
        "src/example.ts": """export function hello(): string {
  return "Hello";
}
""",
        "tests/example.test.ts": """import {{ example }} from "../src/example";

describe("Example Tests", () => {
  test("should return hello world", () => {
    expect(example()).toBe("Hello World");
  });
});
""",
        "jest.config.js": """module.exports = {
  preset: "ts-jest",
  testEnvironment: "node",
  roots: ["<rootDir>/tests"],
  testMatch: ["**/*.test.ts"],
};""",
        ".gitignore": """node_modules/
dist/
.env
*.log
""",
        "README.md": f"""# {project_name}

TypeScript project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm run build
npm start
```
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npm ci
      - run: npm test
      - run: npm run build
""",
    }


def generate_rust_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "Cargo.toml": f'''[package]
name = "{project_name}"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = {{ version = "1.0", features = ["derive"] }}
serde_json = "1.0"
tokio = {{ version = "1", features = ["full"] }}
''',
        "src/main.rs": f"""#[cfg_attr(mobile, tauri::mobile_entry_point)]
fn main() {{
    println!("Welcome to {0}!");
}}
""".format(project_name),
        "src/lib.rs": f"""pub fn example() -> String {{
    "Hello World".to_string()
}}

#[cfg(test)]
mod tests {{
    use super::*;

    #[test]
    fn test_example() {{
        assert_eq!(example(), "Hello World");
    }}
}}
""",
        ".gitignore": """target/
Cargo.lock
.env
""",
        "README.md": f"""# {project_name}

Rust project generated with Boilerplate Agent.

## Getting Started

```bash
cargo build
cargo run
cargo test
```
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          profile: minimal
          toolchain: stable
      - name: Run tests
        run: cargo test
      - name: Build
        run: cargo build --release
""",
    }


def generate_dotnet_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        f"{project_name}.csproj": f"""<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.5.0" />
  </ItemGroup>

</Project>
""",
        "Program.cs": f"""var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{{
    app.UseSwagger();
    app.UseSwaggerUI();
}}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
""",
        "Controllers/ExampleController.cs": """using Microsoft.AspNetCore.Mvc;

namespace {0}.Controllers;

[ApiController]
[Route("[controller]")]
public class ExampleController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
""".format(project_name.replace("-", "")),
        "appsettings.json": """{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
""",
        "appsettings.Development.json": """{
  "Logging": {
    "LogLevel": {
      "Default": "Debug"
    }
  }
}
""",
        ".gitignore": """bin/
obj/
*.user
*.suo
.vs/
.env
""",
        "README.md": f"""# {project_name}

.NET 8 project generated with Boilerplate Agent.

## Getting Started

```bash
dotnet restore
dotnet run
```
""",
        ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: "8.0.x"
      - name: Restore
        run: dotnet restore
      - name: Build
        run: dotnet build
      - name: Test
        run: dotnet test
""",
    }


def generate_docker_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "Dockerfile": f"""FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]
""",
        "docker-compose.yml": f"""version: "3.8"

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
""",
        "nginx.conf": """events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://app:3000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
}
""",
        ".dockerignore": """node_modules/
.git
*.md
.env
""",
        "README.md": f"""# {project_name}

Docker setup generated with Boilerplate Agent.

## Getting Started

```bash
docker-compose up -d
```
""",
    }


def generate_kubernetes_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "deployment.yaml": f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {project_name}
  labels:
    app: {project_name}
spec:
  replicas: 3
  selector:
    matchLabels:
      app: {project_name}
  template:
    metadata:
      labels:
        app: {project_name}
    spec:
      containers:
      - name: {project_name}
        image: {project_name}:latest
        ports:
        - containerPort: 3000
        resources:
          limits:
            cpu: "500m"
            memory: "256Mi"
          requests:
            cpu: "200m"
            memory: "128Mi"
""",
        "service.yaml": f"""apiVersion: v1
kind: Service
metadata:
  name: {project_name}
spec:
  selector:
    app: {project_name}
  ports:
  - port: 80
    targetPort: 3000
  type: LoadBalancer
""",
        "ingress.yaml": f"""apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {project_name}
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: {project_name}.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: {project_name}
            port:
              number: 80
""",
        "configmap.yaml": f"""apiVersion: v1
kind: ConfigMap
metadata:
  name: {project_name}-config
data:
  NODE_ENV: "production"
  LOG_LEVEL: "info"
""",
        "secret.yaml": """apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  API_KEY: "your-api-key-here"
""",
        "README.md": f"""# {project_name}

Kubernetes manifests generated with Boilerplate Agent.

## Deploy

```bash
kubectl apply -f .
```
""",
    }


def generate_ansible_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "inventory.ini": """[webservers]
server1.example.com
server2.example.com

[databases]
db.example.com
""",
        "ansible.cfg": """[defaults]
inventory = inventory.ini
remote_user = admin
host_key_checking = False
""",
        "playbook.yml": """---
- name: Deploy Application
  hosts: webservers
  become: yes
  vars:
    app_dir: /opt/app
    app_port: 3000

  tasks:
    - name: Ensure app directory exists
      file:
        path: "{{ app_dir }}"
        state: directory

    - name: Deploy application files
      synchronize:
        src: ./
        dest: "{{ app_dir }}/"
        delete: yes

    - name: Install dependencies
      command: npm install
      args:
        chdir: "{{ app_dir }}"

    - name: Start application
      systemd:
        name: app
        state: restarted
        daemon_reload: yes

    - name: Configure firewall
      firewalld:
        service: http
        permanent: yes
        state: enabled
""",
        "roles/app/tasks/main.yml": """---
- name: Create app user
  user:
    name: appuser
    system: yes

- name: Setup application directory
  file:
    path: /opt/{{ app_name }}
    owner: appuser
    group: appuser
    state: directory
""",
        "roles/app/handlers/main.yml": """---
- name: restart app
  systemd:
    name: app
    state: restarted
""",
        "roles/app/templates/config.j2": """PORT={{ app_port }}
NODE_ENV=production
""",
        "README.md": f"""# {project_name}

Ansible playbook generated with Boilerplate Agent.

## Run

```bash
ansible-playbook playbook.yml
```
""",
    }


def generate_aws_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "cdk.json": """{{
  "app": "npx ts-node bin/{0}.ts",
  "context": {{
    "@aws-cdk/core:newStyleStackSynthesis": true
  }}
}}
""".format(project_name),
        "bin/app.ts": f'''#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import {{ MainStack }} from "../lib/main-stack";

const app = new cdk.App();
new MainStack(app, "{0}", {{}});
'''.format(project_name),
        "lib/main-stack.ts": """import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import { Construct } from "constructs";

export class MainStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "VPC", {{
      maxAzs: 2
    }});

    const cluster = new ecs.Cluster(this, "Cluster", {{
      vpc
    }});
  }
}
""",
        "package.json": """{{
  "name": "{0}",
  "version": "1.0.0",
  "scripts": {{
    "build": "tsc",
    "deploy": "cdk deploy",
    "destroy": "cdk destroy"
  }},
  "dependencies": {{
    "aws-cdk-lib": "^2.140.0",
    "constructs": "^10.3.0"
  }},
  "devDependencies": {{
    "@types/node": "^20.12.12",
    "aws-cdk": "^2.140.0",
    "typescript": "^5.4.5"
  }}
}}
""".format(project_name),
        "tsconfig.json": """{{
  "compilerOptions": {{
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "strict": true,
    "esModuleInterop": true
  }}
}}
""",
        "README.md": f"""# {project_name}

AWS CDK project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
cdk deploy
```
""",
    }


def generate_azure_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "main.bicep": f"""targetScope = \'resourceGroup\'

param location string = resourceGroup().location

param appServicePlanName string = \'{project_name}-asp\'
param webAppName string = \'{project_name}-app\'

resource appServicePlan \'Microsoft.Web/serverfarms@2022-09-01\' = {{
  name: appServicePlanName
  location: location
  sku: {{
    name: \'B1\'
    capacity: 1
  }}
}}

resource webApp \'Microsoft.Web/sites@2022-09-01\' = {{
  name: webAppName
  location: location
  identity: {{
    type: \'SystemAssigned\'
  }}
  properties: {{
    serverFarmId: appServicePlan.id
    httpsOnly: true
  }}
}}

output webAppUrl string = webApp.properties.defaultHostName
""",
        "azuredeploy.parameters.json": """{{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {{
    "location": {{
      "value": "eastus"
    }}
  }}
}}
""",
        ".github/workflows/deploy.yml": f"""name: Deploy to Azure

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      
      - name: Deploy to Azure
        uses: azure/arm-deploy@v1
        with:
          resourceGroupName: {project_name}-rg
          template: main.bicep
""",
        "README.md": f"""# {project_name}

Azure Bicep project generated with Boilerplate Agent.

## Deploy

```bash
az deployment group create --template-file main.bicep
```
""",
    }


def generate_gcp_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "main.tf": f'''provider "google" {{
  project = "{project_name}"
  region  = "us-central1"
}}

resource "google_compute_instance" "vm" {{
  name         = "{project_name}-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {{
    initialize_params {{
      image = "debian-cloud/debian-11"
    }}
  }}

  network_interface {{
    network = "default"
    access_config {{
      // Ephemeral IP
    }}
  }}
}}
''',
        "variables.tf": """variable "project" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-central1"
}
""",
        "outputs.tf": """output "vm_ip" {
  value = google_compute_instance.vm.network_interface.0.access_config.0.nat_ip
}
""",
        ".terraform.lock": """# This file is maintained by Terraform
""",
        "README.md": f"""# {project_name}

GCP Terraform project generated with Boilerplate Agent.

## Getting Started

```bash
terraform init
terraform plan
terraform apply
```
""",
    }


def generate_terraform_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "main.tf": f'''terraform {{
  required_version = ">= 1.0"

  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
}}

resource "aws_s3_bucket" "app" {{
  bucket = "{project_name}-\({{terraform.workspace}})"
}}

resource "aws_ec2_instance" "app" {{
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {{
    Name = "{project_name}"
  }}
}}
''',
        "variables.tf": """variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}
""",
        "outputs.tf": """output "instance_id" {
  value = aws_ec2_instance.app.id
}
""",
        ".gitignore": """.terraform/
*.tfstate
*.tfstate.backup
""",
        "README.md": f"""# {project_name}

Terraform project generated with Boilerplate Agent.

## Getting Started

```bash
terraform init
terraform plan
terraform apply
```
""",
    }


def generate_solidity_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "contracts/Example.sol": f'''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract {project_name.replace("-", "").replace("_", "")} {{
    string public name = "{project_name}";
    string public symbol = "{project_name[:3].upper()}";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000 * 10 ** uint256(decimals);

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() {{
        balanceOf[msg.sender] = totalSupply;
    }}

    function transfer(address to, uint256 value) public returns (bool) {{
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }}

    function approve(address spender, uint256 value) public returns (bool) {{
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }}
}}
''',
        "scripts/deploy.js": f'''const hre = require("hardhat");

async function main() {{
  const Contract = await hre.ethers.getContractFactory("{project_name.replace("-", "").replace("_", "")}");
  const contract = await Contract.deploy();
  await contract.waitForDeployment();
  console.log("Deployed to:", await contract.getAddress());
}}

main()
  .then(() => process.exit(0))
  .catch((error) => {{
    console.error(error);
    process.exit(1);
  }});
''',
        "hardhat.config.js": f"""require("@nomicfoundation/hardhat-toolbox");

module.exports = {{
  solidity: "0.8.19",
  networks: {{
    sepolia: {{
      url: process.env.SEPOLIA_URL,
      accounts: [process.env.PRIVATE_KEY]
    }}
  }}
}};
""",
        "package.json": """{{
  "name": "{0}",
  "version": "1.0.0",
  "devDependencies": {{
    "@nomicfoundation/hardhat-toolbox": "^5.0.0",
    "@nomiclabs/hardhat-ethers": "^2.2.3",
    "ethers": "^6.12.0",
    "hardhat": "^2.20.0"
  }}
}}
""".format(project_name),
        ".env.example": """SEPOLIA_URL=https://sepolia.infura.io/v3/YOUR_INFURA_KEY
PRIVATE_KEY=your-private-key-here
""",
        "README.md": f"""# {project_name}

Solidity smart contract generated with Boilerplate Agent.

## Deploy

```bash
npx hardhat run scripts/deploy.js --network sepolia
```
""",
    }


def generate_react_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "private": true,
  "dependencies": {{
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-scripts": "5.0.1"
  }},
  "scripts": {{
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }},
  "browserslist": {{
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  }}
}}
''',
        "src/index.js": """import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
""",
        "src/App.js": """function App() {
  return (
    <div className="App">
      <h1>Welcome</h1>
    </div>
  );
}

export default App;
""",
        "src/index.css": """* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
""",
        "public/index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
""",
        ".gitignore": """node_modules/
build/
.env
""",
        "README.md": f"""# {project_name}

React project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm start
```
""",
    }


def generate_vue_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "dependencies": {{
    "vue": "^3.4.21"
  }},
  "devDependencies": {{
    "@vitejs/plugin-vue": "^5.0.4",
    "vite": "^5.2.0"
  }}
}}
''',
        "vite.config.js": """import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
});
""",
        "index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
""",
        "src/main.js": """import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
""",
        "src/App.vue": """<template>
  <div>
    <h1>Welcome</h1>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>
""",
        "README.md": f"""# {project_name}

Vue.js project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm run dev
```
""",
    }


def generate_svelte_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "scripts": {{
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "devDependencies": {{
    "@sveltejs/vite-plugin-svelte": "^3.1.0",
    "svelte": "^4.2.12",
    "vite": "^5.2.0"
  }}
}}
''',
        "vite.config.js": """import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

export default defineConfig({
  plugins: [svelte()],
});
""",
        "svelte.config.js": """import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

export default {
  preprocess: vitePreprocess(),
};
""",
        "index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Svelte App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
""",
        "src/main.js": """import App from "./App.svelte";

const app = new App({
  target: document.getElementById("app"),
});

export default app;
""",
        "src/App.svelte": """<script>
</script>

<main>
  <h1>Welcome</h1>
</main>

<style>
</style>
""",
        "README.md": f"""# {project_name}

Svelte project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm run dev
```
""",
    }


def generate_flutter_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "pubspec.yaml": f"""name: {project_name.replace("-", "_")}
description: "Flutter project generated with Boilerplate Agent"

publish_to: "none"

version: 1.0.0+1

environment:
  sdk: ">=3.0.0 <4.0.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
""",
        "lib/main.dart": """import "package:flutter/material.dart";

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Flutter Demo",
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Home")),
      body: const Center(child: Text("Welcome")),
    );
  }
}
""",
        "lib/screens/home_screen.dart": """import "package:flutter/material.dart";

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text("{0}"),
      ),
    );
  }
}
""".format(project_name),
        ".gitignore": """.dart_tool/
.packages
.pub/
build/
.idea/
.vscode/
*.iml
""",
        "README.md": f"""# {project_name}

Flutter project generated with Boilerplate Agent.

## Getting Started

```bash
flutter pub get
flutter run
```
""",
    }


def generate_react_native_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "package.json": f'''{{
  "name": "{project_name}",
  "version": "1.0.0",
  "scripts": {{
    "start": "react-native start",
    "android": "react-native run-android",
    "ios": "react-native run-ios"
  }},
  "dependencies": {{
    "react": "18.3.1",
    "react-native": "0.74.2"
  }},
  "devDependencies": {{
    "@react-native-community/cli": "14.0.0"
  }}
}}
''',
        "App.tsx": """import React from "react";
import { View, Text } from "react-native";

const App = () => {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>Welcome</Text>
    </View>
  );
};

export default App;
""",
        "index.js": """import { AppRegistry } from "react-native";
import App from "./App";
import { name as appName } from "./app.json";

AppRegistry.registerComponent(appName, () => App);
""",
        "app.json": f'''{{
  "name": "{project_name}",
  "displayName": "{project_name}"
}}
''',
        ".gitignore": """node_modules/
*.log
ios/build/
android/build/
""",
        "README.md": f"""# {project_name}

React Native project generated with Boilerplate Agent.

## Getting Started

```bash
npm install
npm start
npm run android
```
""",
    }


def generate_postgres_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "init.sql": """-- PostgreSQL Database Setup
-- Generated with Boilerplate Agent

-- Create database
CREATE DATABASE app_db;

-- Connect to database
\\c app_db;

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example table
CREATE TABLE examples (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);

-- Insert sample data
INSERT INTO examples (name, description) VALUES 
    ('Example 1', 'Sample description 1'),
    ('Example 2', 'Sample description 2');
""",
        "docker-compose.yml": f"""version: "3.8"

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppassword
      POSTGRES_DB: app_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres_data:
""",
        ".env.example": """POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=app_db
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppassword
""",
        "README.md": f"""# {project_name}

PostgreSQL setup generated with Boilerplate Agent.

## Getting Started

```bash
docker-compose up -d
```
""",
    }


def generate_scala_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "build.sbt": f'''name := "{project_name}"

version := "0.1"

scalaVersion := "2.13.12"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-http" % "10.6.3",
  "com.typesafe.akka" %% "akka-http-spray-json" % "10.6.3"
)
''',
        "src/main/scala/Main.scala": f'''package {project_name.replace("-", "_")}

import akka.http.scaladsl.Http
import akka.http.scaladsl.model._
import akka.http.scaladsl.server.Directives._
import akka.actor.typed.ActorSystem
import akka.http.scaladsl.server.Route
import scala.concurrent.ExecutionContext

object Main extends App {{
  implicit val system = ActorSystem(Behaviors.empty, "{project_name}")
  implicit val ec: ExecutionContext = system.executionContext

  val route: Route = pathPrefix("api") {{
    path("health") {{
      get {{
        complete(StatusCodes.OK, Map("status" -> "ok"))
      }}
    }} ~ path("example") {{
      get {{
        complete(Map("message" -> "Hello World"))
      }}
    }}
  }}

  Http().newServerAt("0.0.0.0", 8080).bind(route)
  println("Server started on port 8080")
}}
''',
        "build.gradle": f"""plugins {{
    id "scala"
}}

repositories {{
    mavenCentral()
}}

dependencies {{
    implementation "org.scala-lang:scala-library:2.13.12"
    implementation "com.typesafe.akka:akka-http_2.13:10.6.3"
}}
""",
        ".gitignore": """target/
.idea/
*.iml
""",
        "README.md": f"""# {project_name}

Scala project generated with Boilerplate Agent.

## Getting Started

```bash
sbt run
```
""",
    }


def generate_mongodb_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "docker-compose.yml": f"""version: "3.8"

services:
  mongodb:
    image: mongo:7
    container_name: {project_name}
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: password
    volumes:
      - mongodb_data:/data/db
      - ./init.js:/docker-entrypoint-initdb.d/init.js:ro

volumes:
  mongodb_data:
""",
        "init.js": """db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "readWrite", db: "app_db" }]
});

db.createCollection("examples");
""",
        ".env.example": """MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DB=app_db
MONGO_USER=admin
MONGO_PASSWORD=password
""",
        "README.md": f"""# {project_name}

MongoDB setup generated with Boilerplate Agent.

## Getting Started

```bash
docker-compose up -d
```
""",
    }


def generate_redis_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "docker-compose.yml": f"""version: "3.8"

services:
  redis:
    image: redis:7-alpine
    container_name: {project_name}
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

volumes:
  redis_data:
""",
        ".env.example": """REDIS_HOST=localhost
REDIS_PORT=6379
""",
        "README.md": f"""# {project_name}

Redis setup generated with Boilerplate Agent.

## Getting Started

```bash
docker-compose up -d
```
""",
    }


def generate_mysql_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "docker-compose.yml": f"""version: "3.8"

services:
  mysql:
    image: mysql:8
    container_name: {project_name}
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: app_db
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppassword
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
""",
        "init.sql": """CREATE TABLE IF NOT EXISTS examples (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO examples (name, description) VALUES 
    ('Example 1', 'Sample description 1'),
    ('Example 2', 'Sample description 2');
""",
        ".env.example": """MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=app_db
MYSQL_USER=appuser
MYSQL_PASSWORD=apppassword
""",
        "README.md": f"""# {project_name}

MySQL setup generated with Boilerplate Agent.
""",
    }


def generate_k8s_helm(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "Chart.yaml": f"""apiVersion: v2
name: {project_name}
description: A Helm chart for {project_name}
type: application
version: 0.1.0
appVersion: "1.0"
""",
        "values.yaml": """replicaCount: 1

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "latest"

service:
  type: LoadBalancer
  port: 80

ingress:
  enabled: false
  className: ""
  annotations: {}
  hosts:
    - host: chart-example.local
      paths:
        - path: /
          pathType: ImplementationSpecific

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
""",
        "templates/deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ .Chart.Name }}
      app.kubernetes.io/instance: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ .Chart.Name }}
        app.kubernetes.io/instance: {{ .Release.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
""",
        "templates/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app.kubernetes.io/name: {{ .Chart.Name }}
    app.kubernetes.io/instance: {{ .Release.Name }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
""",
        "README.md": f"""# {project_name}

Helm chart generated with Boilerplate Agent.
""",
    }


def generate_k8s_argo(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "application.yaml": f"""apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {project_name}
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/repo.git
    targetRevision: HEAD
    path: .
  destination:
    server: https://kubernetes.default.svc
    namespace: {project_name}
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
""",
        "README.md": f"""# {project_name}

ArgoCD application generated with Boilerplate Agent.
""",
    }


def generate_github_actions_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        ".github/workflows/main.yml": f"""name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build
        run: echo "Building..."
      
      - name: Test
        run: echo "Testing..."
""",
        "README.md": f"""# {project_name}

GitHub Actions workflow generated with Boilerplate Agent.
""",
    }


def generate_gitlab_ci_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        ".gitlab-ci.yml": f"""stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - echo "Building..."

test:
  stage: test
  script:
    - echo "Testing..."

deploy:
  stage: deploy
  script:
    - echo "Deploying..."
  only:
    - main
""",
        "README.md": f"""# {project_name}

GitLab CI pipeline generated with Boilerplate Agent.
""",
    }


def generate_jenkins_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "Jenkinsfile": f"""pipeline {{
    agent any
    
    stages {{
        stage('Build') {{
            steps {{
                echo 'Building...'
            }}
        }}
        
        stage('Test') {{
            steps {{
                echo 'Testing...'
            }}
        }}
        
        stage('Deploy') {{
            steps {{
                echo 'Deploying...'
            }}
        }}
    }}
}}
""",
        "README.md": f"""# {project_name}

Jenkins pipeline generated with Boilerplate Agent.
""",
    }


def generate_ml_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "requirements.txt": """numpy==1.26.0
pandas==2.2.0
scikit-learn==1.4.0
mlflow==2.12.0
""",
        "src/train.py": """import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train():
    mlflow.start_run()
    
    data = pd.read_csv("data.csv")
    X = data.drop("target", axis=1)
    y = data["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
    
    mlflow.end_run()

if __name__ == "__main__":
    train()
""",
        "README.md": f"""# {project_name}

ML project generated with Boilerplate Agent.

## Getting Started

```bash
pip install -r requirements.txt
python src/train.py
```
""",
    }


def generate_kafka_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "docker-compose.yml": """version: "3.8"

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
""",
        "producer.py": """from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

producer.send("topic", {"key": "value"})
producer.flush()
""",
        "consumer.py": """from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "topic",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    print(message.value)
""",
        "README.md": f"""# {project_name}

Kafka setup generated with Boilerplate Agent.
""",
    }


def generate_nats_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "docker-compose.yml": """version: "3.8"

services:
  nats:
    image: nats:2.10
    ports:
      - "4222:4222"
      - "8222:8222"
""",
        "publisher.py": """import nats

async def publish():
    nc = await nats.connect()
    await nc.publish("subject", b"Hello NATS")
    await nc.close()

import asyncio
asyncio.run(publish())
""",
        "subscriber.py": """import nats

async def subscribe():
    nc = await nats.connect()
    sub = await nc.subscribe("subject")
    async for msg in sub.messages:
        print(msg.data)
    await nc.close()

import asyncio
asyncio.run(subscribe())
""",
        "README.md": f"""# {project_name}

NATS setup generated with Boilerplate Agent.
""",
    }


def generate_envoy_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "envoy.yaml": """static_resources:
  listeners:
    - name: listener_0
      address:
        socket_address:
          address: 0.0.0.0
          port_value: 80
      filter_chains:
        - filters:
            - name: envoy.filters.network.http_connection_manager
              typed_config:
                "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                stat_prefix: ingress_http
                route_config:
                  name: local_route
                  virtual_hosts:
                    - name: local_service
                      domains: ["*"]
                      routes:
                        - match:
                            prefix: "/"
                          route:
                            cluster: service

  clusters:
    - name: service
      connect_timeout: 0.25s
      type: STATIC
      lb_policy: ROUND_ROBIN
      load_assignment:
        cluster_name: service
        endpoints:
          - lb_endpoints:
              - endpoint:
                  address:
                    socket_address:
                      address: 127.0.0.1
                      port_value: 8080
""",
        "Dockerfile": """FROM envoyproxy/envoy:v1.30.0
COPY envoy.yaml /etc/envoy/envoy.yaml
CMD ["envoy", "-c", "/etc/envoy/envoy.yaml"]
""",
        "README.md": f"""# {project_name}

Envoy proxy configuration generated with Boilerplate Agent.
""",
    }


def generate_istio_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "virtual-service.yaml": """apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: {project_name}
spec:
  hosts:
    - {project_name}
  http:
    - route:
        - destination:
            host: {project_name}
            port:
              number: 80
""",
        "destination-rule.yaml": """apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: {project_name}
spec:
  host: {project_name}
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http2MaxRequests: 1000
""",
        "README.md": f"""# {project_name}

Istio service mesh configuration generated with Boilerplate Agent.
""",
    }


def generate_crossplane_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "provider.yaml": """apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws
spec:
  package: xpkg.upbound.io/upbound/provider-aws:v0.47.0
""",
        "composition.yaml": """apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: {project_name}
spec:
  resources: []
""",
        "README.md": f"""# {project_name}

Crossplane configuration generated with Boilerplate Agent.
""",
    }


def generate_vault_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "docker-compose.yml": """version: "3.8"

services:
  vault:
    image: vault:1.15
    ports:
      - "8200:8200"
    environment:
      VAULT_DEV_ROOT_TOKEN_ID: root
    cap_add:
      - IPC_LOCK
""",
        "policy.hcl": """path "secret/data/*" {
  capabilities = ["create", "read", "update", "delete"]
}
""",
        "README.md": f"""# {project_name}

HashiCorp Vault setup generated with Boilerplate Agent.
""",
    }


def generate_terragrunt_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "terragrunt.hcl": """terraform {
  source = "..//modules/example"
}

inputs = {
  name = "{project_name}"
}
""",
        "modules/example/main.tf": """variable "name" {
  description = "Name for resources"
  type        = string
}

resource "aws_s3_bucket" "example" {
  bucket = var.name
}
""",
        "README.md": f"""# {project_name}

Terragrunt configuration generated with Boilerplate Agent.
""",
    }


def generate_packer_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "example.packer.hcl": f"""source "amazon-ebs" "example" {{
  ami_name      = "{project_name}"
  instance_type = "t2.micro"
  region        = "us-east-1"

  source_ami    = "ami-0c55b159cbfafe1f0"
  ssh_username  = "ubuntu"
}}

build {{
  sources = ["source.amazon-ebs.example"]

  provisioner "shell" {{
    inline = ["echo Hello from Packer"]
  }}
}}
""",
        "README.md": f"""# {project_name}

Packer template generated with Boilerplate Agent.
""",
    }


def generate_kustomize_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "kustomization.yaml": f"""apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
""",
        "deployment.yaml": f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {project_name}
spec:
  replicas: 3
  selector:
    matchLabels:
      app: {project_name}
  template:
    metadata:
      labels:
        app: {project_name}
    spec:
      containers:
        - name: app
          image: nginx:latest
""",
        "service.yaml": f"""apiVersion: v1
kind: Service
metadata:
  name: {project_name}
spec:
  selector:
    app: {project_name}
  ports:
    - port: 80
      targetPort: 80
""",
        "overlays/production/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
  - ../../base

replicas:
  - name: app
    count: 5
""",
        "README.md": f"""# {project_name}

Kustomize configuration generated with Boilerplate Agent.
""",
    }


def generate_terraform_module(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "main.tf": f"""variable "name" {{
  description = "Name for {project_name}"
  type        = string
}}

resource "aws_s3_bucket" "app" {{
  bucket = var.name
}}
""",
        "variables.tf": """variable "tags" {
  description = "Tags to apply"
  type        = map(string)
  default     = {}
}
""",
        "outputs.tf": """output "bucket_name" {
  description = "S3 Bucket name"
  value       = aws_s3_bucket.app.id
}
""",
        "README.md": f"""# {project_name}

Terraform module generated with Boilerplate Agent.
""",
    }


def generate_java_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "pom.xml": f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>{project_name}</artifactId>
    <version>1.0.0</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
    </parent>
</project>
""",
        "src/main/java/com/example/App.java": """package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
""",
        "src/main/resources/application.properties": """server.port=8080
""",
        "README.md": f"""# {project_name}

Java Spring Boot project generated with Boilerplate Agent.
""",
    }


def generate_kotlin_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "build.gradle.kts": f"""plugins {{
    id("org.springframework.boot") version "3.2.0"
    id("org.jetbrains.kotlin.jvm") version "1.9.21"
}}

group = "com.example"
version = "1.0.0"

repositories {{
    mavenCentral()
}}

dependencies {{
    implementation("org.springframework.boot:spring-boot-starter-web")
}}
""",
        "src/main/kotlin/com/example/Application.kt": """package com.example

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication

@SpringBootApplication
class Application

fun main(args: Array<String>) {{
    SpringApplication.run(Application::class.java, *args)
}}
""",
        "src/main/resources/application.properties": """server.port=8080
""",
        "README.md": f"""# {project_name}

Kotlin Spring Boot project generated with Boilerplate Agent.
""",
    }


def generate_php_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "composer.json": f"""{{
    "name": "app/{project_name}",
    "require": {{
        "php": "^8.1"
    }},
    "autoload": {{
        "psr-4": {{
            "App\\\\": "src/"
        }}
    }}
}}
""",
        "public/index.php": """<?php

require_once __DIR__ . '/../vendor/autoload.php';

$app = new Slim\\App();

$app->get('/', function ($request, $response) {{
    $response->getBody()->write('Hello World');
    return $response;
}});

$app->run();
""",
        "README.md": f"""# {project_name}

PHP project generated with Boilerplate Agent.
""",
    }


def generate_ruby_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "Gemfile": f"""source 'https://rubygems.org'

gem 'sinatra'
gem 'puma'
""",
        "app.rb": f"""require 'sinatra'

get '/' do
  'Hello World!'
end
""",
        "config.ru": f"""require './app'
run Sinatra::Application
""",
        "README.md": f"""# {project_name}

Ruby Sinatra project generated with Boilerplate Agent.
""",
    }


def generate_angular_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "angular.json": f"""{{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {{
    "{project_name}": {{
      "projectType": "application",
      "root": "",
      "sourceRoot": "src",
      "prefix": "app"
    }}
  }}
}}
""",
        "src/main.ts": """import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, {
  providers: []
});
""",
        "src/app/app.component.ts": """import { Component } from '@angular/core';

@Component({{
  selector: 'app-root',
  template: `<h1>Hello World</h1>`
}})
export class AppComponent {{}}
""",
        "package.json": """{{
  "name": "angular-app",
  "scripts": {{
    "start": "ng serve"
  }}
}}
""",
        "README.md": f"""# {project_name}

Angular project generated with Boilerplate Agent.
""",
    }


def generate_alpine_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alpine.js App</title>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body x-data="{{ message: 'Hello World' }}">
    <h1 x-text="message"></h1>
</body>
</html>
""",
        "README.md": f"""# {project_name}

Alpine.js project generated with Boilerplate Agent.
""",
    }


def generate_htmx_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTMX App</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body>
    <button hx-get="/hello" hx-swap="outerHTML">Click Me</button>
</body>
</html>
""",
        "server.py": """from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<span>Hello World</span>')

HTTPServer(('localhost', 8000), Handler).serve_forever()
""",
        "README.md": f"""# {project_name}

HTMX project generated with Boilerplate Agent.
""",
    }


def generate_ionic_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "package.json": f"""{{
  "name": "{project_name}",
  "version": "1.0.0",
  "dependencies": {{
    "@ionic/react": "^7.0.0"
  }}
}}
""",
        "src/App.tsx": """import {{ IonApp, IonContent, IonHeader, IonTitle, IonToolbar }} from '@ionic/react';

function App() {{
  return (
    <IonApp>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Hello</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <h1>Hello World</h1>
      </IonContent>
    </IonApp>
  );
}}

export default App;
""",
        "README.md": f"""# {project_name}

Ionic project generated with Boilerplate Agent.
""",
    }


def generate_capacitor_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "capacitor.config.ts": f"""import {{ CapacitorConfig }} from '@capacitor/cli';

const config: CapacitorConfig = {{
  appId: 'com.example.{project_name}',
  appName: '{project_name}',
  webDir: 'dist',
  server: {{
    androidScheme: 'https'
  }}
}};

export default config;
""",
        "index.html": """<!DOCTYPE html>
<html>
<body>
    <h1>Hello World</h1>
    <script type="module" src="/src/main.ts"></script>
</body>
</html>
""",
        "src/main.ts": """import {{ Capacitor }} from '@capacitor/core';
console.log(Capacitor.isNativePlatform());
""",
        "README.md": f"""# {project_name}

Capacitor project generated with Boilerplate Agent.
""",
    }


def generate_elixir_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "mix.exs": f"""defmodule {project_name.replace("-", "_")}.MixProject do
  use Mix.Project

  def project do
    [
      app: :{project_name},
      version: "0.1.0",
      elixir: "~> 1.14"
    ]
  end
end
""",
        "lib/app.ex": """defmodule App do
  def hello do
    :world
  end
end
""",
        "README.md": f"""# {project_name}

Elixir project generated with Boilerplate Agent.
""",
    }


def generate_haskell_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "package.yaml": f"""name: {project_name}
version: 0.1.0.0

executable:
  main: Main.hs
  ghc-options:
    - -main-is
""",
        "app/Main.hs": """main :: IO ()
main = putStrLn "Hello World"
""",
        "README.md": f"""# {project_name}

Haskell project generated with Boilerplate Agent.
""",
    }


def generate_nim_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        f"{project_name}.nim": f"""# {project_name}

when isMainModule:
    echo "Hello World"
""",
        "README.md": f"""# {project_name}

Nim project generated with Boilerplate Agent.
""",
    }


def generate_dart_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "pubspec.yaml": f"""name: {project_name}
version: 1.0.0

environment:
  sdk: '>=3.0.0 <4.0.0'
""",
        "bin/main.dart": """void main() {
  print('Hello World');
}
""",
        "README.md": f"""# {project_name}

Dart project generated with Boilerplate Agent.
""",
    }


def generate_cpp_template(project_name: str, options: Dict = None) -> Dict[str, str]:
    return {
        "main.cpp": f"""#include <iostream>

int main() {{
    std::cout << "Hello World from {project_name}" << std::endl;
    return 0;
}}
""",
        "CMakeLists.txt": f"""cmake_minimum_required(VERSION 3.10)
project({project_name})

add_executable({project_name} main.cpp)
""",
        "README.md": f"""# {project_name}

C++ project generated with Boilerplate Agent.
""",
    }


def generate_swift_ios_template(
    project_name: str, options: Dict = None
) -> Dict[str, str]:
    return {
        "Package.swift": f"""// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "{project_name}",
    platforms: [.iOS(.v16)],
    products: [.library(name: "{project_name}", targets: ["{project_name}"])],
    targets: [.target(name: "{project_name}")]
)
""",
        f"Sources/{project_name}/main.swift": f"""import Foundation

print("Hello from {project_name}")
""",
        "README.md": f"""# {project_name}

Swift iOS project generated with Boilerplate Agent.
""",
    }
