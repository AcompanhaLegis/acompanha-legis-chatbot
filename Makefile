train:
	docker-compose run -v ${PWD}:/opt/chatbot:rw rasa-core_1 rasa train
