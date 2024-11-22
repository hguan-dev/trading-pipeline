.PHONY: build install cppinstall test pytest cpptest clean lint pylint cpplint format pyformat cppformat

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

build: cppinstall
	cd build && cmake .. \
		-DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake \
		-DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) \
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
		-G Ninja
	cd build && cmake --build .
	@cp -f build/*.so $(PY_SRC)

install:
	poetry lock --no-update
	poetry env use python3.12
	poetry install

cppinstall:
	conan install . --build=missing

test: build pytest cpptest

pytest:
	@poetry run pytest $(PY_SRC)/test

cpptest:
	@cd build && ./intern_tests

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so

lint: pylint cpplint

pylint:
	poetry run mypy $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

cpplint:
	run-clang-tidy -j $(shell nproc) -p build

format: pyformat cppformat

pyformat:
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)

cppformat:
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	run-clang-tidy -fix -j $(shell nproc) -p build
