.PHONY: build install cppinstall test pytest-unit pytest-integration cpptest clean lint pylint cpplint format pyformat cppformat

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
	@cp -f build/*.so $(PY_SRC)

# Poetry Installation
pythoninstall:
	pipx install poetry
	poetry install

# Conan Installation
cppinstall:
	conan install . --build=missing

test: pytest-unit pytest-integration cpptest-unit cpptest-integration

# Python Tests
pytest-unit: pythoninstall
	@poetry run pytest $(PY_SRC)/test/unit

pytest-integration: pythoninstall
	@poetry run pytest $(PY_SRC)/test/integration

# Cpp Tests (to be finished)
cpptest: build dependencies
	@cd build && ./intern_tests

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so

lint: pylint cpplint

# Python Linting
pylint: pyinstall
	poetry run mypy --install-types --non-interactive $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

# Cpp Linting
cpplint: dependencies
	run-clang-tidy -j $(shell nproc) -p build
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i

format: pyformat cppformat

# Cpp Dependencies
dependencies:
	pip install --upgrade pip
	pipx install conan
	conan profile detect
	bash < .github/scripts/conan-profile.sh
	pipx install ninja

# Python Dependencies
pyformat: pyinstall
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)

cppformat: dependencies
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	run-clang-tidy -fix -j $(shell nproc) -p build
