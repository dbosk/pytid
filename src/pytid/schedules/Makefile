.PHONY: all
all: __init__.py

.INTERMEDIATE: init.py

__init__.py: init.py
	${MV} $^ $@


.PHONY: clean
clean:
	${RM} init.py __init__.py init.tex


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
