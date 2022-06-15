SUBDIR_GOALS=all clean distclean

SUBDIR+=	src/nytid/schedules
SUBDIR+=	doc

.PHONY: all publish

all:
publish: all
	poetry build
	poetry publish


.PHONY: clean
clean:
	${RM} -Rf dist

INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
