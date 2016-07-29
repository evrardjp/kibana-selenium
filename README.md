# kibana-selenium
Kibana testing framework which uses selenium webdriver and phantomjs.


## Install

```bash
**Optional: 
    pip install virtualenv
    virtualenv ~/venv/kib-sel
    . ~/venv/kib-sel/bin/activate

**Required
    cd /opt && git clone https://github.com/Rydor/kibana-selenium.git   
    cd kibana-selenium
    pip install -r requirements.txt
    export PYTHONPATH=$(pwd)

**Configuration file generator
    python config-gen.py
```

## Test execution

```
cd /opt/kibana-selenium/testrepo/kibana
python kibana.py
```
