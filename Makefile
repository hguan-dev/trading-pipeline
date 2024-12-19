.PHONY: build pythoninstall cppinstall test pytest-unit pytest-integration cpptest clean lint pylint cpplint format pyformat cppformat

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

# Build C++ Project
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
	pip install --upgrade pip
	pipx install --force conan
	@if [ ! -f ~/.conan2/profiles/default ]; then \
		conan profile detect; \
	else \
		echo "Conan default profile already exists, skipping profile detection."; \
	fi
	pipx install --force ninja
	conan install . --build=missing

test: pytest-unit pytest-integration cpptest

# Python Tests
pytest-unit: pythoninstall build
	@poetry run pytest $(PY_SRC)/test/unit

pytest-integration: pythoninstall build
	@poetry run pytest $(PY_SRC)/test/integration

# C++ Tests
cpptest: build
	@cd build && ./intern_tests

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so

lint: pylint cpplint

# Python Linting
pylint: pythoninstall
	poetry run mypy --install-types --non-interactive $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

# C++ Linting
cpplint: build
	run-clang-tidy -j $(shell nproc) -p build
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i

format: pyformat cppformat

# Python Formatting
pyformat: pythoninstall
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)

# C++ Formatting
cppformat: build
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	run-clang-tidy -fix -j $(shell nproc) -p build
