# sad-project
# Members
- **Devyani Dubey** - docker-compose.yml for elk-stack 80%, backend for logging 30%
- **Anuj Gupta** - Django back-end development 80%, initial basic front-end design 100%, load balancing 100%
- **Abhinav Lugun** - Improved front-end design 100%, setup Dockfile and docker-compose.yml 100%, Django back-end development: 15%,  
- **Marie Curie Salera** - Setting up of repository 100%, Initial Django Logging 100%, Implementation of ELK for logging 100%, Django backend development 15%

# How to Run
1. Enter `SAD/crud` and run `docker-compose up --build -d`.
2. Run `docker-compose run web python3 manage.py migrate`.
3. Enter `nginx-1.21.6` and run command `nginx`.
4. Navigate to `http://localhost/` on browser.

## ELK Setup
1. Run the command ```curl -XPOST -D- "http://localhost:5601/api/saved_objects/index-pattern" \
    -H "Content-Type: application/json" \
    -H "kbn-version: 6.1.0" \
    -d "{'attributes':{'title':'logstash-*','timeFieldName':'@timestamp'}}"```
2. Navigate to `http://localhost:5601/`

## Documents
1. Project Presentation - https://docs.google.com/presentation/d/1dXpTHFqFMV7D8KSz6An6Mgf38JzkD2OGU53JLG2fM4E/edit?usp=sharing
2. Final Project Report - https://docs.google.com/document/d/1cm9ItTzX0pdK51E61_Yoq8z9nMHr10r_mBtLMhjahTQ/edit?usp=sharing
