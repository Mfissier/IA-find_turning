# Makefile pour créer l'architecture du projet LLM_Customization_Project

.PHONY: all clean script install_ollama create_folders install

all: create_folders install_ollama install script 

script:
	git clone https://github.com/Mfissier/PYTHON_.git ./LLM_Customization_Project/Data/script/PYTHON_ && \
	mv LLM_Customization_Project/Data/script/PYTHON_/* LLM_Customization_Project/Data/script/ && \
	rm -rf LLM_Customization_Project/Data/script/PYTHON_

install_ollama:
	@echo "Setting up virtual environment and installing Ollama..."
	python3 -m venv llama_env && \
	. llama_env/bin/activate && \
	echo "Virtual environment activated." 
	# Place Ollama installation commands here if available for Linux
	llama_env/bin/pip install ollama

create_folders:
	mkdir -p LLM_Customization_Project/Data/raw_data
	mkdir -p LLM_Customization_Project/Data/processed_data
	mkdir -p LLM_Customization_Project/Data/synthetic_data
	mkdir -p LLM_Customization_Project/Data/script
	mkdir -p LLM_Customization_Project/Models/base_models
	mkdir -p LLM_Customization_Project/Models/fine_tuned_models
	mkdir -p LLM_Customization_Project/Models/continued_pretrained_models
	mkdir -p LLM_Customization_Project/Models/compressed_models
	mkdir -p LLM_Customization_Project/Training/scripts
	mkdir -p LLM_Customization_Project/Training/config
	mkdir -p LLM_Customization_Project/Training/logs
	mkdir -p LLM_Customization_Project/Training/checkpoints
	mkdir -p LLM_Customization_Project/Evaluation/test_data
	mkdir -p LLM_Customization_Project/Evaluation/metrics
	mkdir -p LLM_Customization_Project/Evaluation/human_evaluation
	mkdir -p LLM_Customization_Project/Evaluation/reports
	mkdir -p LLM_Customization_Project/Deployment/docker
	mkdir -p LLM_Customization_Project/Deployment/kubernetes
	mkdir -p LLM_Customization_Project/Deployment/scaling
	mkdir -p LLM_Customization_Project/Deployment/monitoring
	mkdir -p LLM_Customization_Project/Documentation/methodology
	mkdir -p LLM_Customization_Project/Documentation/config_docs
	mkdir -p LLM_Customization_Project/Documentation/evaluation_reports
	mkdir -p LLM_Customization_Project/Documentation/deployment_guide

install: install_ollama
	llama_env/bin/pip install -r requirements.txt

clean:
	rm -rf LLM_Customization_Project llama_env
