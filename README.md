\# Trading SRE Platform



A production-ready DevOps \& Site Reliability Engineering (SRE) platform demonstrating a complete CI/CD, GitOps, Kubernetes, Security, and Monitoring workflow.



\---



\#  Project Overview



Trading SRE Platform is an end-to-end DevOps and Site Reliability Engineering (SRE) project designed to simulate a real-world production environment.



The platform demonstrates how modern DevOps tools work together to build, test, secure, deploy, and monitor cloud-native applications running on Kubernetes.



This project follows DevOps best practices including Infrastructure Automation, GitOps deployment, Continuous Integration, Continuous Delivery, Security Scanning, Monitoring, and Observability.



\---



\#  Project Objectives



\- Build a production-ready Flask microservice

\- Containerize the application using Docker

\- Automate CI/CD with Jenkins

\- Perform Static Code Analysis using SonarQube

\- Scan container images using Trivy

\- Store container images in Docker Hub

\- Deploy applications to Kubernetes

\- Implement GitOps using ArgoCD

\- Monitor infrastructure using Prometheus

\- Visualize metrics using Grafana

\- Expose custom application metrics using Prometheus Client



\---



\#  Project Architecture



```text

&#x20;                     Developer

&#x20;                         │

&#x20;                         ▼

&#x20;                     GitHub Repository

&#x20;                         │

&#x20;                         ▼

&#x20;                   Jenkins CI Pipeline

&#x20;                         │

&#x20;       ┌─────────────────┴──────────────────┐

&#x20;       │                                    │

&#x20;       ▼                                    ▼

&#x20;  SonarQube                           Trivy Scan

(Code Quality)                    (Security Scan)

&#x20;       │                                    │

&#x20;       └─────────────────┬──────────────────┘

&#x20;                         ▼

&#x20;                   Docker Build

&#x20;                         │

&#x20;                         ▼

&#x20;                    Docker Hub

&#x20;                         │

&#x20;                         ▼

&#x20;                       ArgoCD

&#x20;                   (GitOps Deploy)

&#x20;                         │

&#x20;                         ▼

&#x20;                    Kubernetes

&#x20;                         │

&#x20;         ┌───────────────┴───────────────┐

&#x20;         │                               │

&#x20;         ▼                               ▼

&#x20;    Flask Application               Prometheus

&#x20;         │                               │

&#x20;     /metrics Endpoint                   │

&#x20;         │                               │

&#x20;         └──────────────► Grafana ◄──────┘

```



\---



\# Technologies Used



| Category | Technology |

|----------|------------|

| Language | Python |

| Framework | Flask |

| Containerization | Docker |

| Registry | Docker Hub |

| CI/CD | Jenkins |

| Code Quality | SonarQube |

| Security | Trivy |

| Version Control | Git \& GitHub |

| GitOps | ArgoCD |

| Container Orchestration | Kubernetes |

| Monitoring | Prometheus |

| Dashboard | Grafana |



\---



\#  Project Structure



```

Trading-SRE-Platform

│

├── app/

│   └── order-service/

│       ├── app.py

│       ├── Dockerfile

│       ├── requirements.txt

│

├── kubernetes/

│   ├── namespace.yaml

│   ├── order-deployment.yaml

│   └── order-service.yaml

│

├── monitoring/

│

├── argocd/

│

├── jenkins/

│

├── terraform/

│

├── scripts/

│

├── docs/

│   └── images/

│

├── Jenkinsfile

│

├── order-servicemonitor.yaml

│

└── README.md

```



\---



\#  CI/CD Pipeline



The CI/CD workflow is fully automated.



\## Stage 1



Developer pushes code to GitHub.



↓



\## Stage 2



Jenkins automatically starts the pipeline.



↓



\## Stage 3



SonarQube performs Static Code Analysis.



↓



\## Stage 4



Trivy scans the Docker image for vulnerabilities.



↓



\## Stage 5



Docker builds the application image.



↓



\## Stage 6



Docker pushes the image to Docker Hub.



↓



\## Stage 7



GitHub manifests are updated.



↓



\## Stage 8



ArgoCD detects Git changes.



↓



\## Stage 9



Kubernetes deploys the latest version.



↓



\## Stage 10



Prometheus collects metrics.



↓



\## Stage 11



Grafana visualizes infrastructure and application metrics.



\---



\# Kubernetes Deployment



The application is deployed using:



\- Deployment

\- Service

\- Namespace

\- ServiceMonitor



Features include:



\- Multiple replicas

\- Readiness Probe

\- Liveness Probe

\- Resource Requests

\- Resource Limits

\- NodePort Service



\---



\#  GitOps with ArgoCD



ArgoCD continuously monitors the GitHub repository.



Whenever Kubernetes manifests are updated:



\- Git detects changes

\- ArgoCD automatically synchronizes

\- Kubernetes deploys the new version



Application status:



\- Healthy

\- Synced



\---



\#  Monitoring



Monitoring is implemented using Prometheus and Grafana.



Prometheus collects:



\- HTTP Requests

\- CPU Usage

\- Memory Usage

\- Process Metrics

\- Kubernetes Metrics



Grafana dashboards include:



\- CPU Usage

\- Memory Usage

\- Running Pods

\- Pod Restarts

\- Pod Status

\- HTTP Requests/sec

\- Total HTTP Requests

\- Application CPU

\- Application Memory



\---



\# 📈 Prometheus Metrics



Application metrics are exposed through:



```

/metrics

```



Example metrics:



```

http\_requests\_total



process\_cpu\_seconds\_total



process\_resident\_memory\_bytes



python\_gc\_objects\_collected\_total

```



\---



\#  Screenshots



\## Jenkins Pipeline



!\[Jenkins](docs/images/jenkins.png)



\---



\## SonarQube



!\[SonarQube](docs/images/sonarqube.png)



\---



\## Trivy Scan



!\[Trivy](docs/images/trivy.png)



\---



\## ArgoCD



!\[ArgoCD](docs/images/argocd.png)



\---



\## Prometheus



!\[Prometheus](docs/images/prometheus.png)



\---



\## Grafana Dashboard



!\[Grafana](docs/images/grafana.png)



\---



\# Installation



Clone repository



```bash

git clone https://github.com/gidikoml/Trading-SRE-Platform.git

```



Enter project



```bash

cd Trading-SRE-Platform

```



Build Docker image



```bash

docker build -t trading-order-service .

```



Deploy Kubernetes resources



```bash

kubectl apply -f kubernetes/

```



Deploy ServiceMonitor



```bash

kubectl apply -f order-servicemonitor.yaml

```



\---



\#  Features Demonstrated



\- CI/CD Automation

\- GitOps Deployment

\- Kubernetes Deployment

\- Container Security

\- Code Quality Analysis

\- Docker Image Management

\- Monitoring \& Observability

\- Production Health Checks

\- Prometheus Metrics

\- Grafana Dashboards



\---



\#  Future Improvements



\- Helm Charts

\- Terraform Infrastructure

\- AWS EKS Deployment

\- Alertmanager Notifications

\- Slack Alerts

\- Horizontal Pod Autoscaler

\- Ingress Controller

\- HTTPS with TLS

\- Loki Logging

\- Distributed Tracing

\- Multi-Environment Deployment



\---



\#  Author



\*\*Komlavi Gidi\*\*



DevOps | Cloud | Kubernetes | Platform Engineer | Site Reliability Engineer



GitHub:



https://github.com/gidikoml



\---



\# If you found this project useful, please consider giving it a Star!

