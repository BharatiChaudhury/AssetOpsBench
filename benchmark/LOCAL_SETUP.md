# Local Setup Guide for AssetOpsBench

Since the pre-built Docker images are not publicly available, here's how to set up AssetOpsBench locally.

## Option 1: Local Python Environment (Recommended)

### Prerequisites
- Python 3.12
- pip or conda
- Git

### Setup Steps

1. **Clone the repository** (if not already done):
```bash
git clone https://github.com/IBM/AssetOpsBench.git
cd AssetOpsBench
```

2. **Create a virtual environment**:
```bash
python -m venv assetopsbench-env
source assetopsbench-env/bin/activate  # On Windows: assetopsbench-env\Scripts\activate
```

3. **Install basic requirements**:
```bash
cd benchmark
pip install -r basic_requirements.txt
```

4. **Install additional packages**:
```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn transformers torch langchain termcolor
```

5. **Set up CouchDB** (optional, for full functionality):
```bash
# Install CouchDB locally or use Docker
docker run -d --name couchdb -p 5984:5984 couchdb:3.5
```

6. **Set environment variables**:
```bash
export PYTHONPATH=/path/to/AssetOpsBench/src
export COUCHDB_URL=http://localhost:5984
```

## Option 2: Build Docker Image Locally

If you prefer Docker, you can build the image locally:

1. **Build the Docker image**:
```bash
cd benchmark
docker build -t assetopsbench-local .
```

2. **Update docker-compose.yml** (already done):
The docker-compose.yml has been updated to use local build instead of pre-built images.

3. **Run with Docker**:
```bash
docker-compose up
```

## Running the Benchmark

### Basic Usage

1. **Navigate to the src directory**:
```bash
cd ../src
```

2. **Run a simple test**:
```bash
python -c "
from meta_agent.default_meta_agent import AgentHub
agent_hub = AgentHub()
agent_hub.display_agents_and_examples()
"
```

### Running Specific Scenarios

1. **Single agent scenarios**:
```bash
cd src/meta_agent
python -c "
from default_meta_agent import AgentHub
agent_hub = AgentHub()
result = agent_hub.run('What IoT sites are available?')
print(result)
"
```

2. **Multi-agent scenarios**:
```bash
cd src/agent_hive
python run_plan_execute.py --help
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure PYTHONPATH is set correctly
2. **Missing dependencies**: Install additional packages as needed
3. **CouchDB connection**: Ensure CouchDB is running and accessible

### Getting Help

- Check the main README.md for more details
- Review the source code in the `src/` directory
- Look at the scenario files in the `scenarios/` directory

## Next Steps

Once the basic setup is working, you can:

1. **Explore the scenarios**: Look at the JSON files in `scenarios/`
2. **Run benchmarks**: Use the provided scripts to evaluate different models
3. **Customize agents**: Modify or extend the existing agents
4. **Add new scenarios**: Create your own benchmark scenarios

## Note

The original Docker images contained pre-built agents from IBM's internal repositories. For full functionality, you may need to:
- Set up API keys for external services
- Install additional dependencies as needed
- Configure model endpoints for LLM inference 