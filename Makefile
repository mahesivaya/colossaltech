# hello:
# 	echo "Hello, World"

files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file

file1:
	touch file1
file2:
	touch file2

clean:
	rm -f file1 file2 some_file

migrate:
	python3 ./colossal_main/manage.py migrate

makemigrations:
	python3 ./colossal_main/manage.py makemigrations

runserver:
	python3 ./colossal_main/manage.py runserver