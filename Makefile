python = python3
pip = pip3


install:
	$(pip) install -r requirements.txt

clean:
	rm -rf __pycache__/
	rm -rf build/

run:
	$(python) main.py