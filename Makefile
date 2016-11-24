tests:
	python test_pinyin.py
	python3 test_pinyin.py
	python3 test_cedict.py

cedict:
	wget https://www.mdbg.net/chindict/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz -O -  > pinyin/cedict.txt.gz

pep8:
	pep8 *py pinyin/*py
