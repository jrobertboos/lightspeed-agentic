# Lightspeed Agentic

A multi-agent system built with FastAPI and the OpenAI Agents SDK, powered by Llama Stack for inference.

## Overview

Lightspeed Agentic uses an orchestrator agent to route queries to specialized agents for Red Hat products:

- **OpenShift** - OpenShift Container Platform expertise
- **RHEL** - Red Hat Enterprise Linux administration
- **Ansible** - Ansible Automation Platform guidance
- **Developer Hub** - Red Hat Developer Hub / Backstage
- **OKP** - General RAG agent for knowledge retrieval

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Llama Stack running locally (or remote endpoint)

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. Start Llama Stack:
   ```bash
   uv run llama stack run llama-stack-config.yaml
   ```

4. Start the application:
   ```bash
   uv run lightspeed-agentic
   ```

## Configuration

Edit `lightspeed-config.yaml` to configure the service:

```yaml
name: Lightspeed Agentic
service:
  host: 0.0.0.0
  port: 8080

llama_stack:
  url: http://localhost:8321/v1/

agents:
  - name: openshift
    config: {}
  - name: rhel
    config: {}
  - name: ansible
    config: {}
  - name: developer_hub
    config: {}
```

## Usage

Send queries to the `/query` endpoint:

```bash
curl -X POST http://localhost:8080/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I deploy an application on OpenShift?"}'
```

API documentation available at `http://localhost:8080/docs`.

## Adding Custom Agents

See [src/agents/README.md](src/agents/README.md) for instructions on creating custom agents.

## Project Structure

```
src/
  agents/          # Agent implementations
  app/             # FastAPI application
    endpoints/     # API endpoints
  config/          # Configuration loading
  runners/         # Application runners
```
