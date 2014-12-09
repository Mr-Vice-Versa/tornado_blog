# Tornado Blog Project

#### (c) Vladyslav Ishchenko 12.2014
#### http://python-django.net


### Goal:
	The project was written for the purpose of practice in a modern web technology in a 4 days estimate.
	Tornado web framework and Riak distributed database was for me new.
	During working with these technologies in a further code source will be improved.

### Technology stack

### Backend:
    Main framefork:
    	Tornado version 4.0.2
			https://github.com/tornadoweb/tornado
			http://www.tornadoweb.org/en/stable/
	DB:
		MySQL
		Riack
		http://docs.basho.com/riak/2.0.0/
		Install:
			curl https://packagecloud.io/install/repositories/basho/riak/script.deb | sudo bash
			sudo apt-get install riak=2.0.0-1
	
		Python clients lib for Riak:
			http://docs.basho.com/riak/latest/dev/using/libraries/
			http://basho.github.io/riak-python-client/index.html
			https://github.com/basho/riak-python-client

### Frontend:
	Same of them usage same not. I use it to experiment.
		jquery
		underscore
		backbone
        backbone-relational
		requirejs-text plugin
        modernizr
		backbone.paginator
		backbone-forms
		backbone.marionette
		bootstrap from Twitter:
	Project layout:
		https://github.com/ironsummitmedia/startbootstrap-clean-blog

### Deploying Tornado Blog Project:

	Look here for base install:
		https://github.com/tornadoweb/tornado/tree/stable/demos/blog

* 1. Install prerequisites and build tornado
* 2. Install DB: MySQL/Riak
	* MySQL schema
		* mysql --user=blog --password=blog --database=blog < schema.sql
* 3. Install project prerequisites
	* pip install -r requirements.txt
	* Seletc DB: Riak or MySQL in settings.py (Options: DB)
	* If you change DB, do:
	* Clear Cookies in brovser
* 4. Run Tornado Blog
	* cd
	* ./app.py
	* If need chmod +x app.py
* 5. Go to the site
   > http://localhost:8888/

### TODO:
	tests
	fabfile

### TODO Global:
	Better Design Web all of App (DIVIDE AND CONQUER)
	Generalization, decomposition, design patterns of scale web app.
	FRONTEND:
		REFACTORING and rewrite JavaScript (View, ect)
		Remove DYR!
	BACKEND
		API:
			Better design URL (ugly url - slug)
			Rewrite Tornado handlers by DB TYPE.
			With one interface for different DB.
			API for UPDATE/DELETE ect.
		DB design(data structure):
			unique ID, Counters ect.
			Riak MapReduce, Riak ORM
			Better ORM (Riak)
			Better QUERYSETS methods
			Optimisation queries
		Templates:
			Better templates (front/back-end)
			Optimisation
			Add same fields to templates
		Also:
 			Paginations on backends and frontends.

#### (c) Vladyslav Ishchenko 12.2014, http://python-django.net