.PHONY: build install cppinstall test pytest cpptest clean lint pylint cpplint format pyformat cppformat

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

build: cppinstall
	mkdir -p build
	cd build && cmake .. \
		-DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake \
		-DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) \
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
		-G Ninja
	cd build && cmake --build .
	ln -sf build/compile_commands.json compile_commands.json
	@cp -f build/*.so $(PY_SRC)

install:
	poetry lock --no-update
	poetry env use python3.12
	poetry install

cppinstall:
	conan install . --build=missing

test: build pytest cpptest

pytest: install build
	@poetry run pytest $(PY_SRC)/test

cpptest: build
	@cd build && ./intern_tests

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so
	@rm -f compile_commands.json

lint: pylint cpplint

pylint:
	poetry run mypy $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

cpplint: build
	run-clang-tidy -j $(shell nproc) -p build
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i

format: pyformat cppformat

pyformat:
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)

cppformat: build
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	run-clang-tidy -fix -j $(shell nproc) -p build
