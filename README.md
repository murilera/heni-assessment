# heni-assessment

first clone project and access projects folder

#### 1. setup env

```
pip install virtualenv
virtualenv env
source env/bin/activate
```

#### 2. install requirements

```
pip install -r requirements.txt
```

#### 3. run files

```
python 1-parsing-html.py
python 2-regex.py
python 3-web-cawler.py
python 4-data.py
```

#### 4. scrapy spider

```
cd web_crawler
scrapy crawl bearspace -O products.json
```

#### todo/improvements

- define scrapy/requests item class
- improve pandas/numpy knowledge
